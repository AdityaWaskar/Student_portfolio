import os
from tkinter import *
from tkinter import messagebox
from PIL import Image ,ImageTk
from Report import report

from show_defaulter import show_defaulter 
from result_input import enter_marks
from Report import report
# from course import courseClass
class RMS:
    def __init__(self, root):
        self.root= root
        self.root.title("Result Management System")
        self.root.geometry("1600x800+0+0")
        self.root.config(bg="white")

        self.bg_img = Image.open("images/bg1.jpg") 
        self.bg_img = self.bg_img.resize((1600, 800), Image.ANTIALIAS)       
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=0, y=0, width=1600, height=800)

        title = Label(self.root, text="Performance", font=("goudy old style",25,"bold"),fg="white", bg="#fa9f02").place(x=40, y=10,width= 1460, height=80)

        # buttons
        self.add_marks_btn = Button(self.root,command=self.add_marks,text="Add Marks",cursor='hand2',font=("goundy old style", 20), bd=10,relief=RIDGE, bg="#e43b06", fg="white")
        self.add_marks_btn.place(x=350, y=200,width=300, height=100)
        
        self.show_marks_btn = Button(self.root,command=self.show_marks, text="Show Marks",cursor = 'hand2',font=("goundy old style", 20), bd=10,relief=RIDGE, bg="#0676ad", fg="white")
        self.show_marks_btn.place(x=850, y=200,width=300, height=100)
        
        self.defaulter_btn = Button(self.root,command=self.defaulter, text="Defaulter List",cursor = 'hand2',font=("goundy old style", 20), bd=10,relief=RIDGE, bg="#038074", fg="white")
        self.defaulter_btn.place(x=350, y=400,width=300, height=100)
        
        self.log_btn = Button(self.root,command=self.logout, text="Logout",cursor = 'hand2',font=("goundy old style", 20), bd=10,relief=RIDGE, bg="#038074", fg="white")
        self.log_btn.place(x=850, y=400,width=300, height=100)

        #Footer
        footer =Label(self.root, text="SP = Student Portfolio\nContact Us for any technical issue: 1234567890",font=("goudy old style",12), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)

    def add_marks(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = enter_marks(self.new_win)
    def show_marks(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = report(self.new_win)
    def defaulter(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = show_defaulter(self.new_win)
    def logout(self):
        a = messagebox.askquestion("logout", "Are you sure?")
        print(a)
        if(a == "yes"):
            self.root.destroy()
            os.system('python student_Login.py')



if __name__ == "__main__":
    root=Tk()
    obj = RMS(root)
    root.mainloop()