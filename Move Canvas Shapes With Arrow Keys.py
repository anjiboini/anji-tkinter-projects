from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random

root = Tk()
root.title('Flashcards!')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/yeshu1.ico')
root.geometry('700x500')

w = 600
h = 400
x = w//2
y = h//2


my_canvas = Canvas(root, width=w, height=h, bg="pink")
my_canvas.pack(pady=20)
#create line
#my_canvas.create_line(x1,y1,x2,y2, fill="color")
#my_canvas.create_line(0,100,300,100, fill="red")
#my_canvas.create_line(150,0,150,200, fill="red")
#create rectangle
#my_canvas.create_rectangle(x1,y1,x2,y2, fill="color")
#my_canvas.create_rectangle(50,150,250,50, fill="green")
#create oaval
#my_canvas.create_oval(50,150,250,50, fill="red")
#my_canvas.create_rectangle(50,50,50,50, fill="black")




my_circle= my_canvas.create_oval(x,y,x+100,y+100, fill="red")

def left(event):
    x = -10
    y = 0
    my_canvas.move(my_circle,x,y)

def right(event):
    x = 10
    y = 0
    my_canvas.move(my_circle,x,y)

def up(event):
    x = 0
    y = -10
    my_canvas.move(my_circle,x,y)

def down(event):
    x = 0
    y = 10
    my_canvas.move(my_circle,x,y)
def pressing(event):
    x=0
    y=0
    if event.char == "a": x= -10
    if event.char == "d": x = 10
    if event.char == "w": y = -10
    if event.char == "s": y = 10
    my_canvas.move(my_circle,x,y)

root.bind("<Key>",pressing)
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)




root.mainloop()

