from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as sql

# ----------------------Connection with database
mydb = sql.connect(host="localhost", user="root", passwd="", database="SP")
mycursor = mydb.cursor()

class forgot:
   def __init__(self,root):
      self.root=root
      self.root.title("FORGOT PASSWORD")
      self.root.geometry("350x400+520+180")
      self.root.config(bg="white")
      self.root.focus_force()
      self.root.grab_set()

      t=Label(self.root,text="FORGOT PASSWORD",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)

      question=Label(self.root,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=70)
      self.question=ttk.Combobox(self.root,font=("times new roman",13),state='readonly',justify=CENTER)
      self.question['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
      self.question.place(x=50,y=100,width=250)
      self.question.current(0)

      answer=Label(self.root,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=140)
      self.txt_answer=Entry(self.root,font=("times new roman",15),bg="lightgray")
      self.txt_answer.place(x=50,y=170,width=250)

      Button(self.root,command=self.check_ans,text="Check",bg="green",fg="white",font=("times new roman",12)).place(x=140,y=210)

      self.new_password=Label(self.root,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="gray")
      self.txt_new_pass=Entry(self.root,font=("times new roman",15),bg="lightgray")

     # btn_change_password.pack(pady=10)

   def check_ans(self):
      self.get_question = self.question.get()
      self.get_answer = self.txt_answer.get()

      query1 = f"select * from login where question = '{self.get_question}' and answer = '{self.get_answer}'"
      mycursor.execute(query1)
      result = mycursor.fetchall()
      if(result):
         messagebox.showinfo("new", "Enter new password", parent=self.root)
         self.new_password.place(x=50,y=260)
         self.txt_new_pass.place(x=50,y=290,width=250 )
         Button(self.root,command=self.change_pass ,text="Reset Password",bg="green",fg="white",font=("times new roman",15,"bold")).place(x=90,y=340)
# -----------update password
      else: 
         messagebox.showerror("error", "Question and answer is not match!", parent=self.root)

   def change_pass(self):
      self.get_question = self.question.get()
      self.get_answer = self.txt_answer.get()
      self.get_new_pass = self.txt_new_pass.get()
      try:
         query = f"update login set password = '{self.get_new_pass}' where question = '{self.get_question}' and answer = '{self.get_answer}';"
         mycursor.execute(query)
         print(query)
         mydb.commit()
         messagebox.showinfo("info", "Password changed!", parent=self.root)
         self.root.destroy()
      except:
         query = f"update login set password = '{self.get_new_pass}' where question = '{self.get_question}' and answer = '{self.get_answer}';"
         print(query)
         mycursor.execute(query)
         mydb.commit()
      
         



if __name__ == "__main__":
   root = Tk()
   obj = forgot(root)
   root.mainloop()