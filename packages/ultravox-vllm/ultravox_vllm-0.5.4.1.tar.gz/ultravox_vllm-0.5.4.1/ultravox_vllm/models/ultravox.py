# coding=utf-8
# NB chua: modified from https://github.com/huggingface/transformers/blob/v4.37.2/src/transformers/models/llava/modeling_llava.py#L350
# Copyright 2023 the HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""PyTorch Ultravox model."""

from functools import lru_cache
import math
from typing import Iterable, List, Optional, Protocol, Tuple, Union, cast

import librosa
import numpy as np
import torch
import torch.utils.checkpoint
from torch import nn
from torch.nn import functional as F

from transformers import activations, PretrainedConfig, logging
from transformers.models.llama.modeling_llama import LlamaRMSNorm
from transformers.models.whisper import WhisperFeatureExtractor

from vllm.attention import AttentionMetadata
from vllm.config import CacheConfig, MultiModalConfig
from vllm.inputs import INPUT_REGISTRY
from vllm.inputs.data import LLMInputs
from vllm.inputs.registry import InputContext
from vllm.model_executor.layers.logits_processor import LogitsProcessor
from vllm.model_executor.layers.quantization.base_config import (
    QuantizationConfig)
from vllm.model_executor.layers.sampler import Sampler
from vllm.model_executor.layers.vocab_parallel_embedding import ParallelLMHead
from vllm.model_executor.models.interfaces import SupportsVision
from vllm.model_executor.models.utils import merge_vision_embeddings
from ultravox_vllm.models.whisper_streaming import WhisperEncoder

from vllm.model_executor.sampling_metadata import SamplingMetadata
from vllm.multimodal import MULTIMODAL_REGISTRY
from vllm.multimodal.base import BatchedTensors, MultiModalInputs
from vllm.multimodal.image import repeat_and_pad_image_tokens
from vllm.sequence import SamplerOutput, SequenceData

from vllm.transformers_utils.tokenizer import get_tokenizer

@lru_cache
def cached_get_auto_processor(
    processor_name: str,
    *args,
    trust_remote_code: bool = False,
    **kwargs,
):
    """Gets an auto processor for the given model name via HuggingFace."""
    # don't put this import at the top level
    # it will call torch.cuda.device_count()
    from transformers import AutoProcessor

    try:
        processor = AutoProcessor.from_pretrained(
            processor_name,
            *args,
            trust_remote_code=trust_remote_code,
            **kwargs)
    except ValueError as e:
        # If the error pertains to the processor class not existing or not
        # currently being imported, suggest using the --trust-remote-code flag.
        # Unlike AutoTokenizer, AutoImageProcessor does not separate such errors
        if not trust_remote_code:
            err_msg = (
                "Failed to load the processor. If the processor is "
                "a custom processor not yet available in the HuggingFace "
                "transformers library, consider setting "
                "`trust_remote_code=True` in LLM or using the "
                "`--trust-remote-code` flag in the CLI.")
            raise RuntimeError(err_msg) from e
        else:
            raise e

    return processor

cached_get_tokenizer = lru_cache(get_tokenizer)

_KEYS_TO_MODIFY_MAPPING = {
    "language_model.lm_head": "lm_head",
    "language_model.model": "language_model",
}

_AUDIO_PLACEHOLDER_TOKEN = 128002
_AUDIO_TOKENS_PER_SECOND = 6.25

logger = logging.get_logger(__name__)

def whisper_feature_extractor() -> WhisperFeatureExtractor:
    whisper_processor = cached_get_auto_processor(
        "openai/whisper-small",
        trust_remote_code=True,
    )
    return whisper_processor.feature_extractor

def get_ultravox_max_audio_tokens(ctx: InputContext):
    feature_extractor = whisper_feature_extractor()
    return math.ceil(feature_extractor.chunk_length * _AUDIO_TOKENS_PER_SECOND)

