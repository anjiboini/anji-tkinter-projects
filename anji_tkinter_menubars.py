from tkinter import *

root = Tk()
root.title('well come to India thanudatabase')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry('600x600')

my_menu = Menu(root)
root.config(menu=my_menu)

#click command
def our_command():
    my_label = Label(root, text="You Clicked A Dropdown Menu").pack()
def file_new():
    hide_all_frames()
    my_label = Label(file_new_frame, text="You Clicked File Menu >> New menu").pack()
    file_new_frame.pack(fill="both", expand=1)
def edit_cut():
    hide_all_frames()
    my_label = Label(edit_new_frame, text="You Clicked Edit Menu >> Cut menu").pack()
    edit_new_frame.pack(fill="both", expand=1)

def hide_all_frames():
    file_new_frame.pack_forget()
    edit_new_frame.pack_forget()


#create menu items
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_cascade(label="New..", command = file_new)
file_menu.add_separator()
file_menu.add_cascade(label="Exit", command =root.quit)


#Create Edit items
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_cascade(label="Cut..", command = edit_cut)
edit_menu.add_cascade(label="Copy..", command = our_command)

#Create Navigate items
navigate_menu = Menu(my_menu)
my_menu.add_cascade(label="Navigate", menu=navigate_menu)
navigate_menu.add_cascade(label="Class", command = our_command)
navigate_menu.add_cascade(label="File", command = our_command)


#create some frames
file_new_frame = Frame(root, width=400,height=400, bg="red")
edit_new_frame = Frame(root, width=400,height=400, bg="blue")




root.mainloop()

