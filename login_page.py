from tkinter import *
from PIL import ImageTk
import os

class Login:
    def __init__(self, root):
        self.root = root                                                                                                                                    
        self.root.title("Login Page")
        self.root.geometry("1199x600+150+100") 
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="images/bg1.jpg")
        self.bg_img = Label(self.root, image=self.bg).place(x=0,y=0,relwidth=1, relheight=1)
        self.root.focus_force()
    
        Frame_login = Frame(self.root, bg="White")
        Frame_login.place(x=150, y=150, height=340, width=500)
    # title
        title = Label(Frame_login, text="Login As:", font=("Impact",35,"bold"), fg="skyblue", bg="white").place(x=90, y=30)
        
        Button(Frame_login, text="Teacher",cursor="hand2",bg="white",command=self.teh_login,fg="black" ,bd=0, font=("times new roman",12)).place(x=100, y=100)
        Button(Frame_login, text="Student",cursor="hand2",bg="white",command=self.stu_login,fg="black",bd =0, font=("times new roman",12)).place(x=270, y=100)
    
    
    def stu_login(self):
        self.root.destroy()
        os.system("python student_login.py")
    
    def teh_login(self):
        self.root.destroy()
        os.system("python teacher_login.py")


              
        
if __name__ == "__main__":
    root=Tk()
    obj = Login(root)
    root.mainloop()