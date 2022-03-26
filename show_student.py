import email
import os
from tkinter import messagebox
from turtle import width
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

        self.dob = DateEntry(self.root, selectmode="day",state="readonly",date_pattern = 'dd/mm/yyyy',background="blue",Cursor="hand1",year=2003, month=1, foreground='black', font=("Times new roman", 13))
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

        self.branch = ttk.Combobox(self.root, text="branch", font=("times new roman",13), state="readonly", justify=CENTER)
        self.branch['values'] = ("Select","Information Technology")
        self.branch.place(x=160, y=450, width=150, height=30)
        self.branch.current(0)

        self.sem = ttk.Combobox(self.root, text="semester", font=("times new roman",13), state="readonly", justify=CENTER)
        self.sem['values'] = ("Select","sem 1", "sem 2", "sem 3", "sem 4", "sem 5", "sem 6", "sem 7", "sem 8")
        self.sem.place(x=430, y=450, width=150, height=30)
        self.sem.current(0)


# --------------buttons
        Button(self.root, text="search",cursor="hand2",bg="#1ab402",fg="black" ,bd=0, font=("times new roman",13)).place(x=450, y=120)
        Button(self.root, text="Update",cursor="hand2",bg="#1ab402",fg="black" ,bd=0, font=("times new roman",15)).place(x=300, y=600, width=80)
        Button(self.root, text="Delete",cursor="hand2",bg="aqua",fg="black" ,bd=0, font=("times new roman",15)).place(x=400, y=600, width=80)
        Button(self.root, text="clear",cursor="hand2",bg="yellow",fg="black" ,bd=0, font=("times new roman",15)).place(x=500, y=600, width=80)


    
if __name__ == "__main__":
    root=Tk()
    obj = add_student(root)
    root.mainloop()