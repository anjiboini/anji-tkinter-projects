from tkinter import *
from PIL import ImageTk,Image
import mysql.connector
import csv
from tkinter import ttk

root = Tk()
root.title('well come to India thanudatabase')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry('600x400')

mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "1234",
        database = "anji_customer",

        )
#create cursor
my_cursor = mydb.cursor()
#create database
#my_cursor.execute("CREATE DATABASE anji_customer")
#show database
#my_cursor.execute("SHOW DATABASES")
#print(my_cursor)
#for db in my_cursor:
#    print(db)
'''
#Create a Tabel
my_cursor.execute("CREATE TABLE IF NOT EXISTS anji_customer (first_name VARCHAR(255),\
    last_name VARCHAR(255),\
    user_id INT AUTO_INCREMENT PRIMARY KEY)")

my_cursor.execute("ALTER TABLE anji_customer ADD (\
    phone VARCHAR(255),\
    payment VARCHAR(50))")

'''
#show  table
'''
my_cursor.execute("SELECT * FROM anji_customer")
print(my_cursor.description)
for thing in my_cursor.description:
    print(thing)
'''

def clear_fields():
    first_name_label_box.delete(0,END)
    last_name_label_box.delete(0, END)
    username_label_box.delete(0, END)
    phone_label_box.delete(0, END)
    payment_label_box.delete(0, END)
#write to csv exel function


def add_customer():
    sql_command = "INSERT INTO anji_customer (first_name,last_name,user_id,phone,payment) VALUES (%s,%s,%s,%s,%s)"
    values =(first_name_label_box.get(),last_name_label_box.get(),username_label_box.get(),phone_label_box.get(),payment_label_box.get())
    my_cursor.execute(sql_command,values)
    #Commit the changes the database
    mydb.commit()
    #clear the fields
    clear_fields()

def write_to_csv(result):
    with open('anji_customers5.csv', 'a',newline="") as f:
        w = csv.writer(f,dialect='excel')
        #w.writerow(result)
        for record in result:
            w.writerow(record)
