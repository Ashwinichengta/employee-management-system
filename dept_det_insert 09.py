# Program to insert department details - Python
#importing packages
import tkinter as tk
from tkinter import messagebox
import mysql.connector as sql

#creating function to insert data
def insert_details():

    #checking empty entry fileds
    if any([not entry.get() for entry in(Dcode_entry,Dname_entry,Dlocation_entry)]):
        messagebox.showerror("Error","All Fields Are Mandatory")
        return

    #connecting to database
    db_connection=sql.connect(host='localhost',database='ems',user='root',password='')
    db_cursor=db_connection.cursor()

    #getting data from entrybox
    Dcode=Dcode_entry.get()
    Dname=Dname_entry.get()
    Dlocation=Dlocation_entry.get()

    #query
    db_cursor.execute("insert into empdept_det(Dcode,Dname,Dlocation)values(%s,%s,%s)",[str(Dcode),str(Dname),str(Dlocation)])
    db_connection.commit()
    db_connection.close()

    messagebox.showinfo("Department Details","Data Inserted Successfully!")

    clear_details()

#creating function to clear entered data
def clear_details():
    Dcode_entry.delete(0, tk.END)
    Dname_entry.delete(0, tk.END)
    Dlocation_entry.delete(0, tk.END)

#creating mainwindow
window=tk.Tk()
window.title("Employee Management System")
window.geometry("800x400+300+0")

head=tk.Label(window,text="Insert Department details",font='sans 80 bold',bg='green',fg='white')
head.grid(row=0,columnspan=3,padx=20,pady=10)

Dcode=tk.Label(window,text="Dept Code:",width=20,bg='orange',font='sans 30 bold',fg='black')
Dcode.grid(row=1,column=0)
Dcode_entry=tk.Entry(window,font='sans 30 bold')
Dcode_entry.grid(row=1,column=1)

Dname=tk.Label(window,text="Dept Name:",width=20,bg='orange',font='sans 30 bold',fg='black')
Dname.grid(row=2,column=0)
Dname_entry=tk.Entry(window,font='sans 30 bold')
Dname_entry.grid(row=2,column=1)

Dlocation=tk.Label(window,text="Dept Location:",width=20,bg='orange',font='sans 30 bold',fg='black')
Dlocation.grid(row=3,column=0)
Dlocation_entry=tk.Entry(window,font='sans 30 bold')
Dlocation_entry.grid(row=3,column=1)

insert_button=tk.Button(window,text="Insert Details",font='sans 30 bold',command=insert_details)
insert_button.grid(row=4,column=0)

cancel_button=tk.Button(window,text="Cancel",font='sans 30 bold',bg='silver',fg='red',command=window.destroy)
cancel_button.grid(row=4,column=1,pady=10)

lbl=tk.Label(window,text='Employee Management System',font='sans 80 bold ', bg='skyblue')
lbl.grid(row=8,column=0,columnspan=4,sticky='nsew',padx=10,pady=10)

window.mainloop()
