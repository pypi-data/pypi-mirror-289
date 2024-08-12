from io import BytesIO
from uuid import uuid4

from loguru import logger

from .MemeFactory import MemeFactory, MemeLib


class Generator:
    def __init__(self, output):
        self.path = output

    def generate(self, template: str, texts: list[str]):
        ext = MemeLib[template].image_file_path.split(".")[-1]

        output_path = f"{self.path}/{str(uuid4())}.{ext}"
        with open(output_path, "wb") as f:
            image_bytes = self.get_meme_image_bytes(template, texts)
            f.write(image_bytes.getbuffer())
            logger.info(f"Image saved to {output_path}")

    def get_meme_image_bytes(self, template, args):
        image_bytes = BytesIO()
        meme_img = MemeFactory.factory_from_template(template, args).output_image
        if hasattr(meme_img, "is_animated") and meme_img.is_animated:
            frames = []
            for i in range(0, meme_img.n_frames):
                meme_img.seek(i)
                frames.append(meme_img.copy())
            frames[0].save(image_bytes, format="GIF", save_all=True, append_images=frames[1:], duration=meme_img.info['duration'], loop=0)
        else:
            meme_img.save(image_bytes, format="PNG")
        image_bytes.seek(0)
        return image_bytes

if __name__=="__main__":
    g = Generator(".")
    g.generate("Classy", ["Hello", "World"])