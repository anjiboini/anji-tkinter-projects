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

#panels create
panel_1 = PanedWindow(bd=4,orient=VERTICAL, relief="raised", bg="blue")
panel_1.pack(fill=BOTH, expand=1)
left_label = Label(panel_1, text="Left Panel")
panel_1.add(left_label)

panel_2 = PanedWindow(panel_1, orient=HORIZONTAL,bd=4, relief="raised", bg="red")
panel_1.add(panel_2)
top = Label(panel_2, text="Top Panel")
panel_2.add(top)
bottom = Label(panel_2, text="Bottom Panel")
panel_2.add(bottom)



root.mainloop()

