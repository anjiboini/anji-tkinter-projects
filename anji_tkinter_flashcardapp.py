from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random

root = Tk()
root.title('Flashcards!')
root.iconbitmap('resources/yeshu1.ico')
root.geometry('600x600')

#create addition answer function
def answer_add():
    answer = num_1 + num_2
    if int(add_answer.get()) == answer:
        response = "Correct!"   + str(num_1) + " + " + str(num_2) + " = " + str(answer)
    else:
        response = "Wrong!"   + str(num_1) + " + " + str(num_2) + " = " + str(answer) + " Not " +   add_answer.get()

    answer_message.config(text=response)
    add_answer.delete(0, 'end')

def answer_sub():
    answer =   num_2 -  num_1
    answer1 =  num_1 - num_2

    if int(sub_answer.get()) == (answer):
        response = "Correct!"   + str(num_1) + " - " + str(num_2) + " = " + str(answer)

    elif int(sub_answer.get()) == (answer1):
        response = "Correct!"   + str(num_1) + " - " + str(num_2) + " = " + str(answer1)

    else:
        response = "Wrong!"   + str(num_1) + " - " + str(num_2) + " = " + str(answer) + " Not " +   sub_answer.get()

    answer_message.config(text=response)
    sub_answer.delete(0, 'end')

def answer_mult():
    answer = num_1 * num_2
    if int(mult_answer.get()) == answer:
        response = "Correct!"   + str(num_1) + " * " + str(num_2) + " = " + str(answer)
    else:
        response = "Wrong!"   + str(num_1) + " * " + str(num_2) + " = " + str(answer) + " Not " +   mult_answer.get()

    answer_message.config(text=response)
    mult_answer.delete(0, 'end')



def states():
    hide_all_frames()
    state_frame.pack(fill="both", expand=1)

def state_capitals():
    hide_all_frames()
    state_capitals_frame.pack(fill="both", expand=1)

def add():
    hide_all_frames()
    add_frame.pack(fill="both", expand=1)

    add_label = Label(add_frame, text = "Addition Flashcard", font=("Helvetica", 28))
    add_label.pack(pady=20)
    pic_frame = Frame(add_frame, width=600, height = 500)
    pic_frame.pack()

    # generate a random number
    global num_1
    global num_2

    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    # create 2 labels inside our pic frame, frame
    add_1 = Label(pic_frame, text="+", font=("Helvetica", 40), fg="red")
    add_2 = Label(pic_frame, text="+", font=("Helvetica", 40), fg="red")
    math_sign = Label(pic_frame, text=" + ", font=("Helvetica", 50), fg="blue")

    # Grid labels
    add_1.grid(row=0, column=0)
    add_2.grid(row=0, column=4)
    math_sign.grid(row=0, column=3)

    global add_image1
    global add_image2
    card1 = "resources/" + str(num_1) + ".png"
    card2 = "resources/" + str(num_2) + ".png"
    add_image1 = ImageTk.PhotoImage(Image.open(card1))
    add_image2 = ImageTk.PhotoImage(Image.open(card2))
    # put flashcard images on the screen
    add_1.config(image=add_image1)
    add_2.config(image=add_image2)

    # create button to random state images
    rando_button = Button(add_frame, text="Next Question", width=20, bg="green", font=("Helvetica", 15), command=add)
    rando_button.pack(pady=20)

    # create label
    add_answer_label = Label(add_frame, text="Enter Value", font=("Helvetica", 25), bg="white")
    add_answer_label.pack(pady=30)
    # create answer box and button
    global add_answer
    add_answer = Entry(add_frame, font=("Helvetica", 25), bg="pink")
    add_answer.pack(pady=30)

    add_answer_button = Button(add_frame, text="Answer", width=20, command=answer_add, bg="pink")
    add_answer_button.pack(pady=10)

    global answer_message
    answer_message = Label(add_frame, text="   ", font=("Helvetica", 50), bg="yellow")
    answer_message.pack(pady=50)







