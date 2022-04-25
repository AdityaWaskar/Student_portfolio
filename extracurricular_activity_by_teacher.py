from multiprocessing import parent_process
import shutil
from tkinter import*
from tkinter import Tk, filedialog
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector as sql
from tkinter import *
from tkcalendar import DateEntry

from extracurriculaum_document import extracurriculaum_document

# ----------------------Connection with database
mydb = sql.connect(host="localhost", user="root", passwd="", database="SP")
mycursor = mydb.cursor()

class extracurricular_by_teacher:
    def __init__(self,root):
        self.root=root
        self.root.title("EXTRA CURRICULAR ACTIVITY ")
        self.root.geometry("1500x800+10+13")
        self.root.config(bg="white")
        self.root.focus_force()
        #================title===================
        title=Label(self.root,text="Extra Curricular Activity",font=("times new roman",20,"bold"),bg="orange",fg="black").place(x=10,y=15,width=1600,height=50)
        #================frame 1=================
        self.first_Frame = LabelFrame(self.root, text= "Search", font=("times new roman", 15), bg="white")
        self.first_Frame.place(x=400, y=150, width=800, height=100)
        self.var_search=StringVar()

        gr_no=Label(self.first_Frame,text="GR NO.",font=("times new roman",15,"bold"),bg="white").place(x=200,y=10)
        self.gr_no=Entry(self.first_Frame,font=("times new roman",15),bg="lightyellow")
        self.gr_no.place(x=300,y=10,width=200)
        
        self.search=Button(self.first_Frame,text='Search', command=self.search,font=("times new roman",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2")
        self.search.place(x=650,y=10,width=100,height=35)

        #================frame 2=================
        self.second_Frame = LabelFrame(self.root, bg="white")

        name=Label(self.second_Frame,text="Name", justify=CENTER,font=("times new roman",15,"bold"),bg="white")
        name.place(x=180,y=30, width=150)
        self.name=Entry(self.second_Frame,font=("times new roman",15),bg="lightyellow")
        self.name.place(x=340,y=30,width=250)

        category=Label(self.second_Frame,text="Category", justify=CENTER,font=("times new roman",15,"bold"),bg="white",fg="black")
        category.place(x=180,y=80, width=150)
        self.category=ttk.Combobox(self.second_Frame,font=("times new roman",15),state='readonly',justify=CENTER)
        self.category['values']=("Select","Technical_event","Non_Technical_event")
        self.category.place(x=340,y=80,width=250)
        self.category.current(0)

        event_name=Label(self.second_Frame,text="Name of Event", justify=CENTER,font=("times new roman",15,"bold"),bg="white")
        event_name.place(x=180,y=130, width=150)
        self.event_name=Entry(self.second_Frame,font=("times new roman",15),bg="lightyellow")
        self.event_name.place(x=345,y=130,width=250)

        upload=Button(self.second_Frame,text='Upload', command=self.upload,font=("times new roman",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2")
        upload.place(x=360,y=180,width=100,height=35)

        self.upload = Button(self.root,text='Upload',font=("times new roman",15,"bold"),command = self.upload,bg="#03a9f4",fg="white",cursor="hand2")
        self.upload_warn = Label(self.second_Frame, bg= "white", fg="red", justify=CENTER)

        self.document = Button(self.root,bd=0,text='See the uploaded documents.',bg="white" ,command=self.show_document,justify=CENTER,font=("goudy old style",15,"bold","underline"),fg="orange",cursor="hand2")
        

# ---------progress bar 
        self.progress = ttk.Progressbar(self.second_Frame, orient = HORIZONTAL,length = 100, mode = 'determinate')

    def search(self):
        self.get_gr_no = self.gr_no.get()

        if(self.get_gr_no == ""):
            messagebox.showinfo("info", "Enter Gr No.", parent= self.root)
        else:
            query1 = f"SELECT name FROM students where gr_no = {self.get_gr_no} ;" 
            mycursor.execute(query1)
            result1 = mycursor.fetchone()
            if(result1):
                self.second_Frame.place(x=400, y=320, width=800, height=250)
                self.name.delete(0, 'end')
                self.name.insert(0, result1[0])
                print(result1[0])
                self.name.config(state="readonly")
            else:
                messagebox.showerror("error", "Gr number not found!",parent= self.root )

    def upload(self):
        if(self.name.get() == "" or self.category.get() == "Select" or self.event_name.get() == ""):
            messagebox.showerror("error", "All field must be required!", parent = self.root)
        else:
# --------------open the directory
            f_types =[('jpg files','*.jpg')]
            source = filedialog.askopenfilename(filetypes=f_types, parent=self.root)
# --------------upload the filepath to database
        if(source == ""):
            print("no")
            self.upload_warn.place(x=1340, y=750)
        else:
            self.destination = f"student_documents/event/{self.category.get()}/{self.get_gr_no}.jpg"
            dest = shutil.copy(source, self.destination)
            self.bar()
            self.upload_warn.config(text="Sucessfully Uploaded", fg="green")
            self.upload_warn.place(x=490,y=200)
            self.document.place(x=680,y=600,width=300,height=35)
            try:
                query = f"UPDATE students set {self.category.get()} = '{self.destination}' WHERE gr_no = {self.gr_no.get()} ;"
                mycursor.execute(query)
                mydb.commit()
            except Exception as e:
                print("some error to upload the file!")

# -----------progress bar running method
    def bar(self):
            self.progress.place(x=490,y=190, height=10)
            import time
            self.progress['value'] = 20
            self.root.update_idletasks()
            time.sleep(1)

            self.progress['value'] = 40
            self.root.update_idletasks()
            time.sleep(1)

            self.progress['value'] = 50
            self.root.update_idletasks()
            time.sleep(1)

            self.progress['value'] = 60
            self.root.update_idletasks()
            time.sleep(1)

            self.progress['value'] = 80
            self.root.update_idletasks()
            time.sleep(1)
            self.progress['value'] = 100

    def show_document(self):
        try:
            self.new_win = Toplevel(self.root)
            self.new_obj = extracurriculaum_document(self.new_win, self.gr_no.get(), self.category.get())
        except Exception as e:
            print(e)
if __name__ == "__main__":
    root=Tk()
    obj=extracurricular_by_teacher(root)
    root.mainloop()