from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
import csv
from tkinter import ttk
from random import randint
from tkinter import  colorchooser
root = Tk()
root.title('well come to India thanudatabase')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry('600x600')

def color():
    my_color = colorchooser.askcolor()[1]
    my_label = Label(root, text=my_color).pack(pady=10)
    my_label2 = Label(root, text = "THANU SRI BOINI AND YESHA SRI BOINI", font =("Helvetica",32), bg= my_color).pack()

my_button = Button(root, text="Pick A Color", command=color, width=10,height=5 )
my_button.pack()


root.mainloop()

