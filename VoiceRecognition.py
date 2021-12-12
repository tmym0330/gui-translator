#from google_trans_new import google_translator
from googletrans import Translator
import speech_recognition as sr
import pyttsx3


class Voice:
    """Rec and Speak the words"""
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.content = ''

    def recognize(self):
        with sr.Microphone() as source:
            print("Clearing the noises...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Hear")
            audio = self.recognizer.listen(source, timeout=1)
            print("done")
        try:
            print("rec")
            result = self.recognizer.recognize_google(audio, language="en")
            print(result)
            self.content = result
        except Exception as ex:
            print(ex)

    def speak(self, translate_text):
        print(translate_text)
        self.engine.say(translate_text)
        self.engine.runAndWait()


