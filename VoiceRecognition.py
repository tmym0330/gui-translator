#from google_trans_new import google_translator
from googletrans import Translator
import speech_recognition as sr
import pyttsx3



recognizer = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    print("Clearing the noises...")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("2")
    audio = recognizer.listen(source, timeout=1)
    print("done")
try:
    print("rec")
    result = recognizer.recognize_google(audio, language="en")
    print(result)
except Exception as ex:
    print(ex)

# Trans
engine.say("ready")
engine.runAndWait()

def trans():
    lan_inp = input("Input lang: ")
    translator = Translator()
    translate_text = translator.translate(str(result), dest=lan_inp)
    #bug??   File "C:\Users\Our Fam\anaconda3\lib\json\decoder.py", line 340, in decode
    #raise JSONDecodeError("Extra data", s, end)
    #json.decoder.JSONDecodeError: Extra data: line 1 column 584 (char 583)
    print(translate_text.text)
    engine.say(str(translate_text.text))
    engine.runAndWait()


trans()