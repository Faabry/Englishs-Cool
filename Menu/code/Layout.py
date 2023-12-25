import PySimpleGUI as sg
from code.Left_Layout import Left
from code.Right_Layout import Right
from Learn_Pics.code.Layout import Screen as Learn_Screen
from Translator.code.game import Translator
from Speecher.code.Game import Pronoucer
from code.Greetings import Greeting
from datetime import datetime as dt


class Screen:
    def __init__(self):
        # Defining the layout theme
        sg.theme(Greeting().get_theme())
        
        # Instanciating the classes
        self.left_layout = Left()
        self.right_layout = Right().get_layout()
        self.greeting = Greeting()

        # Mainly layout
        self.layout = [
            [sg.Column(self.left_layout.get_layout(), key="-HOUR-"),
             sg.Column(self.right_layout, element_justification="up")],

            [sg.Text("Let's", font=("Arial Black", 30), text_color="black"),
             sg.Text("Learn?", font=("Arial Black", 30), text_color=("red"))],

            # ---------------------- Buttons ------------------------
            [sg.Button("Learn Pics", key="-LEARN_PICS-", size=(27, 2), font=("Comic Sans MS", 14)),
             
             sg.Push(),

             sg.Button("Translator", key="-TRANSLATOR-", size=(27, 2), font=("Comic Sans MS", 14))],

            [sg.Button("Speecher", key="-SPEECHER-", size=(27, 2), font=("Comic Sans MS", 14)),
             sg.Push()],
            
            [sg.Button("Quit ❎", key="-QUIT-", size=(80, 3), font=("Comic Sans MS", 14))]
            # -------------------------------------------------------
        ]

        # Creating the window
        self.window = sg.Window("English's Cool Game",
                                self.layout, 
                                element_padding=(10, 10),
                                location=(250, 0),
                                size=(680, 800))
        
    # Checking events
    def run(self):
        while True:
            event, values = self.window.read(timeout=100)
            
            # Update the time every 100ms
            self.window["-HOUR-"].update(self.greeting.get_hour())
            
            # Quit the application
            if event == sg.WINDOW_CLOSED or event == "-QUIT-":
                break

            # Start Learn Pics
            elif event == "-LEARN_PICS-":
                pics = Learn_Screen()
                pics.run()
        
            # Start Translator
            elif event == "-TRANSLATOR-":
                translator = Translator()
                translator.run()

            # Start Speecher
            elif event == "-SPEECHER-":
                speecher = Pronoucer()
                speecher.run()

        # End
        self.window.close()
