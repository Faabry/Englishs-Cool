import PySimpleGUI as sg
import Learn_Pics.code.Const as c
from code.Right_Layout import Right as r

class Right:

    def get_layout(self):
        return [
            [sg.Button("Animals", key="-ANIMALS-",
                      size=(c.FONT_SIZE),
                      font=(c.FONT_TYPE, 12)),
            sg.Button("Fruits", key="-FRUITS-",
                      size=(c.FONT_SIZE),
                      font=(c.FONT_TYPE, 12))],

            [sg.Button("Clothes", key="-CLOTHES-",
                      size=(c.FONT_SIZE),
                      font=(c.FONT_TYPE, 12)),
            sg.Button("Verbs", key="-VERBS-",
                      size=(c.FONT_SIZE),
                      font=(c.FONT_TYPE, 12))],

            [sg.Push(),
             sg.Text("Make a\nSentence\nWith...",
                    font=(c.FONT_TYPE2, 32),
                    justification="center"), 
            sg.Push()],
            [sg.Text("", font=("Arial", 60))],
            [sg.Push(),
             sg.Image(r().get_logo()), sg.Push()]
            ]