# program to delete data from table -python

import tkinter as tk
from tkinter import messagebox
import mysql.connector as sql

#creating function to search details
def search_details():

    #connecting to database
    db_connection=sql.connect(host='localhost',database='ems',user='root',password='')
    db_cursor=db_connection.cursor()
    
    #getting data from entry box
    Ecode=Ecode_entry.get()

    #query
    db_cursor.execute("select * from emp_details where Ecode=%s",[str(Ecode)])
    result=db_cursor.fetchone()

    #displaying data
    if result:
        Ename_entry.delete(0, tk.END)
        Ename_entry.insert(tk.END,result[1])

        Education_entry.delete(0, tk.END)
        Education_entry.insert(tk.END,result[2])

        Experience_entry.delete(0, tk.END)
        Experience_entry.insert(tk.END,result[3])

        Dcode_entry.delete(0, tk.END)
        Dcode_entry.insert(tk.END,result[4])
    else:
        messagebox.showinfo("Error","Employee Not Found")

    db_connection.close()

#creating function to delete data
def delete_details():

    #connecting to database
    db_connection=sql.connect(host='localhost',database='ems',user='root',password='')
    db_cursor=db_connection.cursor()

    #getting data from entry box
    Ecode=Ecode_entry.get()
    
    #query
    db_cursor.execute("delete from emp_details where Ecode=%s",[str(Ecode)])

    db_connection.commit()
    db_connection.close()
    clear_details()

    messagebox.showinfo("Employee Details","Data Deleted Successfully.")

#creating function to clear details
def clear_details():
    Ecode_entry.delete(0, tk.END)
    Ename_entry.delete(0, tk.END)
    Education_entry.delete(0, tk.END)
    Experience_entry.delete(0, tk.END)
    Dcode_entry.delete(0, tk.END)

#creating main window
window=tk.Tk()
window.title("Employee Management System")
window.geometry("800x400+300+0")

head=tk.Label(window,text="Delete Employee Details",font='sans 85 bold',bg='blue',fg='white')
head.grid(row=0,columnspan=4,padx=20,pady=10,sticky='nsew')

Ecode=tk.Label(window,text="Employee Code:",font='sans 40 bold',fg='black')
Ecode.grid(row=1,column=0)
Ecode_entry=tk.Entry(window,width=20,font='sans 35 bold')
Ecode_entry.grid(row=1,column=1)

Ename=tk.Label(window,text="Employee Name:",font='sans 40 bold',fg='black')
Ename.grid(row=2,column=0)
Ename_entry=tk.Entry(window,width=20,font='sans 35 bold')
Ename_entry.grid(row=2,column=1)

Education=tk.Label(window,text="Education",font='sans 40 bold',fg='black')
Education.grid(row=3,column=0)
Education_entry=tk.Entry(window,width=20,font='sans 35 bold')
Education_entry.grid(row=3,column=1)

Experience=tk.Label(window,text="Experience",font='sans 40 bold',fg='black')
Experience.grid(row=4,column=0)
Experience_entry=tk.Entry(window,width=20,font='sans 35 bold')
Experience_entry.grid(row=4,column=1)

Dcode=tk.Label(window,text="Dcode",font='sans 40 bold',fg='black')
Dcode.grid(row=5,column=0)
Dcode_entry=tk.Entry(window,width=20,font='sans 35 bold')
Dcode_entry.grid(row=5,column=1)


lbl=tk.Label(window,text='Employee Management System',font='sans 80 bold ', bg='skyblue')
lbl.grid(row=7,column=0,columnspan=8,sticky='nsew',padx=10,pady=10)

search_button=tk.Button(window,text="Search",width=15,font='sans 20 bold',command=search_details)
search_button.grid(row=2,column=3)


update_button=tk.Button(window,text="Delete",width=15,font='sans 35 bold',command=delete_details,fg='green')
update_button.grid(row=6,column=0,columnspan=4,sticky='w',padx=10,pady=10)

cancel_button=tk.Button(window,text="Cancel",width=15,font='sans 35 bold',bg='red',fg='black',command=window.destroy)
cancel_button.grid(row=6,column=1,columnspan=4,sticky='w',padx=10,pady=10)

window.mainloop()
