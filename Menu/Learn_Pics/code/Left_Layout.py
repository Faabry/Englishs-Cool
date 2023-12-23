import PySimpleGUI as sg
import Learn_Pics.code.Const as c

class Left:

    def get_layout(self):
        return [
            [sg.Button("Foods", key="-FOOD-",
                      size=(c.FONT_SIZE),
                      font=(c.FONT_TYPE, 12)),
             sg.Button("Places", key="-PLACES-",
                      size=(c.FONT_SIZE),
                      font=(c.FONT_TYPE, 12))],

            [sg.Button("Drinks", key="-DRINKS-",
                      size=(c.FONT_SIZE),
                      font=(c.FONT_TYPE, 12)),
             sg.Button("Objects", key="-OBJECTS-",
                      size=(c.FONT_SIZE),
                      font=(c.FONT_TYPE, 12))],

            [sg.Image(key="-IMAGE-", size=(273, 274)), sg.Push()],
                        
            [sg.Text("", key="-TEXT-",
                    font=(c.FONT_TYPE, 25),
                    justification="right"),            
             sg.Button("🔊", font=("Arial", 15), size=(3, 1), key="-PLAY-", pad=(0, 0))],

            [sg.Button("Quit ❎", key="-QUIT-",
                    font=(c.FONT_TYPE, 15),
                    size=(21, 3))]
        ]