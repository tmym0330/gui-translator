import speech_recognition as sr
import pyttsx3


class Voice:
    """Recognize and Speak the words"""
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.content = ''

    def recognize(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Hear")
            audio = self.recognizer.listen(source, timeout=4)
        try:
            print("rec")
            result = self.recognizer.recognize_google(audio, language="en")
            print(result)
            self.content = result
        except Exception as ex:
            print(ex)

    def convert_to_speech(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


