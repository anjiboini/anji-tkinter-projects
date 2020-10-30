from tkinter import *
from PIL import ImageTk,Image



root = Tk()
root.title('well come to India thanudatabase')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry('600x600')

def clicker(event):
    myLabel = Label(root,text="You clicked a button")
    myLabel.pack()

myButton = Button(root, text="click Me!")
myButton.bind("<Button-3>", clicker)
myButton.pack(pady=20)



root.mainloop()

