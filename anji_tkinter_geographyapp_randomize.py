from tkinter import *
from PIL import ImageTk,Image
from random import  randint


root = Tk()
root.title('Flashcards!')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/yeshu1.ico')
root.geometry('600x600')

#create Randomizing state functions
def random_state():

    # create a list of sates names
    global our_states
    our_states = ['andhra', 'kerala', 'tamilnadu', 'telangana', 'three', 'four']
    # generate a random number
    global rando
    rando = randint(0, len(our_states) - 1)
    state = "resources/" + our_states[rando] + ".png"
    # create our states Images
    global state_img
    state_img = ImageTk.PhotoImage(Image.open(state))
    show_state.config(image=state_img)

    #show_state = Label(state_frame)
    #show_state.pack(pady=15)



def state_answer():
    answer = answer_input.get()
    answer = answer.replace(" "," ")
    #determine if our answer is right or wrong!
    if answer.lower() == our_states[rando]:
        response = "Correct! " + our_states[rando]
    else:
        response = "Wrong! " + our_states[rando]

    answer_label.config(text=response)
    #clear the entry box
    answer_input.delete(0, 'end')
    random_state()



def states():
    #hide previous frames
    hide_all_frames()
    state_frame.pack(fill="both", expand=1)
    #my_label = Label(state_frame, text ="States").pack()



    '''
    #create a list of sates names
    global our_states
    our_states = ['andhra','kerala','tamilnadu','telanga','three','four']
    #generate a random number
    global rando
    rando = randint(0, len(our_states) -1)
    
    #create our states Imagesstate = "resources/" + our_states[rando] + ".png"
    global state_img
    state_img = ImageTk.PhotoImage(Image.open(state))
    
    '''
    global show_state
    show_state = Label(state_frame)
    show_state.pack(pady=15)
    random_state()


    # create answer input
    global answer_input
    answer_input = Entry(state_frame, font=("Helvetica", 20))
    answer_input.pack(pady=15)

    #create button to random state images
    rando_button = Button(state_frame, text="Next State", command=states)
    rando_button.pack(pady=10)

    answer_button = Button(state_frame, text="Answer", command=state_answer, width=20)
    answer_button.pack(pady=5)

    # create label to tell us if we got answer right or not
    global answer_label
    answer_label = Label(state_frame, text=" ", font=("Helvetica", 30), fg="red")
    answer_label.pack(pady=15)


def states_capitals():
    # hide previous frames
    hide_all_frames()
    state_capitals_frame.pack(fill="both", expand=1)
    my_label = Label(state_capitals_frame, text="Capitals").pack()

def hide_all_frames():
    #loop thru and destroy all children in previous frames
    for widget in state_frame.winfo_children():
        widget.destroy()

    for widget in state_capitals_frame.winfo_children():
        widget.destroy()


    state_frame.pack_forget()
    state_capitals_frame.pack_forget()
#create our menu
my_menu = Menu(root)
root.config(menu=my_menu)

#create menu items
states_menu = Menu(my_menu)
my_menu.add_cascade(label="Geography", menu=states_menu)
states_menu.add_command(label="States", command=states)
states_menu.add_command(label="States Capitals", command=states_capitals)
states_menu.add_separator()
states_menu.add_command(label="Exit", command=root.quit)

#create frames
state_frame = Frame(root, width=800, height=800)
state_capitals_frame = Frame(root, width=500, height=500, bg="pink")


root.mainloop()

