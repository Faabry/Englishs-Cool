from deep_translator import GoogleTranslator

# Function to translate any text
class Translate_text:
    def __init__(self, text, source_language, target_language):
        self.text = text
        self.source_lang = source_language
        self.target_lang = target_language


    def translate(self):
        translation = GoogleTranslator(source=self.source_lang,
                                       target=self.target_lang). \
                                       translate(self.text)
        return translation



        
