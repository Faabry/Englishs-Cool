import PySimpleGUI as sg
from code.Greetings import Greeting
from Learn_Pics.code.Img_Resizer import Resizer

class Right:

    def get_layout(self):
        return [
            [sg.Image(self.get_logo())],
            [sg.Text("", font=("Arial", 150))]
        ]
    

    def get_logo(self):
        greeting = Greeting()
        self.hour = greeting.date.hour

        if 6 <= self.hour < 12:
            logo_path = "Images/logo1.png"
        elif 12 <= self.hour < 18:
            logo_path = "Images/logo2.png"
        else:
            logo_path = "Images/logo3.png"

        return logo_path


        