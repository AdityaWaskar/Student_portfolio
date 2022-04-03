from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter.ttk import Combobox

class forgot:
   def __init__(self,root):
      self.root=root
      self.root.title("FORGOT PASSWORD")
      self.root.geometry("350x400+495+150")
      self.root.config(bg="white")
      self.root.focus_force()
      self.root.grab_set()

      t=Label(self.root,text="FORGOT PASSWORD",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)

      question=Label(self.root,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
      self.cnb_quest=ttk.Combobox(font=("times new roman",13),state='readonly',justify=CENTER)
      self.cnb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
      self.cnb_quest.place(x=50,y=130,width=250)
      self.cnb_quest.current(0)
         
      answer=Label(self.root,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=180)
      self.txt_answer=Entry(self.root,font=("times new roman",15),bg="lightgray")
      self.txt_answer.place(x=50,y=210,width=250)

      new_password=Label(self.root,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=260)
      self.txt_new_pass=Entry(self.root,font=("times new roman",15),bg="lightgray")
      self.txt_new_pass.place(x=50,y=290,width=250)

      btn_change_password=Button(self.root,text="Reset Password",bg="green",fg="white",font=("times new roman",15,"bold")).place(x=90,y=340)
     # btn_change_password.pack(pady=10)


root = Tk()
#root.geometry("400x400+450+150")
#root.title("FORGOT PASSWORD")
obj = forgot(root)


root.mainloop()