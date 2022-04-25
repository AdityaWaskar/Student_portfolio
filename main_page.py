from tkinter import *
from logging import root
from PIL import Image, ImageTk

from add_student import add_student
from add_teacher import add_teacher
from report_by_teacher import report_by_teacher
from result_input_by_teacher import enter_marks_by_teacher
from show_student import show_student
from show_teacher import show_teacher
from take_attendance import take_attendance
from show_performance import show_performance
from show_defaulter import show_defaulter 
from result_input import enter_marks
from extracurricular_activity import extracurricular


class Login:
    def __init__(self, root):
        self.root = root                                                                                                                                    
        screen_width = self.root.winfo_screenwidth()
        screen_heigth = self.root.winfo_screenheight()
        self.root.title("Login Page")
        self.root.geometry("%dx%s+-10+0"%(screen_width,screen_heigth)) 
        self.root.focus_force()
        self.root.grab_set()
        print(screen_heigth)
        print(screen_width)
        # self.root.attributes('-fullscreen',True)

        image = Image.open("images\\main_bg.jpg")
        image=image.resize((1600,830))
        photo = ImageTk.PhotoImage(image)
        label1 = Label(root,image=photo) 
        label1.image = photo
        label1.pack()

        filemenu = Menu(self.root)  #mainmenu

        m1 = Menu(filemenu,tearoff=0)
        m1.add_command(label="ADD TEACHER",command=self.add_teacher)
        m1.add_command(label="ADD STUDENT",command=self.add_students)
        self.root.config(menu=filemenu)
        filemenu.add_cascade(label="ADD",menu=m1)

        m2 = Menu(filemenu,tearoff=0)
        m2.add_command(label="TEACHER",command=self.show_teacher)
        m2.add_command(label="STUDENT",command=self.show_students)
        self.root.config(menu=filemenu)
        filemenu.add_cascade(label="DETAILS",menu=m2)

        m3 = Menu(filemenu,tearoff=0)
        m3.add_command(label="ATTENDENCE",command=self.take_attendance)
        self.root.config(menu=filemenu)
        filemenu.add_cascade(label="ATTENDENCE",menu=m3)

        m4 = Menu(filemenu,tearoff=0)
        m4.add_command(label="PERFORMANCE",command=self.show_performance)
        m4.add_command(label="DEFAULTER LIST",command=self.show_defaulter)
        self.root.config(menu=filemenu)
        filemenu.add_cascade(label="REPORT",menu=m4)

        m5 = Menu(filemenu,tearoff=0)
        m5.add_command(label="ADD MARKS",command=self.result_input)
        m5.add_command(label="SHOW MARKS",command=self.report)
        self.root.config(menu=filemenu)
        filemenu.add_cascade(label="MARKS",menu=m5)
        
        m6 = Menu(filemenu,tearoff=0)
        m6.add_command(label="ADD ACTIVITY",command=self.activity)
        self.root.config(menu=filemenu)
        filemenu.add_cascade(label="ACTIVITY",menu=m6)

        m7 = Menu(filemenu,tearoff=0)
        m7.add_command(label="EXIT",command=exit)
        self.root.config(menu=filemenu)
        filemenu.add_cascade(label="LOGOUT",menu=m7)

    def activity(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = extracurricular(self.new_win)

    def add_teacher(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = add_teacher(self.new_win)
    
    def add_students(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = add_student(self.new_win)

    def show_students(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = show_student(self.new_win)
        
    def show_teacher(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = show_teacher(self.new_win)
        
    def take_attendance(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = take_attendance(self.new_win)

    def show_performance(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = show_performance(self.new_win)

    def show_defaulter(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = show_defaulter(self.new_win)

    def result_input(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = enter_marks_by_teacher(self.new_win)
    
    def report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = report_by_teacher(self.new_win)

        
if __name__ == "__main__":
    root=Tk()
    obj = Login(root)
    root.mainloop()