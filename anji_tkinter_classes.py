from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
import csv
from tkinter import ttk
from random import randint
root = Tk()
root.title('well come to India thanudatabase')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry('600x600')


class thanu:
    def __init__(self,master):
        myFrame = Frame(master)
        myFrame.pack()
        self.myButton =Button(master,text="Click Me!", command=self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print("Look at you... you clicked a button")


e = thanu(root)



root.mainloop()

