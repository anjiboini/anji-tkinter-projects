from tkinter import *
from PIL import ImageTk,Image
import mysql.connector

root = Tk()
root.title('Wellcomt to thanusri')
root.iconbitmap('D:/anji_python software/python/anji tkinter projects/resources/thanu1.ico')
root.geometry('500x400')
#createDb = sqlite3.connect('anji_contacts_book')
#db = createDb.cursor()

mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "1234",
        database = "thanudatabase"
       )

#Create a cursor and initilize it
my_cursor = mydb.cursor()
#Create database

##my_cursor.execute("CREATE DATABASE thanudatabase")

#my_cursor.execute(("SHOW DATABASES"))
#print(my_cursor)
#for db in my_cursor:
 #   print(db)

#Create a table
#my_cursor.execute("CREATE TABLE customers (first_name VARCHAR(255),last_name VARCHAR(255),zipcode INT(10),price_paid DECIMAL(10,2),user_id INT AUTO_INCREMENT PRIMARY KEY)")

#show table
my_cursor.execute("SELECT * FROM customers")
print(my_cursor.description)
for thing in my_cursor.description:
    print(thing)



root.mainloop()