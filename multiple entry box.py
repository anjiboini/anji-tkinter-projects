from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random

root = Tk()
root.title('Flashcards!')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/yeshu1.ico')
root.geometry('700x500')

my_entries = []
def something():
    entry_list = ''
    for entries in my_entries:
        entry_list = entry_list + str(entries.get()) + '\n'
        my_lable.config(text=entry_list)
    print(my_entries[2].get())
# Row loop
for y in range(5):

    # colomn loop
    for x in range(5):
        my_entry = Entry(root)
        my_entry.grid(row=y,column=x, pady=20,padx=5)
        my_entries.append(my_entry)

my_button = Button(root, text="Click Me", command=something)
my_button.grid(row=6,column=0, pady=20)

my_lable = Label(root, text='')
my_lable.grid(row=7,column=0, pady=20)

root.mainloop()

