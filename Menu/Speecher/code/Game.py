import PySimpleGUI as sg
import speech_recognition as sr
import Speecher.code.Constant as c
from random import choice
from Speecher.code.Result import Speak_text
from time import sleep


class Pronoucer:
    def __init__(self):
        # Theme
        sg.theme("lightblue")

        self.recognizer = sr.Recognizer()
        self.user_input = None

        # self.client = speech.SpeechClient.from_service_account_file('path/to/your/credentials.json')

        # Layout of application
        self.layout = [

        # ---------------------Header ---------------------
            # Title
            [sg.Text("Talkit",
                     font=("Arial Black", 40),
                     text_color=("black")),

            sg.Text("Right",
                    font=("Arial Black", 40),
                    text_color=("red")),
            
            sg.Push(),

            # Logo
            sg.Image(r"images/logo1.png")],
        # -------------------------------------------------

            # Starts blank
            [sg.Text(font=("Bookman Old Style", 20),
                           text_color=("black"),
                           key="-TEXT-",
                           size=(26, 3))],

            # Starts blank
            [sg.Text(font=("Bookman Old Style", 20),
                           text_color=("black"),
                           key="-TEXT1-",
                           size=(26, 9))],

            # ---------------- Buttons -----------------
            [sg.Push(),
             sg.Button("Check Pronunciation",
                        font=("Comic Sans MS", 12),
                        size=(48, 2)),
            sg.Push()],

            [sg.Push(),
            sg.Button("Quit ❎",
                       font=("Comic Sans MS", 12),
                       size=(48, 3), key="-QUIT-"),
            sg.Push()],
            # --------------------------------------------

            # Adjust the space between the last element and the end of the window
            [sg.Text()]
        ]

        # Creating the Window to implement the layout
        self.window = sg.Window("Speecher",
                                self.layout,
                                location=(350, 10))
    

    # Run method
    def run(self):
        # Checking events
        while True:
            event, values = self.window.read(timeout=10)

            if event == sg.WINDOW_CLOSED or event == '-QUIT-':
                break

            elif event == 'Check Pronunciation':
                # Randomly choose the sentence to be said
                self.word = choice(c.TEXTS)

                # Update the window with the sentence
                self.window["-TEXT-"].update(f"Say: {self.word}", 
                                             text_color="black")  
                self.window["-TEXT1-"].update("")  

                # I needed to create a popup to allow the window to be updated, without this popup the text won't be displayed, the popup's location is out of the window border
                sg.popup_quick_message(f"Say: {self.word}",
                                       auto_close=True,
                                       font="Bookman 1",
                                       location=(-100, 0))
                
                # Recognizing the User's voice
                with sr.Microphone() as source:
                    try:
                        audio = self.recognizer.listen(source,
                                                       timeout=30)
                        self.user_input = self.recognizer.recognize_google(audio).strip()
                        # audio = self.recognizer.listen(source, timeout=20)
                        # user_input = self.transcribe_audio(audio)
                    
                    except sr.UnknownValueError:
                        sg.popup_quick_message('Speech not recognized. Please try again.')

                    except sr.WaitTimeoutError:
                        sg.popup_quick_message("Time Out!")

                if self.user_input:
                    # Evaluate pronunciation
                    result = self.evaluate_pronunciation(self.user_input, self.word)
                    result1 = Speak_text()

                    # Provide feedback
                    if result:
                        self.window["-TEXT-"].update("Checking your answer...")
                        sg.popup_quick_message(f"Say: {self.word}",
                                               auto_close=True, font="Bookman 1", location=(-100, 0))
                        sleep(1)

                        self.window['-TEXT-'].update(f'Correct Pronunciation! {choice(c.HAPPY_EMOJIS)}', text_color="green")

                        # Correct Voice
                        result1.correct()

                    else:
                        self.window["-TEXT-"].update("Checking your answer...")
                        sg.popup_quick_message(f"Say: {self.word}",
                                               auto_close=True, font="Bookman 1", location=(-100, 0))
                        sleep(1)

                        self.window['-TEXT-'].update(f'Incorrect pronunciation. {choice(c.SAD_EMOJIS)}', text_color="red")

                        self.window['-TEXT1-'].update(f'It should be: {self.word}\n\n\nYou said: {self.user_input}')

                        # Incorrect Voice
                        result1.incorrect()

                else:
                    pass
        
        # Close the window
        self.window.close()


    # Evaluating the User's pronunciation with the sentence defined
    def evaluate_pronunciation(self,
                               user_input,
                               correct_pronunciation):
        # Basic evaluation logic
        return user_input.lower() == correct_pronunciation.lower()
    

    def transcribe_audio(self, audio_data):
        config = speech.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
        )

        audio = speech.RecognitionAudio(content=audio_data.frame_data)

        response = self.client.recognize(config=config, audio=audio)

        return response.results[0].alternatives[0].transcript.lower()