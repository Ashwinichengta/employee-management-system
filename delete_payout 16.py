# program to delete employee salary details
#importing packages
import tkinter as tk
import mysql.connector as sql
from tkinter import messagebox

#creating function to search employee details()
def search_details():

    #connecting to database
    db_connection=sql.connect(host='localhost',database='ems',user='root',password='')
    db_cursor=db_connection.cursor()

    #getting values from entry box
    Ecode=Ecode_entry.get()

    #query
    db_cursor.execute("select * from employee_sal where Ecode=%s",[str(Ecode)])
    result=db_cursor.fetchone()

    if result:
        Ename_entry.delete(0, tk.END)
        Ename_entry.insert(tk.END, result[1])

        Dcode_entry.delete(0, tk.END)
        Dcode_entry.insert(tk.END, result[2])

        Basic_entry.delete(0, tk.END)
        Basic_entry.insert(tk.END, result[3])
    else:
        messagebox.showerror("Error","Employee Not Found")

    db_connection.close()

#creating function to delete data
def delete_details():

    #connecting to database
    db_connection=sql.connect(host='localhost',database='ems',user='root',password='')
    db_cursor=db_connection.cursor()

    #getting data from entry box
    Ecode=Ecode_entry.get()
    
    #query
    db_cursor.execute("delete from employee_sal where Ecode=%s",[str(Ecode)])

    db_connection.commit()
    db_connection.close()
    clear_details()

    messagebox.showinfo("Employee Salary Details","Data Deleted Successfully.")

#creating function to clear details
def clear_details():
    Ecode_entry.delete(0, tk.END)
    Ename_entry.delete(0, tk.END)
    Dcode_entry.delete(0, tk.END)
    Basic_entry.delete(0, tk.END)

#creating function to calculate
def calculate():

    #connecting to database
    db_connection=sql.connect(host='localhost',database='ems',user='root',password='')
    db_cusor=db_connection.cursor()

    #getting data from entry box
    Basic=float(Basic_entry.get())

    if Basic>50000:
        HRA=int(2000)
        res1=[str(HRA)]
        res1=tk.Label(window,text=res1).grid(row=5,column=1)

        PF=Basic*(12/100)
        res2=[str(PF)]
        res2=tk.Label(window,text=res2).grid(row=6,column=1)
    else:
        HRA=int(1000)
        res3=[str(HRA)]
        res3=tk.Label(window,text=res3).grid(row=5,column=1)

        PF=Basic*(8/100)
        res4=[str(PF)]
        res4=tk.Label(window,text=res4).grid(row=6,column=1)

    Net_salary=float(Basic)+int(HRA)-int(PF)
    res5=[str(Net_salary)]
    res5=tk.Label(window,text=res5).grid(row=7,column=1)

#creating mainwindow
window=tk.Tk()
window.title("Employee Management System")
window.geometry("800x400+300+200")

head=tk.Label(window,text="Delete Employee Salary Details",font='sans 80 bold',bg='green',fg='white')
head.grid(row=0,columnspan=5,padx=20,pady=10)

Ecode=tk.Label(window,text="Ecode:",font='sans 20 bold',fg='black')
Ecode.grid(row=1,column=0)
Ecode_entry=tk.Entry(window,font='sans 20 bold')
Ecode_entry.grid(row=1,column=1)

search_button=tk.Button(window,text="Search",font='sans 20 bold',fg='black',command=search_details)
search_button.grid(row=1,column=2)

Ename=tk.Label(window,text="Ename :",font='sans 20 bold',fg='black')
Ename.grid(row=2,column=0)
Ename_entry=tk.Entry(window,font='sans 20 bold')
Ename_entry.grid(row=2,column=1)

Dcode=tk.Label(window,text="Dcode :",font='sans 20 bold',fg='black')
Dcode.grid(row=3,column=0)
Dcode_entry=tk.Entry(window,font='sans 20 bold')
Dcode_entry.grid(row=3,column=1)

Basic=tk.Label(window,text="Basic :",font='sans 20 bold',fg='black')
Basic.grid(row=4,column=0)
Basic_entry=tk.Entry(window,font='sans 20 bold')
Basic_entry.grid(row=4,column=1)

HRA=tk.Label(window,text="HRA :",font='sans 20 bold',fg='black')
HRA.grid(row=5,column=0)

PF=tk.Label(window,text="PF :",font='sans 20 bold',fg='black')
PF.grid(row=6,column=0)

Net_salary=tk.Label(window,text="Net Salary :",font='sans 20 bold',fg='black')
Net_salary.grid(row=7,column=0)

cal=tk.Button(window,text="Calculate",font='sans 20 bold',fg='black',command=calculate)
cal.grid(row=8,column=0)


insert_button=tk.Button(window,text="Delete",font='sans 20 bold',fg='black',command=delete_details)
insert_button.grid(row=8,column=1)

cancel_button=tk.Button(window,text="Cancel",font='sans 20 bold',fg='black',bg='silver',command=window.destroy)
cancel_button.grid(row=8,column=3,columnspan=4,sticky='w',pady=10)
lbl=tk.Label(window,text='Employee Management System',font='sans 80 bold ', bg='skyblue')
lbl.grid(row=9,column=0,columnspan=4,sticky='nsew',padx=10,pady=10)



window.mainloop()
        
