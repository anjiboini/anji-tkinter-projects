from tkinter import *
from PIL import ImageTk,Image
import mysql.connector

root = Tk()
root.title('Wellcomt to yeshasri')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry('400x600')
#createDb = sqlite3.connect('anji_contacts_book')
#db = createDb.cursor()

mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "1234",
        database = "yeshudatabase"
       )

#Create a cursor and initilize it
my_cursor = mydb.cursor()
#Create database

#my_cursor.execute("CREATE DATABASE yeshudatabase")

#my_cursor.execute(("SHOW DATABASES"))
#print(my_cursor)
#for db in my_cursor:
 #   print(db)
'''
#Create a table
my_cursor.execute("CREATE TABLE IF NOT EXISTS yeshucustomers1 (first_name VARCHAR(255),\
    last_name VARCHAR(255),\
    user_id INT AUTO_INCREMENT PRIMARY KEY)")

my_cursor.execute("ALTER TABLE yeshucustomers1 ADD (\
    phone VARCHAR(255),\
    payment VARCHAR(50))")


#show table
my_cursor.execute("SELECT * FROM yeshucustomers1")
print(my_cursor.description)
for thing in my_cursor.description:
    print(thing)

'''

#Clear Text Fields
def clear_fields():
    first_name_label_box.delete(0,END)
    last_name_label_box.delete(0, END)
    username_label_box.delete(0, END)
    phone_label_box.delete(0, END)
    payment_label_box.delete(0, END)

''''

#Submit Customer to database

def add_customer():
    sql_command = "INSERT INTO customers (first_name,last_name,address1,address2,city,state,zipcode,country,phone,email,username,payment,discount,price)"
    values =(first_name_label_box.get(),last_name_label_box.get(),address1_label_box.get(),address2_label_box.get(),city_label_box.get(),state_label_box.get(),zipcode_label_box.get(),country_label_box.get(),phone_label_box.get(),email_label_box.get(),username_label_box.get(),payment_label_box.get(),discount_label_box.get(),price_paid_label_box.get())
    my_cursor.execute(sql_command,values)
    #Commit the changes the database
    mydb.commit()
    #clear the fields
    clear_fields()

'''
#Create Table
title_label = Label(root,text="Yeshu Customer Database", font=("Helvetica",16))
title_label.grid(row=0,column=0,columnspan=2,padx=20,pady="10")

#Create main form to enter custemor Data
first_name_label = Label(root,text="First Name",font=20).grid(row=1,column=0,sticky=W,padx=10)
last_name_label = Label(root,text="Last Name",font=20).grid(row=2,column=0,sticky=W,padx=10)
username_label = Label(root,text="User Name",font=20).grid(row=3,column=0,sticky=W,padx=10)
phone_label = Label(root,text="Phone Number",font=20).grid(row=4,column=0,sticky=W,padx=10)
payment_label = Label(root,text="Payment Method",font=20).grid(row=5,column=0,sticky=W,padx=10)

#Create Entry Boxes

first_name_label_box = Entry(root)
first_name_label_box.grid(row=1,column=1)
last_name_label_box = Entry(root)
last_name_label_box.grid(row=2,column=1)
username_label_box = Entry(root)
username_label_box.grid(row=3,column=1)
phone_label_box = Entry(root)
phone_label_box.grid(row=4,column=1)
payment_label_box = Entry(root)
payment_label_box.grid(row=5,column=1)

#Create Buttons

##add_customer_button.grid(row=15,padx=10,pady=10)
clear_fields_button = Button(root,text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=15,column=1,padx=10,pady=10)





root.mainloop()