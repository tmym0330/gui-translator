from tkinter import *
from PIL import Image, ImageTk
from googletrans import Translator
from VoiceRecognition import *


class Translator(Frame):

    def __init__(self, master):
        self.text_input = ''
        self.voice_input = ''
        self.output = ''
        self.root = Tk()


    def window(self):
        # create window
        self.root.title("GUI Translator")
        self.root.geometry("564x650")
        self.root.iconbitmap("christmas-tree.ico")

        # bg
        load = Image.open("bg.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self.root, image=render)
        img.place(x=0, y=0)

        name = Label(self.root, text="TRANSLATOR", fg="#FFFFFF")
        name.config(font=("Arial", 30))
        name.pack(pady=10)

        self.box0 = Text(self.root, width=28, height=8, font=("ROBOTO", 16))
        self.box1 = Text(self.root, width=28, height=8, font=("ROBOTO", 16))
        self.box0.pack(pady=20)
        self.box1.pack(pady=120)

        button_frame = Frame(self.root).pack(side=BOTTOM)

        clear_button = Button(button_frame, text="Clear", font=("Arial", 10, 'bold'), bg="#303030", fg="#FFFFFF",
                              command=self.clear)
        clear_button.place(x=150, y=310)
        trans_button = Button(button_frame, text="Translate", font=("Arial", 10, 'bold'), bg="#303030", fg="#FFFFFF",
                              command=self.translate)
        trans_button.place(x=290, y=310)

    def clear(self):
        self.box0.delete(1.0, END)
        self.box1.delete(1.0, END)

    def translate(self):
        inp = ''
        inp += self.box0.get(1.0, END)
        if self.voice_input != '':
            inp = self.voice_input
        if self.text_input != '':
            inp = self.text_input

        t = Translator()
        translated = t.translate(inp, dest="en")
        text = translated.text
        self.box1.insert(END, text)

    def insert_input(self):
        inp = self.box0.get(1.0, END)
        #print(inp)

    def listen(self):
        voice = Voice()
        voice.recognize()
        self.voice_input = voice.content
        self.box0.insert(END, voice.content)


root = Tk()
translator = Translator(root)
translator.mainloop()
