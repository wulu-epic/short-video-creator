from gtts import gTTS 

class Voice(object):
    def __init__(self, language='en'):
        self.voice_history = []
        self.language = language 
    
    def say(self, text : str, save='sample.mp3') -> gTTS:  
        gtts_audio = gTTS(text=text, lang=self.language, slow=False)  
        gtts_audio.save(save) 

        return gtts_audio
    
    def get_history(self) -> list:
        return self.voice_history