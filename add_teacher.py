import os
from tkinter import messagebox
from click import command
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
        self.root.title("Add teacher")
        self.root.geometry("900x730+350+50") 
        self.root.resizable(False, False)
        self.root.config(bg="#d1e2f4")

# --------------------queries
        sql = "select count(*) from teachers"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        form_no = result[0][0] + 1 

        print((form_no))
        

# --------------------- title
        title = Label(self.root, text="Add Teacher", font=("Impact",30,"bold"), fg="#167303", bg="#d1e2f4").place(x=90, y=50)

# --------------------- another Frame
        Frame_student = Frame(self.root, bg="light blue")
        Frame_student.config(bg="#d1e2f4")
        Frame_student.place(x=50, y=120, height=500, width=800)

# --------------------row 1
        name = Label(Frame_student, text="Name", font=("times new roman",15), fg="black", bg="#d1e2f4").place(x=30, y=30)
        self.name = Entry(Frame_student, font=("times new roman", 15), bg ="white")
        self.name.place(x=30, y=60, width=300, height=30)

        teacher_gr = Label(Frame_student, text="SR No.", font=("times new roman",15) ,fg="black", bg="#d1e2f4").place(x=450, y=30)
        self.teacher_gr = Entry(Frame_student,font=("times new roman", 15),justify=CENTER ,bg="white")
        self.teacher_gr.insert(END, form_no)
        self.teacher_gr.config(state="readonly")
        self.teacher_gr.place(x=450, y=60, width=300, height=30)

# --------------------row 2
        
        DOB = Label(Frame_student, text="DOB", font=("times new roman",15), fg="black", bg="#d1e2f4").place(x=30, y=120)
        # self.DOB = Entry(Frame_student, font=("times new roman", 15), bg="white")
        self.DOB = DateEntry(Frame_student, selectmode="day",background="blue",date_pattern = 'dd/mm/yyyy',Cursor="hand1",year=2003, month=1, foreground='black', font=("Arial", 12))
        self.DOB.place(x=30, y=150, width=300, height=30)


        email = Label(Frame_student, text="Email", font=("times new roman",15), fg="black", bg="#d1e2f4").place(x=450, y=120)
        self.email = Entry(Frame_student, font=("times new roman", 15), bg="white")
        self.email.place(x=450, y=150, width=300, height=30)
        
# --------------------row 3
        phone_no = Label(Frame_student, text="Phone No.", font=("times new roman",15), fg="black", bg="#d1e2f4").place(x=30, y=220)
        self.phone_no = Entry(Frame_student, font=("times new roman", 15), bg="white")
        self.phone_no.place(x=30, y=250, width=300, height=30)

        aadhar_no = Label(Frame_student, text="Aadhar No.", font=("times new roman",15), fg="black", bg="#d1e2f4").place(x=450, y=220)
        self.aadhar_no = Entry(Frame_student, font=("times new roman", 15), bg="white")
        self.aadhar_no.place(x=450, y=250, width=300, height=30)

        
# --------------------row 4
        gender = Label(Frame_student, text="Gender", font=("times new roman",15), fg="black", bg="#d1e2f4").place(x=30, y=320)
        # self.Gender = Entry(Frame_student, font=("times new roman", 15), bg="white")
        self.gender = ttk.Combobox(Frame_student, font=("times new roman", 15),state="readonly", justify=CENTER)
        self.gender['values'] = ("Select","Male","Female")
        self.gender.place(x=30, y=350, width=300, height=30)
        self.gender.current(0)
        
        address = Label(Frame_student, text="Address", font=("times new roman",15), fg="black", bg="#d1e2f4").place(x=450, y=320)
        self.address = Entry(Frame_student, font=("times new roman", 15), bg="white")
        self.address.place(x=450, y=350, width=300, height=30)
        
# --------------------row 5
        branch = Label(Frame_student, text="branch", font=("times new roman",15), fg="black", bg="#d1e2f4").place(x=30, y=420)
        self.branch = ttk.Combobox(Frame_student, font=("times new roman", 15),state="readonly", justify=CENTER)
        self.branch['values'] = ("Select","Informatin Technology")
        self.branch.place(x=30, y=450, width=300, height=30)
        self.branch.current(0)

        # sem = Label(Frame_student, text="Semester", font=("times new roman",15), fg="black", bg="#d1e2f4").place(x=450, y=420)
        # self.sem = ttk.Combobox(Frame_student, text="semester", font=("times new roman",15), state="readonly", justify=CENTER)
        # self.sem['values'] = ("Select","sem 1", "sem 2", "sem 3", "sem 4", "sem 5", "sem 6", "sem 7", "sem 8")
        # self.sem.place(x=450, y=450, width=300, height=30)
        # self.sem.current(0)


# --------------------Button
        Button(self.root, text="Submit",command=self.submit,cursor="hand2",bg="#1ab402",fg="black" ,bd=0, font=("times new roman",18)).place(x=750, y=650)

    def submit(self):
# -----------------Getting all values
        self.get_name = self.name.get()
        self.get_DOB = self.DOB.get()
        self.get_teacher_gr = self.teacher_gr.get()
        self.get_email = self.email.get()
        self.get_phone_no = self.phone_no.get()
        self.get_aadhar_no = self.aadhar_no.get()
        self.get_address = self.address.get()
        self.get_branch = self.branch.get()
        self.get_gender = self.gender.get()

        if(self.get_name=="" or self.get_teacher_gr=="" or self.get_DOB=="" or self.get_email=="" or self.get_phone_no=="" or self.get_aadhar_no=="" or self.get_address=="" or self.get_branch=="Select" or self.get_gender=="Select"):
                messagebox.showerror("showerror", "All field must be required!")
        else:
                sql1 = "INSERT INTO teachers(name, DOB, email, phone_no, aadhar_no, gender, address, branch) values(%s, %s, %s, %s, %s, %s, %s, %s)"
                mycursor.execute(sql1, [self.get_name, self.get_DOB, self.get_email, self.get_phone_no, self.get_aadhar_no,self.get_gender, self.get_address, self.get_branch])
                messagebox.showinfo("showinfo", "Data Inserted sucessfully.")
                mydb.commit()
# --------------destorying the frame
                self.root.destroy()
                os.system("python main_page.py")

        

    
if __name__ == "__main__":
    root=Tk()
    obj = add_student(root)
    root.mainloop()