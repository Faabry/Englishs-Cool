import PySimpleGUI as sg
import Const as c
from Choose_img import Random_Img
from Display_Img import ShowImg
from Speak_Text import Speak_text


class Screen:
    def __init__(self):
        # Definindo o tema da interface
        sg.theme('Lightblue')

        # Layout da interface
        self.layout = [
            [sg.Text("Learn", font=(c.FONT_TITLE), text_color="black"),
            sg.Text("Pics", font=(c.FONT_TITLE),text_color="red")],

            [sg.Text("Choose a category:", font=(c.FONT_TYPE, 25))],
            
            [sg.Button("Foods", key="-FOOD-",
                      size=(c.FONT_SIZE),
                      font=(c.FONT_TYPE, 12)),
            sg.Button("Places", key="-PLACES-",
                      size=(c.FONT_SIZE),
                      font=(c.FONT_TYPE, 12)),
            sg.Button("Animals", key="-ANIMALS-",
                      size=(c.FONT_SIZE),
                      font=(c.FONT_TYPE, 12)),
            sg.Button("Fruits", key="-FRUITS-",
                      size=(c.FONT_SIZE),
                      font=(c.FONT_TYPE, 12))],
            
            [sg.Button("Drinks", key="-DRINKS-",
                      size=(c.FONT_SIZE),
                      font=(c.FONT_TYPE, 12)),
            sg.Button("Objects", key="-OBJECTS-",
                      size=(c.FONT_SIZE),
                      font=(c.FONT_TYPE, 12)),
            sg.Button("Verbs", key="-VERBS-",
                      size=(c.FONT_SIZE),
                      font=(c.FONT_TYPE, 12)),
            sg.Button("Random", key="-RANDOM-",
                      size=(c.FONT_SIZE),
                      font=(c.FONT_TYPE, 12))],

            [sg.Image(key="-IMAGE-", size=(273, 274)),
            sg.Push(),
            sg.Text("Make a\nsentence\nwith...",
                    font=(c.FONT_TYPE, 35),
                    justification="center"), 
            sg.Push()],

            
            [sg.Text("", key="-TEXT-",
                    font=(c.FONT_TYPE, 25),
                    justification="right"),
            
            sg.Button("🔊", font=("Arial", 15), size=(3, 1), key="-PLAY-", pad=(0, 0))],

            [sg.Button("Quit ❎", key="-QUIT-",
                    font=(c.FONT_TYPE, 15),
                    size=(21, 3)),
            sg.Push(),
            sg.Image("../images/logo1.png")]
        ]

        # Creating the window
        self.window = sg.Window("English's Cool Game",
                                self.layout, 
                                element_padding=(10, 10),
                                location=(250, 0),
                                size=(600, 800))
        
    # Checking events
    def run(self):
        while True:
            # Getting the category dict
            event_category_mapping = c.EVENT_CATERORIES

            # Getting randomly the image
            self.random_img = Random_Img(c.ELEMENTS)

            event, values = self.window.read()

            if event == sg.WINDOW_CLOSED or event == "-QUIT-":
                break

            # Getting the caterory's name based on the user's choice
            category = event_category_mapping.get(event)
            if category:
                # Choose randomly the image based on the category
                element = self.random_img.sort_img(category)

                # Display the image
                image = ShowImg(element, self.window)
                image.display_image()

            if event == "-PLAY-":
                try:
                    word = Speak_text(element)
                    word.speak()
                except:
                    self.window["-TEXT-"].Update("No word")

        # End
        self.window.close()