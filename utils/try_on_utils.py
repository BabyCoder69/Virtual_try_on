import os
import logging
from gradio_client import Client, handle_file

logger = logging.getLogger(__name__)


class VirtualTryOn:
    def __init__(self):
        self.client = Client("Nymbo/Virtual-Try-On")
        self.output_dir = "./output/"
        self.check_dir(_dir=self.output_dir)

    @staticmethod
    def check_dir(_dir):
        if not os.path.exists(_dir):
            os.makedirs(_dir)

    def infer_virtual_try_on(self, human_img, garment_img):
        human_image_name = os.path.splitext(os.path.basename(human_img))[0]

        result = self.client.predict(
            dict={"background": handle_file(human_img), "layers": [], "composite": None},
            garm_img=handle_file(garment_img),
            garment_des="Hello!!",
            is_checked=True,
            is_checked_crop=False,
            denoise_steps=30,
            seed=42,
            api_name="/tryon"
        )

        destination = self.output_dir + f"{human_image_name}_output.jpg"

        os.rename(result[0], destination)
        logger.info(f"Moved {result[0]} to {destination}")

        # Delete the second image
        os.remove(result[1])
        logger.info(f"Deleted {result[1]}")
