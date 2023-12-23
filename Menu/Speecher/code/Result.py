from gtts import gTTS
import os
import Speecher.code.Constant as c
from random import choice

class Speak_text:
    def __init__(self, language="en"):
        self.language = language


    # Correct voice message
    def correct(self):
        # Randomly choose the message to be said
        text = choice(c.CORRECT)

        # Renderezing the text
        tts = gTTS(text,
                   lang=self.language)
        tts.save("Sound/output.mp3")

        # Saying the message
        return os.system('ffplay -autoexit -nodisp Sound/output.mp3')
        

    # Incorrect voice message
    def incorrect(self):
        # Randomly choose the message to be said
        text = choice(c.INCORRECT)

        # Rendering the message
        tts = gTTS(text,
                   lang=self.language)
        tts.save("Sound/output.mp3")

        # Saying the message
        return os.system('ffplay -autoexit -nodisp Sound/output.mp3')
        

