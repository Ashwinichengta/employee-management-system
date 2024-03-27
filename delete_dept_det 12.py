# program to delete department details
#importing packages
import tkinter as tk
from tkinter import messagebox
import mysql.connector as sql

#creating function to search details
def search_details():

    #connecting to database
    db_connection=sql.connect(host='localhost',database='ems',user='root',password='')
    db_cursor=db_connection.cursor()

    #getting data from entrybox
    Dcode=Dcode_entry.get()

    #query
    db_cursor.execute("select * from empdept_det where Dcode=%s",[str(Dcode)])
    result=db_cursor.fetchone()

    if result:
        Dname_entry.delete(0, tk.END)
        Dname_entry.insert(tk.END, result[1])

        Dlocation_entry.delete(0, tk.END)
        Dlocation_entry.insert(tk.END, result[2])
    else:
        messagebox.showerror("Error","Department Code Not Found")

    db_connection.close()

#creating function to
def delete_details():

    #checking empty data
    if any([not entry.get() for entry in(Dcode_entry,Dlocation_entry)]):
        messagebox.showerror("Error","All Fields Are Mandatory")
        return

    #connecting to database
    db_connection=sql.connect(host='localhost',database='ems',user='root',password='')
    db_cursor=db_connection.cursor()

    #getting data from entry box
    Dcode=Dcode_entry.get()

    #query
    db_cursor.execute("delete from empdept_det where Dcode=%s",[str(Dcode)])
    db_connection.commit()
    db_connection.close()

    clear_details()

    messagebox.showinfo("Department Details","Data Deleted Successfully!")

#creating function to clear details
def clear_details():
    Dcode_entry.delete(0, tk.END)
    Dname_entry.delete(0, tk.END)
    Dlocation_entry.delete(0, tk.END)

#creating mainwindow
window=tk.Tk()
window.title("Employee Management Details")
window.geometry("800x400+300+200")

head=tk.Label(window,text="Delete Department Details",font='sans 80 bold',bg='green',fg='white')
head.grid(row=0,columnspan=5,padx=20,pady=10)

Dcode=tk.Label(window,text="Department Code:",width=20,bg='orange',font='sans 30 bold',fg='black')
Dcode.grid(row=1,column=0)
Dcode_entry=tk.Entry(window,font='sans 30 bold')
Dcode_entry.grid(row=1,column=1)

search_button=tk.Button(window,text="Search",font='sans 15 bold',command=search_details)
search_button.grid(row=1,column=2)

Dname=tk.Label(window,text="Department Name:",width=20,bg='orange',font='sans 30 bold',fg='black')
Dname.grid(row=2,column=0)
Dname_entry=tk.Entry(window,font='sans 30 bold')
Dname_entry.grid(row=2,column=1)

Dlocation=tk.Label(window,text="Department Location",width=20,bg='orange',font='sans 30 bold',fg='black')
Dlocation.grid(row=3,column=0)
Dlocation_entry=tk.Entry(window,font='sans 30 bold')
Dlocation_entry.grid(row=3,column=1)

delete_button=tk.Button(window,text="Delete",font='sans 30 bold',command=delete_details)
delete_button.grid(row=4,column=0)

cancel_button=tk.Button(window,text="Cancel",font='sans 30 bold',bg='silver',fg='red',command=window.destroy)
cancel_button.grid(row=4,column=1,columnspan=4,sticky='w',pady=10)

lbl=tk.Label(window,text='Employee Management System',font='sans 80 bold ', bg='skyblue')
lbl.grid(row=8,column=0,columnspan=4,sticky='nsew',padx=10,pady=10)


window.mainloop()
