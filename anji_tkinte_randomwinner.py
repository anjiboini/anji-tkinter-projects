from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
import csv
from tkinter import ttk
from random import randint
root = Tk()
root.title('well come to India thanudatabase')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry('400x1000')


def pick():
    # entrys 4
    entries = ['thanu sri','yesha sri','kavi','anji']
    entries_set = set(entries)
    #convert back to list
    unique_entries = list(entries_set)
    our_nuumber = len(unique_entries)-1
    rando = randint(0,our_nuumber)

    winnerLabel = Label(root,text=unique_entries[rando],font=("Helvetica",24),fg="red")
    winnerLabel.pack(pady=20)

topLabel = Label(root,text="Win is Winner", font=("Helvetica",24),fg="blue")
topLabel.pack(pady=50)


winButton = Button(root,text="PICK OUR WINNER!",font=("Helvetica",24),fg="green",bg="pink", command=pick)
winButton.pack(pady=20)








root.mainloop()

