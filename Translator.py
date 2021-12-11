from tkinter import *
from PIL import Image, ImageTk
from googletrans import Translator
import VoiceRecognition

# create window
root = Tk()
root.title("GUI Translator")
root.geometry("564x650")
root.iconbitmap("christmas-tree.ico")

# bg
load = Image.open("bg.jpg")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=0, y=0)

name = Label(root, text="TRANSLATOR", fg="#FFFFFF")
name.config(font=("Arial",30))
name.pack(pady=10)

box = Text(root, width=28, height=8, font=("ROBOTO", 16))
box.pack(pady=20)
button_frame = Frame(root).pack(side=BOTTOM)


def clear():
    box.delete(1.0, END)
    box1.delete(1.0, END)


def translate():
    inp = box.get(1.0, END)
    print(inp)
    t = Translator()
    a = t.translate(inp, src="vi", dest="en")
    b = a.text
    box1.insert(END, b)


clear_button = Button(button_frame, text="Clear", font=("Arial", 10, 'bold'), bg="#303030", fg="#FFFFFF",
                      command=clear)
clear_button.place(x=150, y=310)
trans_button = Button(button_frame, text="Translate", font=("Arial", 10, 'bold'), bg="#303030", fg="#FFFFFF",
                      command=translate)
trans_button.place(x=290, y=310)

box1 = Text(root, width=28, height=8, font=("ROBOTO", 16))
box1.pack(pady=120)

root.mainloop()
