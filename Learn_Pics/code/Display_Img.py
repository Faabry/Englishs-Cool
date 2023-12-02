# Display_Img.py
from PIL import Image, ImageTk
from Img_Resizer import Resizer
import Const as c

class ShowImg:
    def __init__(self, element, window):
        self.element = element
        self.window = window

    
    def display_image(self):
        img = Resizer(self.element)
        img.convert()
        # Directory of the image
        img_path = f"../images/{self.element}.jpeg"
        image = Image.open(img_path)

        # Define the size of the thumbnail for the image
        image.thumbnail(c.IMG_SIZE)

        # Insert the image into the thumbnail
        image_data = ImageTk.PhotoImage(image)

        # Display the name of the image
        text = self.element.title()

        # Update the image and the image's name on the screen
        self.window["-IMAGE-"].update(data=image_data)
        self.window["-TEXT-"].update(text)
