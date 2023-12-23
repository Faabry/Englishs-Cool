import PySimpleGUI as sg
from code.Left_Layout import Left
from code.Right_Layout import Right
from Learn_Pics.code.Layout import Screen as Learn_Screen
from Translator.code.game import Translator
from Speecher.code.Game import Pronoucer


class Screen:
    def __init__(self):
        # Definindo o tema da interface
        sg.theme('Lightblue')
        
        left_layout = Left().get_layout()
        right_layout = Right().get_layout()

        self.layout = [
            [sg.Column(left_layout),
             sg.Column(right_layout, element_justification="up")],

            [sg.Text("Let's", font=("Arial Black", 30)),
             sg.Text("Learn?", font=("Arial Black", 30), text_color=("red"))],

            [sg.Button("Learn Pics", key="-LEARN_PICS-", size=(27, 2), font=("Comic Sans MS", 14)),
             sg.Push(),
             sg.Button("Translator", key="-TRANSLATOR-", size=(27, 2), font=("Comic Sans MS", 14))],

            [sg.Button("Speecher", key="-SPEECHER-", size=(27, 2), font=("Comic Sans MS", 14)),
             sg.Push()],
            
            [sg.Button("Quit ❎", key="-QUIT-", size=(80, 3), font=("Comic Sans MS", 14))]
        ]

        self.window = sg.Window("English's Cool Game",
                                self.layout, 
                                element_padding=(10, 10),
                                location=(250, 0),
                                size=(680, 800))
        
    # Checking events
    def run(self):
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED or event == "-QUIT-":
                break

            elif event == "-LEARN_PICS-":
                pics = Learn_Screen()
                pics.run()
            elif event == "-TRANSLATOR-":
                translator = Translator()
                translator.run()
            elif event == "-SPEECHER-":
                speecher = Pronoucer()
                speecher.run()

        # End
        self.window.close()

if __name__ == "__main__":
    teste = Screen()
    teste.run()