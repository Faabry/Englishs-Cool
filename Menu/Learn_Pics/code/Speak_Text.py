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
        tts.save("Sound/output.mp3")
        return os.system('ffplay -autoexit -nodisp Sound/output.mp3')

# import os
# import pyttsx3


# class Speak_text:
#     def __init__(self, text, language="en"):
#         self.text = text
#         self.language = language

#     def speak(self):
#         engine = pyttsx3.init()
#         # Setting the speed speach
#         engine.setProperty('rate', 150)
#         voices = engine.getProperty("voices")
#         engine.setProperty("voice", voices[1].id)
#         engine.runAndWait()
#         engine.save_to_file(self.text, "../sound/output.wav")
#         engine.runAndWait()
#         return os.system('ffplay -autoexit -nodisp ../sound/output.wav')
