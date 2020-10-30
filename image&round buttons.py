from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random

root = Tk()
root.title('Flashcards!')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/yeshu1.ico')
root.geometry('700x500')

def thing():
    my_label.config(text="You clicked the button...")


login_btn = PhotoImage(file ="resources/login.png")

img_lable = Label(image=login_btn)
#img_lable.pack(pady=20)

my_button = Button(root, image=login_btn, command=thing, borderwidth=0)
my_button.pack(pady=20)

my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()

