from ultravox_vllm.monkeypatch import patch_vllm

patch_vllm()

from vllm import ModelRegistry
from ultravox_vllm.models.ultravox import UltravoxModel
import runpy

ModelRegistry.register_model("UltravoxModel", UltravoxModel)
runpy.run_module('vllm.entrypoints.openai.api_server', run_name='__main__')