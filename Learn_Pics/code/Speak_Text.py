from gtts import gTTS
import os

# Function to speak the word or text written
class Speak_text:
    def __init__(self, text, language="en"):
        self.text = text
        self.language = language


    def speak(self):
        tts = gTTS(self.text,
                   lang=self.language)
        tts.save("../sound/output.mp3")
        return os.system('ffplay -autoexit -nodisp ../sound/output.mp3')