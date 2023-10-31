from PIL import Image, ImageOps

objects = ["calculator", "chair"]

output_size = (1654, 1654)

for i in objects:
    item = i.lower()
    img = Image.open(f"images/{item}.jpeg")
    resized = ImageOps.fit(img, output_size, Image.Resampling.BILINEAR)

    resized.save(f"img_teste/{item}.jpeg")