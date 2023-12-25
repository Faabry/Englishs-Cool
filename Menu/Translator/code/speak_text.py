from gtts import gTTS
import requests
import os

# Function to speak the word or text written
class Speak_text:
    def __init__(self, text, language):
        self.text = text
        self.language = language


    def speak(self):
        tts = gTTS(self.text,
                   lang=self.language)
        # os.system("mkdir Sound")
        tts.save(r"Sound/output.mp3")
        return os.system('ffplay -autoexit -nodisp Sound/output.mp3')
        

    # def speak(self):
    #     url = "https://voicerss-text-to-speech.p.rapidapi.com/"
    #     querystring = {"key":"a310dd653b9c4740bd1359361f881074"}

    #     payload = {
    #         "src": self.text,
    #         "hl": self.language,
    #         "r": "0",
    #         "c": "mp3",
    #         "f": "8khz_8bit_mono"
    #     }

    #     headers = {
    #         "content-type": "application/x-www-form-urlencoded",
    #         "X-RapidAPI-Key": "eb398b1c3emsh43bd73881cb151ap15c148jsne2785acdd1bb",
    #         "X-RapidAPI-Host": "voicerss-text-to-speech.p.rapidapi.com"
    #     }
    #     response = requests.post(url, data=payload, headers=headers, params=querystring)  

    #     # Save the audio content to an MP3 file
    #     response.save(r"Sound/output.mp3")
  
        
    #     return os.system(f'ffplay -autoexit -nodisp Sound/output.mp3')
