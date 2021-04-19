from tkinter import *
import mysql.connector as msc

def text_adder():
    mydb = msc.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'myfirstdatabase'
        )


window = Tk()

name_label = Label(window,text = 'Enter your name ===>').grid(row = 0, column = 0, padx = 10, pady = 10)
name_entry = Entry(window)
lastName_lbl = Label(window,text = 'Enter you last name ===>').grid(row = 1, column = 0, padx = 10, pady = 10)
lastName_entry = Entry(window)
age_lbl = Label(window,text = 'Enter your age ===>').grid(row = 2, column = 0, padx = 10, pady = 10)
age_entry = Entry(window)
submit_btn = Button(window,text = 'Submit',width = 20,height = 3).grid(row = 3, column = 0, padx = 10, pady = 10)

name_entry.grid(row = 0, column = 1, padx = 10, pady = 10)
lastName_entry.grid(row = 1, column = 1, padx = 10, pady = 10)
age_entry.grid(row = 2, column = 1, padx = 10, pady = 10)

window.mainloop()