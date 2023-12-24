import PySimpleGUI as sg
from translated import translated
from translate_text import Translate_text as tt
from speak_text import Speak_text as st


class Translator:
    def __init__(self):
        # Theme
        sg.theme("lightblue")

        # Layout of application
        self.layout = [
            # Title
            [sg.Text("Trans", font=("Bookman 40 bold"), text_color=("black")),
            sg.Text("lator", font=("Bookman 40 bold"), text_color=("red")),
            sg.Push(),
            sg.Image(r"../images/logo1.png")],

            [sg.Text()],

            [sg.Text("Word | Text:",
                    font=("Bookman Old Style", 25))],

            [sg.Multiline(key="input_text",
                        size=(40, 8),
                        font=("Bookman Old Style", 15))],

            [sg.Text()],

            [sg.Text("Type of Translation:",
                    font=("Bookman Old Style", 25))],

            [sg.Push(),
            sg.Radio("Portuguese » English",
                    "translation",
                    key="pt_to_en",
                    default=True,
                    font=("Bookman Old Style", 12, "bold"),
                    text_color=("#5079d3")),
            sg.Push(),
            sg.Radio("English » Portuguese",
                    "translation",
                    key="en_to_pt",
                    font=("Bookman Old Style", 12, "bold"),
                    text_color=("#5079d3")),
            sg.Push()],

            [sg.Text()],

            [sg.Push(),
            sg.Button("Translate",
                        font=("Bookman Old Style", 12),
                        size=(48, 2)),
            sg.Push()],

            [sg.Push(),
            sg.Button("Speak 🔉",
                        font=("Bookman Old Style", 12),
                        size=(48, 2)),
            sg.Push()],

            [sg.Text()],

            [sg.Push(),
            sg.Button("Quit ❎",
                        font=("Bookman Old Style", 12),
                        size=(48, 3)),
            sg.Push()],

            [sg.Text()]
        ]

        # Creating the window with the layout I've defined
        self.window = sg.Window("Text Translator",
                        self.layout,
                        location=(350, 10))

    def run(self):
        # Checking events
        while True:
            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED or event == "Quit ❎":
                break

            input_text = values["input_text"]
            source_language = "pt" if values["pt_to_en"] else "en"
            target_language = "en" if values["pt_to_en"] else "pt"

            if event == "Translate":
                translated_text = tt(input_text,
                                     source_language,
                                     target_language)
                
                translated(translated_text.translate())

            elif event == "Speak 🔉":
                speak = st(input_text, source_language)
                speak.speak()

        self.window.close()
    