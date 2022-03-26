import os
from tkinter import messagebox
import mysql.connector as sql
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

# ----------------------Connection with database
mydb = sql.connect(host="localhost", user="root", passwd="", database="SP")
mycursor = mydb.cursor()


class add_student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Details")
        self.root.geometry("1200x750+150+30") 
        self.root.resizable(False, False)
        self.root.config(bg="#d1e2f4")
        self.root.focus_force()

# ---------------title
        title = Label(self.root, text="Student Details", font=("goudy old style",20,"bold"), fg="white", bg="#033054").place(x=30, y=10,width= 1140, height=50)

# ---------------labels
        stu_gr = Label(self.root, text="GR No.", font=("goudy old style",15) ,fg="black", bg="#d1e2f4").place(x=50, y=120)
        name = Label(self.root, text="Name", font=("goudy old style",15) ,fg="black", bg="#d1e2f4").place(x=50, y=200)
        Roll_no = Label(self.root, text="Roll No.", font=("goudy old style",15) ,fg="black", bg="#d1e2f4").place(x=50, y=250)
        DOB = Label(self.root, text="DOB", font=("goudy old style",15) ,fg="black", bg="#d1e2f4").place(x=350, y=250)
        phone_no = Label(self.root, text="Phone No.", font=("goudy old style",15) ,fg="black", bg="#d1e2f4").place(x=50, y=300)
        email = Label(self.root, text="Email", font=("goudy old style",15) ,fg="black", bg="#d1e2f4").place(x=350, y=300)
        Xth = Label(self.root, text="Xth", font=("goudy old style",15) ,fg="black", bg="#d1e2f4").place(x=50, y=350)
        XIIth = Label(self.root, text="XIIth", font=("goudy old style",15) ,fg="black", bg="#d1e2f4").place(x=350, y=350)
        address = Label(self.root, text="Address", font=("goudy old style",15) ,fg="black", bg="#d1e2f4").place(x=50, y=400)
        branch = Label(self.root, text="Branch", font=("goudy old style",15) ,fg="black", bg="#d1e2f4").place(x=50, y=450)
        sem = Label(self.root, text="Semester", font=("goudy old style",15) ,fg="black", bg="#d1e2f4").place(x=350, y=450)

# --------------entry
        self.gr_no = Entry(self.root, font=("times new roman", 13), bg ="white")
        self.gr_no.place(x=150, y=120, width=250, height=30)

        self.name = Entry(self.root, font=("times new roman", 13), bg ="white")
        self.name.place(x=160, y=200, width=300, height=30)
       
        self.roll_no = Entry(self.root, font=("times new roman", 13), bg ="white")
        self.roll_no.place(x=160, y=250, width=150, height=30)

        self.dob = DateEntry(self.root, selectmode="day",date_pattern = 'dd/mm/yyyy',background="blue",Cursor="hand1",year=2003, month=1, foreground='black', font=("Times new roman", 13))
        self.dob.place(x=420, y=250, width=150, height=30)  

        self.phone_no = Entry(self.root, font=("times new roman", 13), bg ="white")
        self.phone_no.place(x=160, y=300, width=150, height=30)

        self.email = Entry(self.root, font=("times new roman", 13), bg ="white")
        self.email.place(x=420, y=300, width=150, height=30)

        self.xth = Entry(self.root, font=("times new roman", 13), bg ="white")
        self.xth.place(x=160, y=350, width=150, height=30)

        self.xiith = Entry(self.root, font=("times new roman", 13), bg ="white")
        self.xiith.place(x=420, y=350, width=150, height=30)

        self.address = Entry(self.root, font=("times new roman", 13), bg ="white")
        self.address.place(x=160, y=400, width=300, height=30)

        self.branch = ttk.Combobox(self.root, text="branch", font=("times new roman",13), justify=CENTER)
        self.branch['values'] = ("Select","Information Technology")
        self.branch.place(x=160, y=450, width=150, height=30)
        self.branch.current(0)

        self.sem = ttk.Combobox(self.root, text="semester", font=("times new roman",13), justify=CENTER)
        self.sem['values'] = ("Select","sem 1", "sem 2", "sem 3", "sem 4", "sem 5", "sem 6", "sem 7", "sem 8")
        self.sem.place(x=430, y=450, width=150, height=30)
        self.sem.current(0)


# -----------Frame for displaying student table
        self.Frame = Frame(self.root, bd = 2, relief=RIDGE)
        self.Frame.place(x=620, y=150, width=550, height=500)

# --------------table
        scrollx = Scrollbar(self.Frame, orient=HORIZONTAL)
        scrolly = Scrollbar(self.Frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(self.Frame,xscrollcommand=scrollx.set, yscrollcommand=scrolly.set, columns=("Gr No.", "Name", "DOB", "Email", "Phone No.", "Xth", "XIIth", "Address", "Semester","Branch"))
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.student_table.xview)
        scrolly.config(command=self.student_table.yview)
        self.student_table.heading("Gr No.", text="Gr No.")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone No.", text="Phone No.")
        self.student_table.heading("Xth", text="Xth")
        self.student_table.heading("XIIth", text="XIIth")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("Branch", text="Branch")
        self.student_table["show"] = 'headings'
        self.student_table.column("Gr No.", width=40)
        self.student_table.column("Name", width=150)
        self.student_table.column("DOB", width=70)
        self.student_table.column("Email", width=150)
        self.student_table.column("Phone No.", width=80)
        self.student_table.column("Xth", width=50)
        self.student_table.column("XIIth", width=50)
        self.student_table.column("Address", width=150)
        self.student_table.column("Semester", width=80)
        self.student_table.column("Branch", width=150)
        self.student_table.pack(fill=BOTH, expand=1)

