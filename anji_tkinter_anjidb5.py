from tkinter import *
from PIL import ImageTk,Image
import mysql.connector

root = Tk()
root.title('Wellcomt to thanusri')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry('400x600')
#createDb = sqlite3.connect('anji_contacts_book')
#db = createDb.cursor()

mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "1234",
        database = "thanudatabase3"
       )

#Create a cursor and initilize it
my_cursor = mydb.cursor()
#Create database

#my_cursor.execute("CREATE DATABASE thanudatabase3")

my_cursor.execute(("SHOW DATABASES"))
print(my_cursor)
for db in my_cursor:
    print(db)
'''
#Create a table
my_cursor.execute("CREATE TABLE IF NOT EXISTS customers1 (first_name VARCHAR(255),\
    last_name VARCHAR(255),\
    zipcode INT(10),\
    price_paid DECIMAL(10,2),\
    user_id INT AUTO_INCREMENT PRIMARY KEY)")

my_cursor.execute("ALTER TABLE customers1 ADD (email VARCHAR(255),\
    address1 VARCHAR(255),\
    address2 VARCHAR(255),\
    city VARCHAR(50),\
    state VARCHAR(50),\
    country VARCHAR(255),\
    phone VARCHAR(255),\
    payment VARCHAR(50),\
    discount VARCHAR(255))")

'''
#show table
#my_cursor.execute("SELECT * FROM customers1")
#print(my_cursor.description)
#for thing in my_cursor.description:
 #   print(thing)

#Clear Text Fields
def clear_fields():
    first_name_label_box.delete(0,END)
    last_name_label_box.delete(0, END)
    address1_label_box.delete(0, END)
    address2_label_box.delete(0, END)
    city_label_box.delete(0, END)
    state_label_box.delete(0, END)
    zipcode_label_box.delete(0, END)
    country_label_box.delete(0, END)
    phone_label_box.delete(0, END)
    email_label_box.delete(0, END)
    username_label_box.delete(0, END)
    payment_label_box.delete(0, END)
    discount_label_box.delete(0, END)
    price_paid_label_box.delete(0, END)


#Submit Customer to database
''''
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
title_label = Label(root,text="Thanu Customer Database", font=("Helvetica",16))
title_label.grid(row=0,column=0,columnspan=2,padx=20,pady="10")

#Create main form to enter custemor Data
first_name_label = Label(root,text="First Name",font=20).grid(row=1,column=0,sticky=W,padx=10)
last_name_label = Label(root,text="Last Name",font=20).grid(row=2,column=0,sticky=W,padx=10)
address1_label = Label(root,text="Address1",font=20).grid(row=3,column=0,sticky=W,padx=10)
address2_label = Label(root,text="Address2",font=20).grid(row=4,column=0,sticky=W,padx=10)
city_label = Label(root,text="City",font=20).grid(row=5,column=0,sticky=W,padx=10)
state_label = Label(root,text="State",font=20).grid(row=6,column=0,sticky=W,padx=10)
zipcode_label = Label(root,text="Pincode",font=20).grid(row=7,column=0,sticky=W,padx=10)
country_label = Label(root,text="Country",font=20).grid(row=8,column=0,sticky=W,padx=10)
phone_label = Label(root,text="Phone Number",font=20).grid(row=9,column=0,sticky=W,padx=10)
email_label = Label(root,text="Email",font=20).grid(row=10,column=0,sticky=W,padx=10)
username_label = Label(root,text="User Name",font=20).grid(row=11,column=0,sticky=W,padx=10)
payment_label = Label(root,text="Payment Method",font=20).grid(row=12,column=0,sticky=W,padx=10)
discount_label = Label(root,text="Discount Count",font=20).grid(row=13,column=0,sticky=W,padx=10)
price_paid_label = Label(root,text="Price Paid",font=20).grid(row=14,column=0,sticky=W,padx=10)


#Create Entry Boxes

first_name_label_box = Entry(root)
first_name_label_box.grid(row=1,column=1)
last_name_label_box = Entry(root)
last_name_label_box.grid(row=2,column=1)
address1_label_box = Entry(root)
address1_label_box.grid(row=3,column=1)
address2_label_box = Entry(root)
address2_label_box.grid(row=4,column=1)
city_label_box = Entry(root)
city_label_box.grid(row=5,column=1)
state_label_box = Entry(root)
state_label_box.grid(row=6,column=1)
zipcode_label_box = Entry(root)
zipcode_label_box.grid(row=7,column=1)
country_label_box = Entry(root)
country_label_box.grid(row=8,column=1)
phone_label_box = Entry(root)
phone_label_box.grid(row=9,column=1)
email_label_box = Entry(root)
email_label_box.grid(row=10,column=1)
username_label_box = Entry(root)
username_label_box.grid(row=11,column=1)
payment_label_box = Entry(root)
payment_label_box.grid(row=12,column=1)
discount_label_box = Entry(root)
discount_label_box.grid(row=13,column=1)
price_paid_label_box = Entry(root)
price_paid_label_box.grid(row=14,column=1)

#Create Buttons

##add_customer_button.grid(row=15,padx=10,pady=10)
clear_fields_button = Button(root,text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=15,column=1,padx=10,pady=10)





root.mainloop()