import os
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector as sql
from forgot_page import forgot
from register_page import Register

mydb = sql.connect(host="localhost", user="root", passwd="", database="SP")
mycursor = mydb.cursor()


class teacher_Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Register Page")
        self.root.geometry("1199x600+150+100")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="images/bg1.jpg")
        self.bg_img = Label(self.root, image=self.bg).place(x=0,y=0,relwidth=1, relheight=1)
        self.root.focus_force()

        Frame_login = Frame(self.root, bg="White")
        Frame_login.place(x=150, y=150, height=340, width=500)
    # title
        title = Label(Frame_login, text="Login As", font=("Impact",35,"bold"), fg="skyblue", bg="white").place(x=90, y=30)
        # desc = Label(Frame_login, text="Account Employee Login Area", font=("Goudy old style",15,"bold"), fg="#d25d17", bg="white").place(x=90, y=100)
        

        Button(Frame_login, text="Teacher" ,cursor="hand2",bg="white",fg="black" ,bd=1, font=("times new roman",12)).place(x=100, y=100)
        Button(Frame_login, text="Student",cursor="hand2",command=self.stu_login,bg="white",bd=0,fg="black", font=("times new roman",12)).place(x=270, y=100)
              
        lbl_user = Label(Frame_login, text="Username", font=("Goudy old style",15,"bold"), fg="grey", bg="white").place(x=90, y=140)
        self.txt_user = Entry(Frame_login, font=("times new roman", 15), bg="lightgrey")
        self.txt_user.place(x=90, y=170, width=350, height=35)
        
        lbl_pass = Label(Frame_login, text="Password", font=("Goudy old style",15,"bold"), fg="grey", bg="white").place(x=90, y=210)
        self.txt_pass = Entry(Frame_login, font=("times new roman", 15), bg="lightgrey")
        self.txt_pass.place(x=90, y=240, width=350, height=35)  


        forget_btn = Button(Frame_login, text="New Register",command=self.new_register ,cursor="hand2",bg="white",fg="#d77337",bd=0, font=("times new roman",12)).place(x=120, y=280)
        forget_btn = Button(Frame_login, command=self.forgot_pass,text="Forget Password?",cursor="hand2",bg="white",fg="#d77337",bd=0, font=("times new roman",12)).place(x=260, y=280)
        login_btn = Button(self.root, command=self.login_function,cursor="hand2",text="Login",fg="white",bg="#d77337", font=("times new roman",20)).place(x=300, y=470, width=180, height=40)

    def login_function(self):
        sql = "select * from login where username = %s and password = %s"
        mycursor.execute(sql, [(self.txt_user.get()), (self.txt_pass.get())])
        result = mycursor.fetchall()
        
        if(self.txt_user.get()=="" and self.txt_pass.get()==""):
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        elif result:
            self.root.destroy()
            os.system("python main_page.py")
        else:
            messagebox.showerror("Error", "password/username not match!",parent=self.root)
            
    def stu_login(self):
        self.root.destroy()
        os.system("python student_login.py")

    def forgot_pass(self):
        if(self.txt_user.get() == ''):
            self.txt_user.config(highlightthickness=1,highlightbackground="red")
            messagebox.showerror('error', 'Enter Username!')
        else:
            self.new_win = Toplevel(self.root)
            self.new_obj = forgot(self.new_win)

    def new_register(self):
        print("aditya")
        self.reg_win = Toplevel(self.root)
        self.new_obj = Register(self.reg_win) 
         
if __name__ == "__main__":
    root=Tk()
    obj = teacher_Login(root)
    root.mainloop()