import tkinter as tk
from PIL import Image, ImageTk
# import PIL
from googletrans import Translator
from VoiceRecognition import *
import openpyxl


class App:
    """An app translating to Vietnamese using both text, and voice,
     add vocab to an Excel file """
    def __init__(self, root):
        self.root = root
        self.text_input = ''
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

        name = tk.Label(self.root, text="TRANSLATOR", fg="#303030", bg="#F9F7E8")
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
        trans_button.place(x=250, y=310)

        add_button = tk.Button(button_frame, text="Add to Excel", font=("Arial", 10, 'bold'), bg="#303030",fg="#FFFFFF",
                               command=self.add_excel)
        add_button.place(x=350, y=310)

        micro_button = tk.Button(button_frame, text="Add to Excel", font=("Arial", 10, 'bold'), bg="#303030",fg="#FFFFFF",
                               command=self.listen)
        micro_button.place(x=80, y = 100)
        audio_button = tk.Button(button_frame, text="Add to Excel", font=("Arial", 10, 'bold'), bg="#303030",fg="#FFFFFF",
                               command=self.add_excel)

    def start_loop(self):
        self.root.mainloop()

    def clear(self):
        self.input = ''
        self.output = ''
        self.box0.delete(1.0, tk.END)
        self.box1.delete(1.0, tk.END)

    def translate(self):
        self.input += self.box0.get(1.0, tk.END)
        if self.voice_input != '':
            self.input = self.voice_input
        if self.text_input != '':
            self.input = self.text_input

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

    def add_excel(self):
        wb = openpyxl.load_workbook('vocab.xlsx')
        sheet = wb['Sheet1']
        sheet.append([self.input, self.output])
        wb.save('vocab.xlsx')


window = tk.Tk()
translator = App(window)
translator.start_loop()
