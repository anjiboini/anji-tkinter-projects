from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk



root = Tk()
root.title('well come to India thanudatabase')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry('600x600')

def selected(event):
    #myLabel = Label(root, text=clicked.get()).pack()
    if clicked.get() == 'Friday':
        myLabel = Label(root, text="Yey Its Friday").pack()
    else:
        myLabel = Label(root, text=clicked.get()).pack()

def comboclick(event):
    myLabel = Label(root, text=mycombo.get()).pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",

]

clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked,*options, command=selected)
drop.pack(pady=20)

mycombo = ttk.Combobox(root, value=options)
mycombo.current(0)
mycombo.bind("<<ComboboxSelected>>", comboclick)
mycombo.pack()
#myButton = Button(root, text="select from list", command=selected)
#myButton.pack()
root.mainloop()

