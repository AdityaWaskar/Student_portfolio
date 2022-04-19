import os
from tkinter import messagebox
import mysql.connector as sql
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

# ----------------------Connection with database
mydb = sql.connect(host="localhost", user="root", passwd="", database="SP")
mycursor = mydb.cursor()


class show_teacher:
    def __init__(self, root):
        self.root = root
        self.root.title("Teacher Details")
        self.root.geometry("1200x750+150+30") 
        self.root.resizable(False, False)
        self.root.config(bg="#d1e2f4")
        self.root.focus_force()

# ---------------title
        title = Label(self.root, text="Student Details", font=("goudy old style",20,"bold"), fg="white", bg="#033054").place(x=30, y=10,width= 1140, height=50)

# ---------------labels
        teacher_gr = Label(self.root, text="GR No.", font=("goudy old style",15) ,fg="black", bg="#d1e2f4").place(x=50, y=120)
        name = Label(self.root, text="Name", font=("goudy old style",15) ,fg="black", bg="#d1e2f4").place(x=50, y=240)
        DOB = Label(self.root, text="DOB", font=("goudy old style",15) ,fg="black", bg="#d1e2f4").place(x=50, y=300)
        email = Label(self.root, text="Email", font=("goudy old style",15) ,fg="black", bg="#d1e2f4").place(x=350, y=300)
        phone_no = Label(self.root, text="Phone No.", font=("goudy old style",15) ,fg="black", bg="#d1e2f4").place(x=50, y=360)
        gender = Label(self.root, text="Gender", font=("goudy old style",15) ,fg="black", bg="#d1e2f4").place(x=350, y=360)
        address = Label(self.root, text="Address", font=("goudy old style",15) ,fg="black", bg="#d1e2f4").place(x=50, y=420)
        aadhar_no = Label(self.root, text="Aaddhar No.", font=("goudy old style",15) ,fg="black", bg="#d1e2f4").place(x=50, y=480)
        branch = Label(self.root, text="Branch", font=("goudy old style",15) ,fg="black", bg="#d1e2f4").place(x=350, y=480)
        
# --------------entry
        self.teacher_gr = Entry(self.root, font=("times new roman", 13), bg ="white")
        self.teacher_gr.place(x=150, y=120, width=250, height=30)

        self.name = Entry(self.root, font=("times new roman", 13), bg ="white")
        self.name.place(x=160, y=240, width=300, height=30)
       
        self.dob = DateEntry(self.root, selectmode="day",date_pattern = 'dd/mm/yyyy',background="blue",Cursor="hand1",year=2003, month=1, foreground='black', font=("Times new roman", 13))
        self.dob.place(x=160, y=300, width=150, height=30)  

        self.email = Entry(self.root, font=("times new roman", 13), bg ="white")
        self.email.place(x=420, y=300, width=150, height=30)

        self.phone_no = Entry(self.root, font=("times new roman", 13), bg ="white")
        self.phone_no.place(x=160, y=360, width=150, height=30)

        self.gender = ttk.Combobox(self.root, text="branch", font=("times new roman",13), justify=CENTER)
        self.gender['values'] = ("Select","Male", "Female")
        self.gender.place(x=420, y=360, width=150, height=30)
        self.gender.current(0)

        self.address = Entry(self.root, font=("times new roman", 13), bg ="white")
        self.address.place(x=160, y=420, width=300, height=30)
        
        self.aadhar_no = Entry(self.root, font=("times new roman", 13), bg ="white")
        self.aadhar_no.place(x=160, y=480, width=150, height=30)

        self.branch = ttk.Combobox(self.root, text="Branch", font=("times new roman",13), justify=CENTER)
        self.branch['values'] = ("Select","Informaiton Technology")
        self.branch.place(x=420, y=480, width=150, height=30)
        self.branch.current(0)


# -----------Frame for displaying student table
        self.Frame = Frame(self.root, bd = 2, relief=RIDGE)
        self.Frame.place(x=620, y=150, width=550, height=500)

# --------------table
        scrollx = Scrollbar(self.Frame, orient=HORIZONTAL)
        scrolly = Scrollbar(self.Frame, orient=VERTICAL)
        self.teacher_table = ttk.Treeview(self.Frame,xscrollcommand=scrollx.set, yscrollcommand=scrolly.set, columns=("Sr No.", "Name", "DOB", "Email", "Phone No.", "Aadhar No.", "Gender", "Address","Branch"))
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.teacher_table.xview)
        scrolly.config(command=self.teacher_table.yview)
        self.teacher_table.heading("Sr No.", text="Sr No.")
        self.teacher_table.heading("Name", text="Name")
        self.teacher_table.heading("DOB", text="DOB")
        self.teacher_table.heading("Email", text="Email")
        self.teacher_table.heading("Phone No.", text="Phone No.")
        self.teacher_table.heading("Aadhar No.", text="Aadhar No.")
        self.teacher_table.heading("Gender", text="Gender")
        self.teacher_table.heading("Address", text="Address")
        self.teacher_table.heading("Branch", text="Branch")
        self.teacher_table["show"] = 'headings'
        self.teacher_table.column("Sr No.", width=40)
        self.teacher_table.column("Name", width=150)
        self.teacher_table.column("DOB", width=70)
        self.teacher_table.column("Email", width=150)
        self.teacher_table.column("Phone No.", width=80)
        self.teacher_table.column("Aadhar No.", width=80)
        self.teacher_table.column("Gender", width=50)
        self.teacher_table.column("Address", width=150)
        self.teacher_table.column("Branch", width=150)
        self.teacher_table.pack(fill=BOTH, expand=1)