def dummy_data_for_ultravox(ctx: InputContext, seq_len: int):
    feature_extractor = whisper_feature_extractor()
    audio_tokens = get_ultravox_max_audio_tokens(ctx)

    fake_audio = np.array([0.0] * feature_extractor.chunk_length)
    fake_sample_rate = 1
    return (
        SequenceData([0] * (seq_len - audio_tokens) + [_AUDIO_PLACEHOLDER_TOKEN] * audio_tokens),
        { "image": (fake_audio, fake_sample_rate) }
    )

def input_mapper_for_ultravox(ctx: InputContext, data: object):
    if isinstance(data, tuple):
        (audio, sr) = cast(Tuple[np.ndarray, Union[float, int]], data)
        feature_extractor = whisper_feature_extractor()

        if sr != feature_extractor.sampling_rate:
            audio = librosa.resample(audio, orig_sr=sr, target_sr=feature_extractor.sampling_rate)
            sr = feature_extractor.sampling_rate

        minimum_audio_length = feature_extractor.n_fft // 2 + 1
        if len(audio) < minimum_audio_length:
            # Not enough audio; pad it.
            audio = np.pad(audio, (0, minimum_audio_length - len(audio)))

        return MultiModalInputs(feature_extractor(audio, sampling_rate=sr, padding="longest", return_tensors="pt"))

    raise NotImplementedError(f"Unsupported data type: {type(data)}")

def input_processor_for_ultravox(ctx: InputContext, llm_inputs: LLMInputs):
    multi_modal_data = llm_inputs.get("multi_modal_data")
    if multi_modal_data is None or "image" not in multi_modal_data:
        return llm_inputs

    feature_extractor = whisper_feature_extractor()
    audio_data, sample_rate = multi_modal_data["image"]

    audio_length = audio_data.shape[0]
    if sample_rate != feature_extractor.sampling_rate:
        # Account for resampling.
        adjustment = feature_extractor.sampling_rate / sample_rate
        audio_length = math.ceil(adjustment * audio_length)

    feature_extractor_output_length = math.ceil((audio_length - (feature_extractor.hop_length - 1)) / feature_extractor.hop_length)
    audio_num_tokens = min(max(1, math.ceil(feature_extractor_output_length / 16)), get_ultravox_max_audio_tokens(ctx))
    tokenizer = cached_get_tokenizer(ctx.model_config.tokenizer)

    new_prompt, new_token_ids = repeat_and_pad_image_tokens(
        tokenizer,
        llm_inputs.get("prompt"),
        llm_inputs["prompt_token_ids"],
        image_token_id=_AUDIO_PLACEHOLDER_TOKEN,
        repeat_count=audio_num_tokens,
    )

    # NOTE: Create a defensive copy of the original inputs
    return LLMInputs(prompt_token_ids=new_token_ids,
                     prompt=new_prompt,
                     multi_modal_data=multi_modal_data)

class StackAudioFrames(nn.Module):
    """
    Stack the audio embedding frames to reduce the sequence length by a factor of `stack_factor`.
    """

    def __init__(self, stack_factor: int = 8):
        super().__init__()
        self.stack_factor = stack_factor

    def forward(self, audio_embeds: torch.Tensor) -> torch.Tensor:
        B, T, C = audio_embeds.shape
        T_pad = (T + self.stack_factor - 1) // self.stack_factor * self.stack_factor
        audio_embeds = F.pad(audio_embeds, (0, 0, 0, T_pad - T))
        B, T, C = audio_embeds.shape
        audio_embeds = audio_embeds.view(
            B, T // self.stack_factor, C * self.stack_factor
        )
        return audio_embeds


class RMSNorm(LlamaRMSNorm):
    def __init__(self, hidden_size: int, init: float = 1, eps: float = 1e-6):
        super().__init__(hidden_size=hidden_size, eps=eps)
        self.weight.data.fill_(init)


class SwiGLU(nn.Module):

    def forward(self, x):
        x, gate = x.chunk(2, dim=-1)
        return F.silu(gate) * x

class UltravoxConfig(Protocol):
    hidden_size: int
    stack_factor: int
    audio_config: PretrainedConfig
    text_config: PretrainedConfig
    projector_act: str

