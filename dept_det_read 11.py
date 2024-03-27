# program to read department details - Python
#importing packages
import tkinter as tk
from tkinter import ttk
import mysql.connector as sql

#creating function to fetch data
def fetch_data():
    #connecting to database
    db_connection=sql.connect(host='localhost',database='ems',user='root',password='')
    db_cursor=db_connection.cursor()

    #query
    db_cursor.execute("select * from empdept_det")
    data=db_cursor.fetchall()
    db_connection.close()
    return data

#creating function to display fetched data
def display_data():
    data=fetch_data()

    for row in tree.get_children():
        tree.delete(row)

    #inserting into treeview
    for record in data:
        tree.insert("","end",value=record)

#creating mainwindow
window=tk.Tk()
window.title("Employee Management Details")

#creating TreeView for displaying data
column=("Dcode","Dname","Dlocation")
tree=ttk.Treeview(window,column=column,show="headings")

#set up column headings
for col in column:
    tree.heading(col,text=col)

head=ttk.Label(window,text="Department Read Details",font='sans 80 bold')
head.grid(row=0,column=0,padx=10,pady=10)

tree.grid(row=1,column=0,padx=10,pady=10)

show_button=ttk.Button(window,width=20,text="Show Details",command=display_data)
show_button.grid(row=2,column=0,pady=10)

lbl=tk.Label(window,text='Employee Management System',font='sans 80 bold ', bg='skyblue')
lbl.grid(row=8,column=0,columnspan=4,sticky='nsew',padx=10,pady=10)

window.mainloop()