# --------------buttons
        Button(self.root,command=self.search,text="search",cursor="hand2",bg="#2196f3",fg="white" ,bd=0, font=("goudy old style",13, "bold"),borderwidth=2).place(x=450, y=120)
        Button(self.root,command=self.update,text="Update",cursor="hand2",bg="#4caf50",fg="white" ,bd=0, font=("goudy old style",15, "bold"),borderwidth=2).place(x=300, y=600, width=80)
        Button(self.root,command=self.clear,text="Clear",cursor="hand2",bg="#f44336",fg="white" ,bd=0, font=("goudy old style",15, "bold"),borderwidth=2).place(x=400, y=600, width=80)
        Button(self.root,command=self.back,text="Back",cursor="hand2",bg="#607d8b",fg="white" ,bd=0, font=("goudy old style",15, "bold"),borderwidth=2).place(x=500, y=600, width=80)
        self.show()
# --------------fucntions of buttons

    def search(self):
            self.get_gr_no = self.gr_no.get()
            try:
                if self.gr_no.get() == "":
                        messagebox.showerror("Error", "Enter Gr No.")
                else:
                        sql_query1 = "SELECT * FROM students where gr_no = %s"
                        mycursor.execute(sql_query1, [int(self.get_gr_no)])
                        result = mycursor.fetchone()
                        if(result == None):
                                messagebox.showerror("Error", "Invalid Gr No.")
                        else:
                                self.name.insert(0, result[1])
                                self.dob.delete(0, 'end')
                                self.dob.insert(0, result[2])
                                self.email.insert(0, result[3])
                                self.phone_no.insert(0, result[4])
                                self.xth.insert(0, result[5])
                                self.xiith.insert(0, result[6])
                                self.address.insert(0, result[7])
                                self.sem.delete(0, 'end')
                                self.sem.insert(0, result[8])
                                self.branch.delete(0, 'end')
                                self.branch.insert(0, result[9])
                                self.pre_sem = result[8]
                                sql_query2 = f"SELECT roll_no FROM sem{self.pre_sem[-1]}_students where name = %s"
                                mycursor.execute(sql_query2, [result[1]])
                                result1 = mycursor.fetchone()
                                self.roll_no.insert(0, result1[0])
                self.show()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}")
    
    def show(self):
            try:
                sql_query1 = "SELECT * FROM students"
                mycursor.execute(sql_query1)
                result = mycursor.fetchall()
                self.student_table.delete(*self.student_table.get_children())
                for row in result:
                        self.student_table.insert('',END, values=row)
                        
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}")


    def update(self):
            self.updated_name = self.name.get()
            self.updated_roll_no = self.roll_no.get()
            self.updated_dob = self.dob.get()
            self.updated_phone_no = self.phone_no.get()
            self.updated_email = self.email.get()
            self.updated_xth = self.xth.get()
            self.updated_xiith = self.xiith.get()
            self.updated_address = self.address.get()
            self.updated_branch = self.branch.get()
            self.updated_sem = self.sem.get()
            
            query1 = "UPDATE students SET name = %s, DOB = %s, email = %s, phone_no = %s, Xth = %s, XIIth = %s, address = %s, sem = %s, branch = %s WHERE gr_no = %s"
            mycursor.execute(query1, [self.updated_name, self.updated_dob, self.updated_email, self.updated_phone_no, self.updated_xth, self.updated_xiith, self.updated_address, self.updated_sem, self.updated_branch, self.get_gr_no])
           
            if(self.pre_sem != self.updated_sem):
                query2 = f"DELETE FROM sem{self.pre_sem[-1]}_students WHERE name = %s OR DOB = %s OR email = %s OR phone_no = %s"
                query3 = f"INSERT INTO sem{self.updated_sem[-1]}_students(roll_no, name, DOB, email, phone_no, Xth, XIIth, address, branch) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                mycursor.execute(query2, [self.updated_name, self.updated_dob, self.updated_email, self.updated_phone_no])
                mycursor.execute(query3, [int(self.updated_roll_no), self.updated_name, self.updated_dob, self.updated_email, self.updated_phone_no, self.updated_xth, self.updated_xiith, self.updated_address, self.updated_branch])
            else:
                query4 = f"UPDATE sem{self.updated_sem[-1]}_students SET  roll_no=%s, name = %s, DOB = %s, email = %s, phone_no = %s, Xth = %s, XIIth = %s, address = %s, branch = %s WHERE name = %s OR DOB = %s OR email = %s OR phone_no = %s "
                mycursor.execute(query4, [int(self.updated_roll_no), self.updated_name, self.updated_dob, self.updated_email, self.updated_phone_no, self.updated_xth, self.updated_xiith, self.updated_address, self.updated_branch, self.updated_name, self.updated_dob, self.updated_email, self.updated_phone_no])
            self.show()
            mydb.commit()
            messagebox.showinfo("showinfo", f"Dara Updated")

    def back(self):
            self.root.destroy()
            os.system("python main_page.py")
    def clear(self):
            self.name.delete(0,'end')
        #     self.name.insert(0, '')
            self.dob.delete(0, 'end')
            self.dob.delete(0, 'end')
            self.email.delete(0, 'end')
            self.phone_no.delete(0, 'end')
            self.xth.delete(0, 'end')
            self.xiith.delete(0, 'end')
            self.address.delete(0, 'end')
            self.sem.delete(0, 'end')
            self.sem.current(0)
            self.branch.delete(0, 'end')
            self.branch.current(0)
            self.roll_no.delete(0, 'end')
        
            
    
if __name__ == "__main__":
    root=Tk()
    obj = add_student(root)
    root.mainloop()