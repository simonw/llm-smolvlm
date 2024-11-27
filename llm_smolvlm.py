from transformers import AutoProcessor, AutoModelForVision2Seq
import torch
from typing import Tuple
from transformers.image_utils import load_image
import llm
from llm import models

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


@llm.hookimpl
def register_models(register):
    register(SmolVlm())


class SmolVlm(models.Model):
    model_id = "smolvlm"
    can_stream = False
    attachment_types = {
        "image/jpeg",
        "image/png",
        "image/gif",
    }

    def _load(self) -> Tuple[AutoProcessor, AutoModelForVision2Seq]:
        if not hasattr(self, "_loaded"):
            self._loaded = (
                AutoProcessor.from_pretrained("HuggingFaceTB/SmolVLM-Instruct"),
                AutoModelForVision2Seq.from_pretrained(
                    "HuggingFaceTB/SmolVLM-Instruct",
                    torch_dtype=torch.bfloat16,
                    _attn_implementation=(
                        "flash_attention_2" if DEVICE == "cuda" else "eager"
                    ),
                ).to(DEVICE),
            )
        return self._loaded

    def execute(self, prompt, stream, response, conversation):
        messages = [
            {
                "role": "user",
                "content": [{"type": "image"} for _ in prompt.attachments]
                + [{"type": "text", "text": prompt.prompt}],
            }
        ]
        processor, model = self._load()
        inputs = processor(
            text=processor.apply_chat_template(messages, add_generation_prompt=True),
            images=[load_image(attachment.url) for attachment in prompt.attachments],
            return_tensors="pt",
        ).to(DEVICE)
        generated_ids = model.generate(**inputs, max_new_tokens=500)
        generated_texts = processor.batch_decode(
            generated_ids, skip_special_tokens=True
        )
        yield generated_texts[0]
