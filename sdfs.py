from turtle import width
from pip import main
from tkPDFViewer import tkPDFViewer as pdf
import shutil
from tkinter import Tk, filedialog
from tkinter import *
from PIL import ImageTk, Image
import mysql.connector as sql
import fitz
# doc = fitz.open("E:/python/project/Student Portfoilo/student_documents/results/Information Technology/sem1/file.jpg")

# mydb = sql.connect(host="localhost", user="root", passwd="", database="SP")
# mycursor = mydb.cursor()
# page = doc[0]
# height = int(page.rect.height)
# width = int(page.rect.width)
# print(height, width)


class teacher_Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        # self.root.geometry("1199x600+150+100")
        self.root.geometry("1600x500")
        self.root.configure(bg='#d8dfed')
        
        # self.root.resizable(False, False)
        # global source,img
        # f_types =[('pdf files','*.pdf'),('Jpg Files', '*.jpg')]
        
        # source = filedialog.askopenfilename(filetypes=f_types)
        # print(source)
        # # source = f'r"{source}"'
        # print(source)
        # destination = "E:/python/project/Student Portfoilo/student_documents/results/Information Technology/sem1/1000.jpg"
        # dest = shutil.copy(source, destination)
        # # Button(self.root,text="hs", command= self.show1).pack()
       
        
        frame = Frame(self.root, width=600, height=400)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)

        # Create an object of tkinter ImageTk
        img = Image.open("E:/python/project/Student Portfoilo/student_documents/results/Information Technology/sem1/1000.jpg")

        # img = img.resize((500, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        # Create a Label Widget to display the text or Image
        label = Label(frame, image = img)
        label.pack()


        
if __name__ == "__main__":
    root=Tk()
    obj = teacher_Login(root)
    
    root.mainloop()