#Search customers
def search_customer():
    search_customers = Tk()
    search_customers.title("Search  Customers")
    search_customers.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
    search_customers.geometry("1000x400")

    def update():
        sql_command = """  UPDATE anji_customer SET first_name = %s, last_name = %s, phone = %s, payment = %s WHERE user_id = %s """

        first_name = first_name_box2.get()
        last_name = last_name_box2.get()
        phone = phone_box2.get()
        payment = payment_box2.get()
        id_value = id_box2.get()
        inputs = (first_name, last_name, phone, payment, id_value )

        my_cursor.execute(sql_command,inputs)
        mydb.commit()

        search_customers.destroy()

    def edit_now(id,index):
        sql2 = "SELECT * FROM anji_customer where user_id = %s"
        name2 = (id,)
        result2 = my_cursor.execute(sql2, name2)
        result2 = my_cursor.fetchall()
        index+=1
        # Create main form to enter custemor Data
        first_name_label = Label(search_customers, text="First Name", font=20).grid(row=index+1, column=0, sticky=W, padx=10)
        last_name_label = Label(search_customers, text="Last Name", font=20).grid(row=index+2, column=0, sticky=W, padx=10)
        user_id_label = Label(search_customers, text="User Name", font=20).grid(row=index+3, column=0, sticky=W, padx=10)
        phone_label = Label(search_customers, text="Phone Number", font=20).grid(row=index+4, column=0, sticky=W, padx=10)
        payment_label = Label(search_customers, text="Payment Method", font=20).grid(row=index+5, column=0, sticky=W, padx=10)
        id_label = Label(search_customers, text="User Name").grid(row=index+6, column=0, sticky=W, padx=10)

        # Create Entry Boxes
        global first_name_box2
        first_name_box2 = Entry(search_customers)
        first_name_box2.grid(row=index+1, column=1)
        first_name_box2.insert(0,result2[0][0])

        global last_name_box2
        last_name_box2 = Entry(search_customers)
        last_name_box2.grid(row=index+2, column=1)
        last_name_box2.insert(0,result2[0][1])

        global user_id_box2
        user_id_box2 = Entry(search_customers)
        user_id_box2.grid(row=index+3, column=1)
        user_id_box2.insert(0,result2[0][2])

        global phone_box2
        phone_box2 = Entry(search_customers)
        phone_box2.grid(row=index+4, column=1)
        phone_box2.insert(0,result2[0][3])

        global payment_box2
        payment_box2 = Entry(search_customers)
        payment_box2.grid(row=index+5, column=1)
        payment_box2.insert(0,result2[0][4])

        global id_box2
        id_box2 = Entry(search_customers)
        id_box2.grid(row=index+6, column=1,pady=5)
        id_box2.insert(0,result2[0][2])

        save_record = Button(search_customers, text = "Update Record" )
        save_record.grid(row=index+7,column=0,padx=10)


    def search_now():
        selected = drop.get()
        sql = ""
        if selected == "Search By....":
            test = Label(search_customers, text="Hey! You forgot to pick a drop down selection")
            test.grid(row=4,column=0)
        if selected == "Last Name":
            sql = "SELECT * FROM anji_customer where last_name = %s"
            #test = Label(search_customers, text="Hey! You picked Last Name")
            #test.grid(row=5, column=0)
        if selected == "Phone Number":
            sql = "SELECT * FROM anji_customer where phone = %s"
            #test = Label(search_customers, text="Hey! You picked Phone Number")
            #test.grid(row=6, column=0)
        if selected == "username":
            sql = "SELECT * FROM anji_customer where user_id = %s"
            #test = Label(search_customers, text="Hey! You picked User Name")
            #test.grid(row=7, column=0)


        searched = search_box.get()
        #sql = "SELECT * FROM anji_customer where first_name = %s"
        name = (searched,)
        result = my_cursor.execute(sql, name)
        result = my_cursor.fetchall()
        if not result:
            result = "Record Not Found ...."
            lookup_label = Label(search_customers, text=result, font=("Helvetica", 15), fg="blue")
            lookup_label.grid(row=2, column=0, columnspan=2, padx=10, pady="10")
        else:
            for index, x in enumerate(result):
             num = 0
             index +=2
             id_reference = str(x[4])
             edit_button = Button(search_customers,text="Edit", command=lambda :edit_now(id_reference,index))
             edit_button.grid(row=index, column=num)
             for y in x:
                lookup_label = Label(search_customers, text=y, font=("Helvetica", 15),fg="blue")
                lookup_label.grid(row=index, column=num,columnspan=2, padx=40,pady="10")
                num += 1
            csv_button = Button(search_customers, text="Save to Excel", command=lambda: write_to_csv(result))
            csv_button.grid(row=index + 1, column=5)


        #searched_label = Label(search_customers, text = result)
        #searched_label.grid(row=3,column=2,padx=10,columnspan=2)



    #search box to search customers
    search_box = Entry(search_customers)
    search_box.grid(row=0,column=4,padx=10,pady=10)
    #searc box label
    search_box_label=Label(search_customers, text="Search Customers By Last name :")
    search_box_label.grid(row=0, column=3, padx=10, pady=10)
    # Entry box search button for customers

    search_button = Button(search_customers,text="Search Customers",command=search_now)
    search_button.grid(row=0, column=9, padx=10, pady=10)

    #Drop Down Box
    drop = ttk.Combobox(search_customers,value = ["Search By....","Last Name","Phone Number","username"])
    drop.current(0)
    drop.grid(row=0,column=6)

def list_customers():
    list_customers_query = Tk()
    list_customers_query.title("List All Customers")
    list_customers_query.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
    list_customers_query.geometry("500x300")

    #list_customers_query_title = Label(list_customers_query,text="Anji Customers List", font=("Helvetica",16))
    #list_customers_query_title.grid(row=0,column=0,columnspan=2,padx=40,pady="10")

    #Query the database
    my_cursor.execute("SELECT * FROM anji_customer")
    result = my_cursor.fetchall()

    for index,x in enumerate(result):
        num = 0
        for y in x:
            lookup_label = Label(list_customers_query, text = y,font=("Helvetica",10)).grid(row=index,column=num,columnspan=2,padx=10,pady="10")
            num +=1
    csv_button = Button(list_customers_query,text="Save to Excel",command=lambda:write_to_csv(result))
    csv_button.grid(row=index+1,column=0)

#Create Label
title_label = Label(root,text="Anji Customer Database", font=("Helvetica",16))
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
add_customer_button = Button(root,text="Add Customer To Database", command = add_customer)
add_customer_button.grid(row=15,padx=10,pady=10)
clear_fields_button = Button(root,text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=15,column=1,padx=10,pady=10)
#list customer button
list_customer_button = Button(root, text="List Customer",command=list_customers)
list_customer_button.grid(row=16,column=0,sticky=W,padx=10)
#Search Customers
search_customers_button = Button(root,text="Search Customers/ Edit", command = search_customer)
search_customers_button.grid(row=16,column=1,sticky=W,padx=10)

#Select data from db
my_cursor.execute("SELECT * FROM anji_customer")
result = my_cursor.fetchall()
for x in result:
    print(x)


root.mainloop()