class UltravoxProjector(nn.Sequential):
    def __init__(self, config: UltravoxConfig):
        super().__init__()
        self.hidden_dim = config.hidden_size
        self._pad_and_stack = StackAudioFrames(config.stack_factor)
        dim = config.audio_config.hidden_size * config.stack_factor
        self.ln_pre = RMSNorm(dim, init=config.norm_init)
        self.linear_1 = nn.Linear(dim, self.hidden_dim, bias=False)
        dim = self.hidden_dim
        self.act = SwiGLU() if config.projector_act == "swiglu" else activations.get_activation(config.projector_act)
        dim = dim // 2 if config.projector_act == "swiglu" else dim
        self.linear_2 = nn.Linear(dim, config.text_config.hidden_size, bias=False)
        self.ln_post = RMSNorm(config.text_config.hidden_size, init=config.norm_init)

    def forward(self, audio_features: torch.Tensor) -> torch.Tensor:
        audio_features = self._pad_and_stack(audio_features)
        audio_features = self.ln_pre(audio_features)
        hidden_states = self.linear_1(audio_features)
        hidden_states = self.act(hidden_states)
        hidden_states = self.linear_2(hidden_states)
        hidden_states = self.ln_post(hidden_states)
        return hidden_states


@MULTIMODAL_REGISTRY.register_image_input_mapper(input_mapper_for_ultravox)
@MULTIMODAL_REGISTRY.register_max_image_tokens(get_ultravox_max_audio_tokens)
@INPUT_REGISTRY.register_dummy_data(dummy_data_for_ultravox)
@INPUT_REGISTRY.register_input_processor(input_processor_for_ultravox)
class UltravoxModel(nn.Module, SupportsVision):
    def __init__(self,
                 config: UltravoxConfig,
                 multimodal_config: MultiModalConfig,
                 cache_config: Optional[CacheConfig] = None,
                 quant_config: Optional["QuantizationConfig"] = None):
        from vllm.model_executor.models.llama import LlamaModel
        super().__init__()
        self.config = config
        self.multi_modal_config = multimodal_config
        assert self.multi_modal_config

        if config.audio_model_id is not None:
            self.audio_tower = WhisperEncoder.from_pretrained(config.audio_model_id)
        else:
            self.audio_tower = WhisperEncoder.from_config(config.audio_config)
        self.audio_tower = self.audio_tower.to("cuda")
        torch.compile(self.audio_tower)
        self.audio_tower.eval()

        self.multi_modal_projector = UltravoxProjector(config).to("cuda")
        self.quant_config = quant_config

        self.language_model = LlamaModel(config.text_config, cache_config, quant_config)
        self.unpadded_vocab_size = config.text_config.vocab_size
        self.lm_head = ParallelLMHead(
            self.unpadded_vocab_size,
            config.text_config.hidden_size,
            org_num_embeddings=self.language_model.org_vocab_size)
        logit_scale = getattr(config, "logit_scale", 1.0)
        self.logits_processor = LogitsProcessor(self.unpadded_vocab_size,
                                                config.text_config.vocab_size,
                                                logit_scale)
        self.sampler = Sampler()

    def _audio_features_to_embeddings(self, input_features: torch.Tensor, dtype: torch.dtype) -> torch.Tensor:
        audio_input = input_features.to(self.audio_tower.dtype)
        audio_features = self.audio_tower(audio_input).last_hidden_state
        audio_features = audio_features.to(self.audio_tower.dtype)
        audio_embeddings = self.multi_modal_projector(audio_features).to(dtype)
        return audio_embeddings

    def forward(
        self,
        input_ids: torch.Tensor,
        positions: torch.Tensor,
        kv_caches: List[torch.Tensor],
        attn_metadata: AttentionMetadata,
        intermediate_tensors: Optional[torch.Tensor],
        *,
        input_features: Optional[BatchedTensors] = None,
    ) -> SamplerOutput:  # noqa: E501
        """Run forward pass for Ultravox

        One key thing to understand is the `input_ids` already accounts for the
        positions of the to-be-inserted audio embeddings.
        Concretely, consider a text prompt:
        "<|audio|>\nUSER: What's the content of the audio?\nASSISTANT:".
        Tokenizer outputs:
        [1, 32000, 29871, 13, 11889, 29901, 1724, 29915, 29879, 278,
        2793, 310, 278, 1967, 29973, 13, 22933, 9047, 13566, 29901].
        The to-be-inserted audio has a size that is essentially 6.25 tokens
        per second of audio.        
        `input_ids` is thus [1, 32000, ..., 32000, 29871, 13, 11889, 29901,
        1724, 29915, 29879, 278, 2793, 310, 278, 1967, 29973, 13, 22933,
        9047, 13566, 29901].
        For a 3-second clip, there will be ~19 `32000` in the `input_ids`.
        (32000 is the token id for `<audio>` when using Llama 2 as the backbone.)

        This way, the `positions` and `attn_metadata` are consistent
        with the `input_ids`.

        Args:
            input_ids: Flattened (concatenated) input_ids corresponding to a
                batch.
            image_input: A batch of audio inputs, [1, 80, M].
        """
        if input_features is not None:
            inputs_embeds = self.language_model.get_input_embeddings(input_ids)
            if isinstance(input_features, list):
                # TODO: Batch these through the encoder/projector instead of serializing them.
                audio_embeddings = [
                    self._audio_features_to_embeddings(single_features.unsqueeze(0), inputs_embeds.dtype).squeeze(0) for single_features in input_features
                ]
            elif isinstance(input_features, torch.Tensor):
                audio_embeddings = self._audio_features_to_embeddings(input_features, inputs_embeds.dtype)
            else:
                raise ValueError(f"The input audio features should be a tensor or a list of tensors, not {type(input_features)}")

            merge_vision_embeddings(input_ids, inputs_embeds, audio_embeddings, _AUDIO_PLACEHOLDER_TOKEN)
            input_ids = None
        else:
            inputs_embeds = None

        hidden_states = self.language_model(input_ids=input_ids,
                                            positions=positions,
                                            kv_caches=kv_caches,
                                            attn_metadata=attn_metadata,
                                            intermediate_tensors=intermediate_tensors,
                                            inputs_embeds=inputs_embeds)
        return hidden_states

    def compute_logits(self, hidden_states: torch.Tensor,
                       sampling_metadata: SamplingMetadata) -> torch.Tensor:
        logits = self.logits_processor(self.lm_head, hidden_states,
                                       sampling_metadata)
        return logits

    def sample(
        self,
        logits: torch.Tensor,
        sampling_metadata: SamplingMetadata,
    ) -> Optional[SamplerOutput]:
        next_tokens = self.sampler(logits, sampling_metadata)
        return next_tokens

    def load_weights(self, weights: Iterable[Tuple[str, torch.Tensor]]):
        from vllm.model_executor.model_loader.weight_utils import default_weight_loader
        # only doing this for language model part for now.
        stacked_params_mapping = [
            # (param_name, shard_name, shard_id)
            ("qkv_proj", "q_proj", "q"),
            ("qkv_proj", "k_proj", "k"),
            ("qkv_proj", "v_proj", "v"),
            ("gate_up_proj", "gate_proj", 0),
            ("gate_up_proj", "up_proj", 1),
        ]
        params_dict = dict(self.named_parameters())
        for name, loaded_weight in weights:
            if "rotary_emb.inv_freq" in name:
                continue
            for key_to_modify, new_key in _KEYS_TO_MODIFY_MAPPING.items():
                if key_to_modify in name:
                    name = name.replace(key_to_modify, new_key)
            use_default_weight_loading = False
            if "audio" in name:
                if self.audio_tower is not None:
                    # We only do sharding for language model and
                    # not audio model for now.
                    use_default_weight_loading = True
            else:
                for (param_name, weight_name,
                     shard_id) in stacked_params_mapping:
                    if weight_name not in name:
                        continue
                    new_name = name.replace(weight_name, param_name)
                    param = params_dict[new_name]
                    weight_loader = param.weight_loader
                    weight_loader(param, loaded_weight, shard_id)
                    break
                else:
                    use_default_weight_loading = True
            if use_default_weight_loading:
                param = params_dict[name]
                weight_loader = getattr(param, "weight_loader",
                                        default_weight_loader)
                weight_loader(param, loaded_weight)
