from cgitb import text
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox

class extracurricular:
    def __init__(self,root):
        self.root=root
        self.root.title("EXTRA CURRICULAR ACTIVITY ")
        self.root.geometry("1600x800")
        self.root.config(bg="white")
        self.root.focus_force()
        #================title===================
        title=Label(self.root,text="EXTRA CURRICULAR ACTIVITY",font=("times new roman",20,"bold"),bg="#03a9f4",fg="black").place(x=10,y=15,width=1600,height=50)
        #================frame 1=================
        self.first_Frame = LabelFrame(self.root, text= "Search", font=("times new roman", 15), bg="white")
        self.first_Frame.place(x=400, y=150, width=800, height=100)
        self.var_search=StringVar()
        gr_no=Label(self.first_Frame,text="GR NO.",font=("times new roman",15,"bold"),bg="white").place(x=10,y=10)
        self.gr_no=Entry(self.first_Frame,font=("times new roman",20),bg="lightyellow").place(x=100,y=10,width=120)
        dob=Label(self.first_Frame,text="DOB.",font=("times new roman",15,"bold"),bg="white").place(x=240,y=10)
        self.dob=Entry(self.first_Frame,font=("times new roman",20),bg="lightyellow").place(x=300,y=10,width=120)
        self.search=Button(self.first_Frame,text='Search',font=("times new roman",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2")
        self.search.place(x=650,y=10,width=100,height=35)
        #================frame 2=================
        self.second_Frame = LabelFrame(self.root, bg="white")
        self.second_Frame.place(x=400, y=280, width=800, height=250)
        name=Label(self.second_Frame,text="Name : ",font=("times new roman",15,"bold"),bg="white").place(x=200,y=10)
        self.name=Entry(self.second_Frame,font=("times new roman",20),bg="lightyellow").place(x=340,y=10,width=250)

        category=Label(self.second_Frame,text="Category :",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=200,y=60)
        self.category=ttk.Combobox(self.second_Frame,font=("times new roman",15),state='readonly',justify=CENTER)
        self.category['values']=("Select","Technical","Non Technical")
        self.category.place(x=340,y=60,width=250)
        self.category.current(0)

        event_name=Label(self.second_Frame,text="Name of Event :",font=("times new roman",15,"bold"),bg="white").place(x=200,y=110)
        self.event_name=Entry(self.second_Frame,font=("times new roman",20),bg="lightyellow")
        self.event_name.place(x=345,y=110,width=250)

        upload=Button(self.second_Frame,text='Upload',font=("times new roman",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2").place(x=350,y=160,width=100,height=35)




root=Tk()
bj=extracurricular(root)
root.mainloop()