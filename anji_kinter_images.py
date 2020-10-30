from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title("welcome to India")
root.iconbitmap('thanu1.ico')

def forward(image_number):
    global my_label1
    global Button_forward
    global Button_back
    my_label1.grid_forget()
    my_label1 = Label(image=image_list[image_number-1])

def back():
    global my_label1
    global Button_forward
    global Button_back

Button_back = Button(root,text=">>",command=back,padx=10,pady=10,fg='Blue',bg='Yellow')
Button_exit = Button(root,text="Exit",command=root.quit,padx=10,pady=10,fg='Blue',bg='white')
Button_forward = Button(root,text="<<",command= lambda: forward(2),padx=10,pady=10,fg='Blue',bg='Pink')

Button_back.pack()
Button_exit.pack()
Button_forward.pack()

my_img1 = ImageTk.PhotoImage(Image.open("images/thanu.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/thanu1.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/thanu2.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/thanu3.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/thanu4.jpg"))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5]

my_label1 = Label(image=my_img1)
my_label2 = Label(image=my_img2)
my_label3 = Label(image=my_img3)
my_label4 = Label(image=my_img4)
my_label5 = Label(image=my_img5)

my_label1.pack()
my_label2.pack()
my_label3.pack()
my_label4.pack()
my_label5.pack()


root.mainloop()