def sub():
    hide_all_frames()
    sub_frame.pack(fill="both", expand=1)

    sub_label = Label(sub_frame, text="Addition Flashcard", font=("Helvetica", 28))
    sub_label.pack(pady=20)
    pic_frame = Frame(sub_frame, width=600, height=500)
    pic_frame.pack()

    #generate a random number
    global num_1
    global num_2

    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    #create 2 labels inside our pic frame, frame
    sub_1 = Label(pic_frame, text="+", font=("Helvetica", 40), fg="red")
    sub_2 = Label(pic_frame, text="+", font=("Helvetica", 40), fg="red")
    math_sign1 = Label(pic_frame, text=" - ", font=("Helvetica", 50), fg="blue")

    # Grid labels
    sub_1.grid(row=0, column=0)
    sub_2.grid(row=0, column=4)
    math_sign1.grid(row=0, column=3)

    global sub_image1
    global sub_image2
    card1 = "resources/" + str(num_1) + ".png"
    card2 = "resources/" + str(num_2) + ".png"
    sub_image1 = ImageTk.PhotoImage(Image.open(card1))
    sub_image2 = ImageTk.PhotoImage(Image.open(card2))
    # put flashcard images on the screen
    sub_1.config(image=sub_image1)
    sub_2.config(image=sub_image2)

    # create button to random state images
    rando_button1 = Button(sub_frame, text="Next Question", width=20, bg="green", font=("Helvetica", 15), command=sub)
    rando_button1.pack(pady=20)

    # create label
    sub_answer_label = Label(sub_frame, text="Enter Value", font=("Helvetica", 25), bg="white")
    sub_answer_label.pack(pady=30)

    # create answer box and button
    global sub_answer
    sub_answer = Entry(sub_frame, font=("Helvetica", 25), bg="pink")
    sub_answer.pack(pady=30)

    sub_answer_button = Button(sub_frame, text="Answer", width=20, command=answer_sub, bg="pink")
    sub_answer_button.pack(pady=10)

    global answer_message
    answer_message = Label(sub_frame, text="   ", font=("Helvetica", 50), bg="yellow")
    answer_message.pack(pady=50)



def mult():
    hide_all_frames()
    mult_frame.pack(fill="both", expand=1)

    mult_label = Label(mult_frame, text="Addition Flashcard", font=("Helvetica", 28))
    mult_label.pack(pady=20)
    pic_frame = Frame(mult_frame, width=600, height=500)
    pic_frame.pack()

    #generate a random number
    global num_1
    global num_2

    num_1 = randint(0, 10)
    num_2 = randint(0, 10)

    #create 2 labels inside our pic frame, frame
    mult_1 = Label(pic_frame, text="+", font=("Helvetica", 40), fg="red")
    mult_2 = Label(pic_frame, text="+", font=("Helvetica", 40), fg="red")
    math_sign2 = Label(pic_frame, text=" * ", font=("Helvetica", 50), fg="blue")

    # Grid labels
    mult_1.grid(row=0, column=0)
    mult_2.grid(row=0, column=4)
    math_sign2.grid(row=0, column=3)

    global mult_image1
    global mult_image2
    card1 = "resources/" + str(num_1) + ".png"
    card2 = "resources/" + str(num_2) + ".png"
    mult_image1 = ImageTk.PhotoImage(Image.open(card1))
    mult_image2 = ImageTk.PhotoImage(Image.open(card2))
    # put flashcard images on the screen
    mult_1.config(image=mult_image1)
    mult_2.config(image=mult_image2)

    # create button to random state images
    rando_button2 = Button(mult_frame, text="Next Question", width=20, bg="green", font=("Helvetica", 15), command=mult)
    rando_button2.pack(pady=20)

    # create label
    mult_answer_label = Label(mult_frame, text="Enter Value", font=("Helvetica", 25), bg="white")
    mult_answer_label.pack(pady=30)

    # create answer box and button
    global mult_answer
    mult_answer = Entry(mult_frame, font=("Helvetica", 25), bg="pink")
    mult_answer.pack(pady=30)

    mult_answer_button = Button(mult_frame, text="Answer", width=20, command=answer_mult, bg="pink")
    mult_answer_button.pack(pady=10)

    global answer_message
    answer_message = Label(mult_frame, text="   ", font=("Helvetica", 50), bg="yellow")
    answer_message.pack(pady=50)


def hide_all_frames():
    #loop thru and destroy all children in previous frames
    for widget in state_frame.winfo_children():
        widget.destroy()

    for widget in state_capitals_frame.winfo_children():
        widget.destroy()

    for widget in add_frame.winfo_children():
        widget.destroy()

    for widget in sub_frame.winfo_children():
        widget.destroy()

    for widget in mult_frame.winfo_children():
        widget.destroy()

    add_frame.pack_forget()
    sub_frame.pack_forget()
    mult_frame.pack_forget()
    state_frame.pack_forget()
    state_capitals_frame.pack_forget()


#create our menu

my_menu = Menu(root)
root.config(menu=my_menu)

#create geography menu items

states_menu = Menu(my_menu)
my_menu.add_cascade(label="Geography", menu=states_menu)
states_menu.add_command(label="States", command = states)
states_menu.add_command(label="State Capitals", command = state_capitals)
states_menu.add_separator()
states_menu.add_command(label="Exit", command = root.quit)

#math flash card menu
math_menu = Menu(my_menu)
my_menu.add_cascade(label="Math", menu=math_menu)
math_menu.add_command(label="Addition", command =add)
math_menu.add_command(label="Substruction", command =sub)
math_menu.add_command(label="Multification", command =mult)


#create frames
state_frame = Frame(root, width=500, height=500, bg="pink")
state_capitals_frame = Frame(root, width=500, height=500, bg="red")

#addition frame

add_frame = Frame(root, width=800, height=1200, bg="blue")
sub_frame = Frame(root, width=800, height=1200, bg="blue")
mult_frame = Frame(root, width=800, height=1200, bg="blue")



root.mainloop()

