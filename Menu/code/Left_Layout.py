import PySimpleGUI as sg
import code.Constant as c
from code.Greetings import Greeting

class Left:

    def get_layout(self):
        self.greeting = Greeting()

        return [
            [sg.Text("English's", font=("Arial Black", 40), text_color="black"),
             sg.Text("Cool", font=("Arial Black", 40), text_color="red")],

            [sg.Text()],

            [sg.Text(self.greeting.greetings(),
                     font=(c.GREETING_FONT, 30),
                     text_color=c.GREETING_COLOR)],
            [sg.Text(self.greeting.get_day(),
                     font=(c.GREETING_FONT, 20),
                     text_color=c.GREETING_COLOR)],
            [sg.Text(self.greeting.get_hour(),
                     font=(c.GREETING_FONT, 20),
                     text_color=c.GREETING_COLOR)],

            [sg.Text()]
        ]