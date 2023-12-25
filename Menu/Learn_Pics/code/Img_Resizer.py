from PIL import Image, ImageOps
import Learn_Pics.code.Const as c

class Resizer:
    def __init__(self, element):
        self.element = element
        self.img_size = c.IMG_OUT


    def convert(self):
        item = self.element.lower()
        img = Image.open(f"Images/{item}.jpeg")

        # Convert the image to RGB mode
        img = img.convert("RGB")

        resized = ImageOps.fit(img,
                               self.img_size,
                               Image.Resampling.BILINEAR)

        resized.save(f"Images/{item}.jpeg")