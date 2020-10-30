from tkinter import *
root = Tk()

e = Entry(root, width=50, bg="pink", fg="Black",borderwidth=10)
e.pack()
e.insert(0, "Enter Your Name: ")

def myClick1():
    hello = "Hello  " + e.get()
    myLabel1 = Label(root,text=hello ,fg='Blue')
    myLabel1.pack()




myButton1 = Button(root,text="Enter Your Name",command=myClick1,padx=50,pady=50,fg='Blue',bg='Yellow')


myButton1.pack()


root.mainloop()

