import tkinter as tk
from PIL import Image, ImageTk
#import PIL
from googletrans import Translator
from VoiceRecognition import *


class App(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.text_input = ''
        self.voice_input = ''

        # create window
        self.root.title("GUI Translator")
        self.root.geometry("564x650")
        self.root.iconbitmap("christmas-tree.ico")

        # bg

        load = Image.open("bg.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self.root, image=render)
        img.place(x=0, y=0)

        name = tk.Label(self.root, text="TRANSLATOR", fg="#FFFFFF")
        name.config(font=("Arial", 30))
        name.pack(pady=10)

        self.box0 = tk.Text(self.root, width=28, height=8, font=("ROBOTO", 16))
        self.box1 = tk.Text(self.root, width=28, height=8, font=("ROBOTO", 16))
        self.box0.pack(pady=20)
        self.box1.pack(pady=120)

        button_frame = tk.Frame(self.root).pack(side=tk.BOTTOM)

        clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 10, 'bold'), bg="#303030", fg="#FFFFFF",
                              command=self.clear)
        clear_button.place(x=150, y=310)

        trans_button = tk.Button(button_frame, text="Translate", font=("Arial", 10, 'bold'), bg="#303030", fg="#FFFFFF",
                              command=self.translate)
        trans_button.place(x=290, y=310)

        #micro_button
        #audio_button

    def clear(self):
        self.box0.delete(1.0, tk.END)
        self.box1.delete(1.0, tk.END)

    def translate(self):
        inp = ''
        inp += self.box0.get(1.0, tk.END)
        if self.voice_input != '':
            inp = self.voice_input
        if self.text_input != '':
            inp = self.text_input

        t = Translator()
        translated = t.translate(inp, dest="vi")
        text = translated.text
        self.box1.insert(tk.END, text)

    def listen(self):
        voice = Voice()
        voice.recognize()
        self.voice_input = voice.content
        self.box0.insert(tk.END, voice.content)


root = tk.Tk()
translator = App(root)
translator.mainloop()
