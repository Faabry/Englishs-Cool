# Display_Img.py
from PIL import Image, ImageTk
from Learn_Pics.code.Img_Resizer import Resizer
import Learn_Pics.code.Const as c

class ShowImg:
    def __init__(self, element, window):
        self.element = element
        self.window = window

    
    def display_image(self):
        img = Resizer(self.element)
        img.convert()
        # Directory of the image
        img_path = f"Images/{self.element}.jpeg"
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
