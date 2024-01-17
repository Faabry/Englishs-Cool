import PySimpleGUI as sg
import code.Constant as c
from code.Greetings import Greeting

class Left:
    def __init__(self):
        self.greeting = Greeting()
        sg.theme(Greeting().get_theme())

        # Layout
        self.layout = [
            # Title
            [sg.Text("English's", font=("Arial Black", 40), text_color=self.greeting.get_title_color()[0]),
             sg.Text("Cool", font=("Arial Black", 40), text_color=self.greeting.get_title_color()[1])],

            [sg.Text()],

            # Greeting message with the day and datetime
            [sg.Text(self.greeting.greetings(),
                     font=(c.GREETING_FONT, 30), key="-GREETING-"
                     )],

            [sg.Text(self.greeting.get_day(),
                     font=(c.GREETING_FONT, 20))],

            [sg.Text(self.greeting.get_hour(),
                     font=(c.GREETING_FONT, 20), key="-HOUR-")],

            [sg.Text()]
        ]
    
    
    # Getting the layout
    def get_layout(self):
        return self.layout
        