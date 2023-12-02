from PIL import Image, ImageOps
import Const as c

class Resizer:
    def __init__(self, element):
        self.element = element
        self.img_size = c.IMG_OUT


    def convert(self):
        item = self.element.lower()
        img = Image.open(f"../images/{item}.jpeg")
        resized = ImageOps.fit(img,
                               self.img_size,
                               Image.Resampling.BILINEAR)

        resized.save(f"../images/{item}.jpeg")