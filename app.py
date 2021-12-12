import tkinter as tk
from PIL import Image, ImageTk
from googletrans import Translator
from Voice import *
from Flashcard import *
import openpyxl


class App:
    """An app translating to Vietnamese using both text, and voice,
     add vocab to an Excel file """
    def __init__(self, root):
        self.root = root
        self.voice_input = ''
        self.input = ''
        self.output = ''

        # create window
        self.root.title("GUI Translator")
        self.root.geometry("564x650")
        self.root.iconbitmap("christmas-tree.ico")

        # bg
        load = Image.open("bg3.jpg")
        self.render = ImageTk.PhotoImage(load)
        self.img = tk.Label(self.root, image=self.render)
        self.img.place(x=0, y=0)
        # the name: Translator
        name = tk.Label(self.root, text="TRANSLATOR", fg="#303030", bg="#F9F7E8")
        name.config(font=("Arial", 30))
        name.pack(pady=10)
        # Text boxes
        self.box0 = tk.Text(self.root, width=28, height=6, font=("ROBOTO", 16))
        self.box1 = tk.Text(self.root, width=28, height=6, font=("ROBOTO", 16))
        self.box0.pack(pady=20)
        self.box1.pack(pady=120)
        # Buttons
        button_frame = tk.Frame(self.root).pack(side=tk.BOTTOM)
        clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 10, 'bold'), bg="#303030", fg="#FFFFFF",
                                 command=self.clear)
        clear_button.place(x=150, y=310)

        trans_button = tk.Button(button_frame, text="Translate", font=("Arial", 10, 'bold'), bg="#303030", fg="#FFFFFF",
                                 command=self.translate)
        trans_button.place(x=240, y=310)

        add_button = tk.Button(button_frame, text="Add to Excel", font=("Arial", 10, 'bold'), bg="#303030",
                               fg="#FFFFFF", command=self.add_excel)
        add_button.place(x=350, y=310)

        play_button = tk.Button(button_frame, text="Play with Words", font=("Arial", 15, 'bold'), bg="#303030",
                                fg="#FFFFFF", command=self.new_window)
        play_button.place(x=205, y=550)

        mic = tk.PhotoImage(file='mic1.png')
        mic_img = tk.Label(image=mic)
        mic_img.image = mic
        micro_button = tk.Button(button_frame, image=mic, command=self.listen, borderwidth=0)
        micro_button.place(x=80, y=100)

        audio = tk.PhotoImage(file='audio1.png')
        audio_img = tk.Label(image=audio)
        audio_img.image = audio
        audio_button = tk.Button(button_frame, image=audio, command=self.speak, borderwidth=0)
        audio_button.place(x=80, y=130)

    def start_loop(self):
        self.root.mainloop()

    def new_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Flashcard")
        new_window.geometry("600x350")
        flashcard = Play()
        word = tk.Label(new_window, text=flashcard.word)
        word.config(font=("Arial", 25))
        word.pack(pady=50)

        def show_meaning():
            meaning = tk.Label(new_window, text=flashcard.meaning)
            meaning.config(font=("Arial", 25))
            meaning.pack(pady=60)

        answer_button = tk.Button(new_window, text="Show", font=("Arial", 15, 'bold'), bg="#303030",
                               fg="#FFFFFF", command=show_meaning)
        answer_button.pack()

    def clear(self):
        self.input = ''
        self.output = ''
        self.box0.delete(1.0, tk.END)
        self.box1.delete(1.0, tk.END)

    def translate(self):
        if self.voice_input != '':
            self.input = self.voice_input
        self.input = self.box0.get(1.0, tk.END)

        t = Translator()
        translated = t.translate(self.input, dest="vi")
        text = translated.text
        self.output = text
        self.box1.insert(tk.END, text)

    def listen(self):
        voice = Voice()
        voice.recognize()
        self.voice_input = voice.content
        self.box0.insert(tk.END, voice.content)

    def speak(self):
        speech = Voice()
        speech.convert_to_speech(self.input)

    def add_excel(self):
        wb = openpyxl.load_workbook('vocab.xlsx')
        sheet = wb['Sheet1']
        sheet.append([self.input, self.output])
        wb.save('vocab.xlsx')


window = tk.Tk()
translator = App(window)
translator.start_loop()
