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

my_label = Label(root,text ='41' + u'\u00A9', font = ("Helvetica",32)).pack()

my_button = Button(root,text =u'\u00BB',font = ("Helvetica",32))
my_button.pack(pady=20)

root.mainloop()

