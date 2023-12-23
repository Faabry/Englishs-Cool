import PySimpleGUI as sg
import Learn_Pics.code.Const as c
from Learn_Pics.code.Choose_img import Random_Img
from Learn_Pics.code.Display_Img import ShowImg
from Learn_Pics.code.Speak_Text import Speak_text
from Learn_Pics.code.Left_Layout import Left
from Learn_Pics.code.Right_Layout import Right


class Screen:
    def __init__(self):
        # Definindo o tema da interface
        sg.theme('Lightblue')
        self.left = Left().get_layout()
        self.right = Right().get_layout()


        # Layout da interface
        self.layout = [
            [sg.Text("Learn",
                     font=(c.FONT_TITLE, 40), 
                     text_color="black"),
            sg.Text("Pics", 
                    font=(c.FONT_TITLE, 40),
                    text_color="red")],

            [sg.Text("Choose a category:", font=(c.FONT_TYPE, 25))],
            
            [sg.Column(self.left, justification="left"),
             sg.Column(self.right, justification="right")]
        ]

        # Creating the window
        self.window = sg.Window("Learn Pics Game",
                                self.layout, 
                                element_padding=(10, 10),
                                location=(250, 0),
                                size=(650, 800))
        
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