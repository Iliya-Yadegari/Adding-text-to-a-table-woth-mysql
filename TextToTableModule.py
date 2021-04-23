from tkinter import *
import mysql.connector as msc


def text_adder(name_e,lastName_e,age_e):
    mydb = msc.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'myfirstdatabase'
        )
    mycursor = mydb.cursor()
    
    if name_e == '' or lastName_e == '' or age_e == '':
        messagebox.showerror('Error!','You left one or more of the boxes empty.')

    else:
        sqlCommand = 'INSERT INTO student (name,lastname,age) VALUES (%s,%s,%s)'
        values = (name_e,lastName_e,age_e)
        
        mycursor.execute(sqlCommand,values)
        mydb.commit()