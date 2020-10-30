from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random

root = Tk()
root.title('Flashcards!')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/yeshu1.ico')
root.geometry('700x500')

def number():
    try:
        int (my_box.get())
        answer.config(text="That is a number!..")
    except ValueError:
        answer.config(text="That is not  a number!..")

my_label = Label(root, text="Enter a Number")
my_label.pack(pady=20)

my_box = Entry(root)
my_box.pack(pady=10)

my_button = Button(root, text='Enter a Number', command=number)
my_button.pack(pady=5)

answer = Label(root,text='')
answer.pack(pady=20)

root.mainloop()

