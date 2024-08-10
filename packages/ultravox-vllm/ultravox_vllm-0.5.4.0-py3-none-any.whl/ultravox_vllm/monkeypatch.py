import sys
import wrapt

_PLACEHOLDER_PSEUDO_TOKEN = "<|audio|>"
_PLACEHOLDER_TOKEN = "<|reserved_special_token_0|>"

def _patch_multimodal_utils(module):
    import base64
    from io import BytesIO

    import librosa
    from vllm.connections import global_http_connection
    from vllm.envs import VLLM_IMAGE_FETCH_TIMEOUT

    def _load_audio_from_bytes(audio: bytes):
        result = librosa.load(BytesIO(audio), sr=None)
        return result

    @wrapt.patch_function_wrapper(module, "fetch_image")
    def _patched_fetch_image(wrapped, instance, args, kwargs):
        """
        Load a PIL image from a HTTP or base64 data URL.

        By default, the image is converted into RGB format.
        """
        

        image_url, = args
        if image_url.startswith('http'):
            image_raw = global_http_connection.get_bytes(
                image_url, timeout=VLLM_IMAGE_FETCH_TIMEOUT)
            image = _load_audio_from_bytes(image_raw)

        elif image_url.startswith('data:image'):
            _, image_base64 = image_url.split(",", 1)
            image = _load_audio_from_bytes(base64.b64decode(image_base64))
        else:
            raise ValueError("Invalid 'image_url': A valid 'image_url' must start "
                            "with either 'data:audio' or 'http'.")

        return image

    @wrapt.patch_function_wrapper(module, "async_fetch_image")
    async def _patched_async_fetch_image(wrapped, instance, args, kwargs):
        """
        Asynchronously load a PIL image from a HTTP or base64 data URL.

        By default, the image is converted into RGB format.
        """
        image_url, = args

        if image_url.startswith('http'):
            image_raw = await global_http_connection.async_get_bytes(
                image_url, timeout=VLLM_IMAGE_FETCH_TIMEOUT)
            image = _load_audio_from_bytes(image_raw)

        elif image_url.startswith('data:audio'):
            _, image_base64 = image_url.split(",", 1)
            image = _load_audio_from_bytes(base64.b64decode(image_base64))
        else:
            raise ValueError("Invalid 'image_url': A valid 'image_url' must start "
                            "with either 'data:audio' or 'http'.")

        return image

def _patch_chat_utils(module):
    @wrapt.patch_function_wrapper(module, "_image_token_str")
    def _patched_image_token_str(wrapped, instance, args, kwargs):
        return _PLACEHOLDER_TOKEN

    @wrapt.patch_function_wrapper(module, "_parse_chat_message_content_parts")
    def _patched_parse_chat_message_content_parts(wrapped, instance, args, kwargs):
        def _impl(
            role,
            parts,
            model_config,
            tokenizer
        ):
            parts = list(parts)
            image_url_indices = list(index for (index, part) in enumerate(parts) if part["type"] == "image_url")
            if len(image_url_indices) > 1:
                raise ValueError("Only one image_url is supported.")

            # Remove any placeholder from text parts and replace any pseudo-tokens with the placeholder.
            escaped_placeholder_token = _PLACEHOLDER_TOKEN.replace("|", "\\|")
            parts = list((part | { "text": part["text"].replace(_PLACEHOLDER_TOKEN, escaped_placeholder_token).replace(_PLACEHOLDER_PSEUDO_TOKEN, _PLACEHOLDER_TOKEN) } if part["type"] == "text" else part) for part in parts)

            placeholder_count = len(list(part for part in parts if part["type"] == "text" and _PLACEHOLDER_TOKEN in part["text"]))
            if placeholder_count > 0 and not image_url_indices:
                raise ValueError(f"Cannot specify {_PLACEHOLDER_PSEUDO_TOKEN} without an image_url.")
            elif placeholder_count > 1:
                raise ValueError(f"Only one {_PLACEHOLDER_PSEUDO_TOKEN} placeholder is supported.")
            
            if placeholder_count == 0 and image_url_indices:
                image_url_index = image_url_indices[0]
                if image_url_index == 0 or parts[image_url_index - 1]["type"] != "text":
                    # Insert the placeholder.
                    parts.insert(image_url_index, { "type": "text", "text": _PLACEHOLDER_TOKEN })
                else:
                    changed_part = parts[image_url_index - 1]
                    parts[image_url_index - 1] = changed_part | { "text": changed_part["text"] + _PLACEHOLDER_TOKEN }
                
            return wrapped(role, parts, model_config, tokenizer)
        
        return _impl(*args, **kwargs)

def patch_vllm():
    assert "vllm.multimodal.utils" not in sys.modules, "vllm.multimodal.utils has already been imported"
    wrapt.register_post_import_hook(_patch_multimodal_utils, "vllm.multimodal.utils")

    assert "vllm.entrypoints.chat_utils" not in sys.modules, "vllm.entrypoints.chat_utils has already been imported"
    wrapt.register_post_import_hook(_patch_chat_utils, "vllm.entrypoints.chat_utils")
    