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

    # title
        title = Label(self.root, text="Main Page", font=("Impact",35,"bold"), fg="skyblue", bg="white").place(x=90, y=30)
        # desc = Label(Frame_login, text="Account Employee Login Area", font=("Goudy old style",15,"bold"), fg="#d25d17", bg="white").place(x=90, y=100)

       
    



              
        
if __name__ == "__main__":
    root=Tk()
    obj = Login(root)
    root.mainloop()