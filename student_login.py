from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import os
import mysql.connector as sql
from tkcalendar import *

mydb = sql.connect(host="localhost", user="root", passwd="", database="SP")
mycursor = mydb.cursor()

class student_Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Login Page")
        self.root.geometry("1199x600+150+100")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="images/bg1.jpg")
        self.root.focus_force()
        self.bg_img = Label(self.root, image=self.bg).place(x=0,y=0,relwidth=1, relheight=1)

        Frame_login = Frame(self.root, bg="White")
        Frame_login.place(x=150, y=150, height=340, width=500)
    # title
        title = Label(Frame_login, text="Login As", font=("Impact",35,"bold"), fg="skyblue", bg="white").place(x=90, y=30)
        # desc = Label(Frame_login, text="Account Employee Login Area", font=("Goudy old style",15,"bold"), fg="#d25d17", bg="white").place(x=90, y=100)

        Button(Frame_login, text="Teacher" ,cursor="hand2",command=self.teh_login,bg="white",bd=0,fg="black" , font=("times new roman",12)).place(x=100, y=100)
        Button(Frame_login, text="Student",cursor="hand2",bg="white",bd=1,fg="black", font=("times new roman",12)).place(x=270, y=100)
              
        lbl_user = Label(Frame_login, text="Email", font=("Goudy old style",15,"bold"), fg="grey", bg="white").place(x=90, y=140)
        self.txt_user = Entry(Frame_login, font=("times new roman", 15), bg="lightgrey")
        self.txt_user.place(x=90, y=170, width=350, height=35)
        
        lbl_pass = Label(Frame_login, text="Birdthday", font=("Goudy old style",15,"bold"), fg="grey", bg="white").place(x=90, y=210)
        self.txt_pass = DateEntry(Frame_login, selectmode="day",state="readonly",date_pattern = 'dd/mm/yyyy',background="blue",Cursor="hand1",year=2003, month=1, foreground='black', font=("Arial", 12))
        self.txt_pass.place(x=90, y=240, width=350, height=35)


        login_btn = Button(self.root, command=self.login_function,cursor="hand2",text="Login",fg="white",bg="#d77337", font=("times new roman",20)).place(x=300, y=470, width=180, height=40)

    def login_function(self):
        self.get_txt_pass = self.txt_pass.get()
        sql = "select email, dob from students where email = %s and dob = %s"
        mycursor.execute(sql, [(self.txt_user.get()), (self.txt_pass.get())])
        result = mycursor.fetchall()
        
        if(self.txt_user.get()=="" and self.txt_pass.get()==""):
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        elif result:
            self.root.destroy()
            os.system("python student_main_page.py")
        else:
            messagebox.showerror("Error", "password/username not match!",parent=self.root)

    def teh_login(self):
        self.root.destroy()
        os.system("python teacher_login.py")

if __name__ == "__main__":
    root = Tk()
    obj =student_Login(root)
    root.mainloop()

    