import PySimpleGUI as sg

class Right:

    def get_layout(self):
        return [
            [sg.Image("Images/logo1.png")],
            [sg.Text("", font=("Arial", 120))]
        ]