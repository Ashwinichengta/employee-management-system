import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import time

class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Employee Project Dashboard")
        self.geometry("600x400")

        #Load and display image
        self.load_image("emp.PNG")

        #create menu
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        #Create employee details CRUD menu
        self.emp_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Employee Details",menu=self.emp_menu)
        self.emp_menu.add_command(label="Insert Employee",command=self.open_insert_emp_det)
        self.emp_menu.add_command(label="Update Employee",command=self.open_update_emp_det)
        self.emp_menu.add_command(label="Delete Employee",command=self.open_delete_emp_det)
        self.emp_menu.add_command(label="All Employee Details",command=self.open_read_emp_det)
        self.emp_menu.add_separator()
        self.emp_menu.add_command(label="Exit",command=self.destroy)

        #creating leave details CRUD menu
        self.leave_menu=tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Leave Details",menu=self.leave_menu)
        self.leave_menu.add_command(label="Insert Leave",command=self.open_insert_leave_det)
        self.leave_menu.add_command(label="Update Leave",command=self.open_update_leave_det)
        self.leave_menu.add_command(label="Delete Leave",command=self.open_delete_leave_det)
        self.leave_menu.add_command(label="All Leave Details",command=self.open_read_leave_det)
        self.leave_menu.add_separator()
        self.leave_menu.add_command(label="Exit",command=self.destroy)

        #creating department details CRUD menu
        self.dept_menu=tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Department Details",menu=self.dept_menu)
        self.dept_menu.add_command(label="Insert Department",command=self.open_insert_dept_det)
        self.dept_menu.add_command(label="Update Department",command=self.open_update_dept_det)
        self.dept_menu.add_command(label="Delete Department",command=self.open_delete_dept_det)
        self.dept_menu.add_command(label="All Departments",command=self.open_read_dept_det)
        self.dept_menu.add_separator()
        self.dept_menu.add_command(label="Exit",command=self.destroy)

        #creating salary details menu
        self.sal_menu=tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Salary Details",menu=self.sal_menu)
        self.sal_menu.add_command(label="Insert Salary ",command=self.open_insert_emp_sal)
        self.sal_menu.add_command(label="Update Salary",command=self.open_update_emp_sal)
        self.sal_menu.add_command(label="Delete Salary",command=self.open_delete_emp_sal)
        self.sal_menu.add_command(label="All Employee Salary",command=self.open_read_emp_sal)
        self.sal_menu.add_separator()
        self.sal_menu.add_command(label="Exit",command=self.destroy)

    def load_image(self, image_path):
        image=Image.open(image_path)
        image=image.resize((800,500))
        self.dashboard_image=ImageTk.PhotoImage(image)
        self.image_label=tk.Label(self,image=self.dashboard_image)
        hd=tk.Label(self, text="Employee Management Application",bg='orange',fg='green',font=('sans bold',16)).pack(fill="both")
        self.image_label.pack()
        sd=tk.Label(self, text='Developed by ASHWINI R CHENGTA',bg='green',fg='white',font=('sans bold',16)).pack(fill="both")

        #show time
        self.time_label=tk.Label(self,text="", font=("Helvetica",12), bg='yellow')
        self.time_label.pack(pady=10,side="right")
        self.update_time()

    def update_time(self):
        current_time=time.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.after(1000,self.update_time)

    #Employee Details
    def open_insert_emp_det(self):
      
        import insert_emp_det as IED

    def open_update_emp_det(self):
       
        import update_emp_det_TEST as UED

    def open_delete_emp_det(self):
       
        import delete_emp_det as DED

    def open_read_emp_det(self):
       
        import read_emp_det as RED

    #Leave Details
    def open_insert_leave_det(self):
        
        import insert_leave_det as ILD

    def open_update_leave_det(self):
        
        import update_leave_det as ULD

    def open_delete_leave_det(self):
        #os.system("delete_leave_det.py")
        import delete_leave_det as DLD

    def open_read_leave_det(self):
        
        import read_leave_det as RLD

    #Department Details
    def open_insert_dept_det(self):
      
        import insert_dept_det as IDD

    def open_update_dept_det(self):
       
        import update_dept_det as UDD

    def open_delete_dept_det(self):
       
        import delete_dept_det as DDD

    def open_read_dept_det(self):
      
        import read_dept_det as RDD

    #Salry Details
    def open_insert_emp_sal(self):

        import insert_emp_sal as IES

    def open_update_emp_sal(self):
        
        import update_emp_sal as UES

    def open_delete_emp_sal(self):
     
        import delete_emp_sal as DES

    def open_read_emp_sal(self):
       
        import read_emp_sal as RES

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()
