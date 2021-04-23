from tkinter import *
import mysql.connector as msc
import TextToTableModule as tttm

def text_adder(name_e,lastName_e,age_e):
    mydb = msc.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'myfirstdatabase'
        )
    mycursor = mydb.cursor()
    
    if name_entry.get() == '' or lastName_entry.get() == '' or age_entry.get() == '':
        messagebox.showerror('Error!','You left one or more of the boxes empty.')

    else:
        sqlCommand = 'INSERT INTO student (name,lastname,age) VALUES (%s,%s,%s)'
        values = (name_entry.get(),lastName_entry.get(),age_entry.get())
        
        mycursor.execute(sqlCommand,values)
        mydb.commit()

window = Tk()

window.title('Text to table')
window.iconbitmap('txt_adder_ico.ico')

name_label = Label(window,text = 'Enter your name ===>').grid(row = 0, column = 0, padx = 10, pady = 10)
name_entry = Entry(window)
lastName_lbl = Label(window,text = 'Enter you last name ===>').grid(row = 1, column = 0, padx = 10, pady = 10)
lastName_entry = Entry(window)
age_lbl = Label(window,text = 'Enter your age ===>').grid(row = 2, column = 0, padx = 10, pady = 10)
age_entry = Entry(window)
submit_btn = Button(window,text = 'Submit',width = 20,height = 3,command = lambda: tttm.text_adder(name_entry.get(),lastName_entry.get(),age_entry.get())).grid(row = 3, column = 0, padx = 10, pady = 10)

name_entry.grid(row = 0, column = 1, padx = 10, pady = 10)
lastName_entry.grid(row = 1, column = 1, padx = 10, pady = 10)
age_entry.grid(row = 2, column = 1, padx = 10, pady = 10)

window.mainloop()