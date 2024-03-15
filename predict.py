from cog import BasePredictor, Input, Path

from PIL import Image
from transformers import UdopProcessor, UdopForConditionalGeneration
import time
import os
import subprocess

UDOP_URL = "https://weights.replicate.delivery/default/udop/udop-large-cache.tar"


def download_weights(url, dest):
    start = time.time()
    print("downloading from: ", url)
    subprocess.check_call(["pget", "-x", url, dest])
    print("downloading took: ", time.time() - start)


class Predictor(BasePredictor):
    def setup(self) -> None:
        if not os.path.exists("udop-large"):
            download_weights(UDOP_URL, "udop-large")
        self.processor = UdopProcessor.from_pretrained("udop-large")
        self.model = UdopForConditionalGeneration.from_pretrained("udop-large")

    def predict(
        self,
        image: Path = Input(description="Input image"),
        prompt: str = Input(description="Prompt to describe the task", default=None),
    ) -> str:

        image = Image.open(image).convert("RGB")

        encoding = self.processor(images=image, text=prompt, return_tensors="pt")

        outputs = self.model.generate(**encoding)
        generated_text = self.processor.batch_decode(outputs, skip_special_tokens=True)[
            0
        ]

        return generated_text
