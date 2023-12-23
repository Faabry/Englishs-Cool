import PySimpleGUI as sg
import pyperclip as pc

def translated(translated_text):
    # Layout of the window
    translate_layout = [
                [sg.Multiline(default_text=translated_text,
                              size=(25, 10), key="translated_text", font=("Bookman Old Style", 15))],

                [sg.Text()],

                # Button to copy the content
                [sg.Button("Copy to Clipboard",
                           font=("Bookman Old Style", 12),
                           size=(31, 2),
                           key="-CLIPBOARD-")]
            ]

    # Creating the window
    translate_window = sg.Window("Translator",
                                 translate_layout,
                                 modal=True)

    while True:
        event_translate, values_translate = translate_window.read()
        
        if event_translate == sg.WINDOW_CLOSED:
            break

        if event_translate == "-CLIPBOARD-":
            pc.copy(values_translate["translated_text"])
            sg.Popup("Texto copiado!",
                     font=("Bookman Old Style", 10),
                     text_color=("#5079d3"))
            translate_window.close()
    