# --------------buttons
        Button(self.root,command=self.search,text="search",cursor="hand2",bg="#2196f3",fg="white" ,bd=0, font=("goudy old style",13, "bold"),borderwidth=2).place(x=450, y=120)
        Button(self.root,command=self.update,text="Update",cursor="hand2",bg="#4caf50",fg="white" ,bd=0, font=("goudy old style",15, "bold"),borderwidth=2).place(x=300, y=600, width=80)
        Button(self.root,command=self.clear,text="Clear",cursor="hand2",bg="#f44336",fg="white" ,bd=0, font=("goudy old style",15, "bold"),borderwidth=2).place(x=400, y=600, width=80)
        Button(self.root,command=self.back,text="Back",cursor="hand2",bg="#607d8b",fg="white" ,bd=0, font=("goudy old style",15, "bold"),borderwidth=2).place(x=500, y=600, width=80)
        self.show()
# --------------fucntions of buttons

    def search(self):
            self.get_gr_no = self.teacher_gr.get()
            try:
                if self.teacher_gr.get() == "":
                        messagebox.showerror("Error", "Enter Sr No.",parent=self.root)
                else:
                        sql_query1 = "SELECT * FROM teachers where sr_no = %s"
                        mycursor.execute(sql_query1, [int(self.get_gr_no)])
                        result = mycursor.fetchone()
                        if(result == None):
                                messagebox.showerror("Error", "Invalid Sr No.",parent=self.root)
                        else:
                                self.name.delete(0, 'end')
                                self.name.insert(0, result[1])
                                self.dob.delete(0, 'end')
                                self.dob.insert(0, result[2])
                                self.email.delete(0, 'end')
                                self.email.insert(0, result[3])
                                self.phone_no.delete(0, 'end')
                                self.phone_no.insert(0, result[4])
                                self.aadhar_no.delete(0, 'end')
                                self.aadhar_no.insert(0, result[5])
                                self.gender.delete(0, 'end')
                                self.gender.insert(0, result[6])        
                                self.address.delete(0, 'end')
                                self.address.insert(0, result[7])
                                self.branch.delete(0, 'end')
                                self.branch.insert(0, result[8])
                                
                self.show()
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}",parent=self.root)
    
    def show(self):
            try:
                sql_query1 = "SELECT * FROM teachers"
                mycursor.execute(sql_query1)
                result = mycursor.fetchall()
                self.teacher_table.delete(*self.teacher_table.get_children())
                for row in result:
                        self.teacher_table.insert('',END, values=row)
                        
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}",parent=self.root)


    def update(self):
            self.updated_name = self.name.get()
            self.updated_dob = self.dob.get()
            self.updated_email = self.email.get()
            self.updated_phone_no = self.phone_no.get()
            self.updated_gender = self.gender.get()
            self.updated_address = self.address.get()
            self.updated_aadhar_no = self.aadhar_no.get()
            self.updated_branch = self.branch.get()
            
            query1 = "UPDATE teachers SET name = %s, DOB = %s, email = %s, phone_no = %s, aadhar_no = %s, gender = %s, address = %s, branch = %s WHERE sr_no = %s"
            mycursor.execute(query1, [self.updated_name, self.updated_dob, self.updated_email, self.updated_phone_no, self.updated_aadhar_no,self.updated_gender, self.updated_address, self.updated_branch, self.teacher_gr.get()])
            self.show()
            mydb.commit()
            messagebox.showinfo("showinfo", f"Data Updated",parent=self.root)

    def back(self):
            self.root.destroy()
            os.system("python main_page.py")
    def clear(self):
            self.name.delete(0,'end')
            self.dob.delete(0, 'end')
            self.dob.delete(0, 'end')
            self.email.delete(0, 'end')
            self.phone_no.delete(0, 'end')
            self.gender.delete(0, 'end')
            self.gender.current(0)
            self.address.delete(0, 'end')
            self.aadhar_no.delete(0, 'end')
            self.branch.delete(0, 'end')
            self.branch.current(0)
            
    
if __name__ == "__main__":
    root=Tk()
    obj = show_teacher(root)
    root.mainloop()