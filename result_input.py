from argparse import _MutuallyExclusiveGroup
import base64
from fileinput import filename
from itertools import count
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from tkinter import filedialog
import mysql.connector as sql

mydb = sql.connect(host="localhost", user="root", passwd="", database="SP")
mycursor = mydb.cursor()

subjects =[["EM_1", "EC_1", "EP_1", "BEE", "Mechanics"],
            ["EM_2", "EC_2", "EP_2", "C_Programming", "ED"],
            ["EM_3", "Java", "DSA", "DBMS", "PCE_1"],
            ["EM_4", "Python", "CNND", "OS", "COA"],
            ["Internet_Programming"],
            ["Data_Mining"],
            ["Enterprise_Network_Design"],
            ["Big_data_analytics"]]

class enter_marks:
    def __init__(self,root):
        self.root=root
        self.root.title("Enter Marks ")
        self.root.geometry("1600x800+0+0")
        self.root.config(bg="white")
        self.root.focus_force()
        self.count = -1
        #================title===================
        title=Label(self.root,text="Enter Your Marks",font=("times new roman",20,"bold"),bg="orange",fg="white").place(x=10,y=15,width=1600,height=50)

        #==============search=============
        self.var_search=StringVar()
        gr_no=Label(self.root,text="ENTER GR NO.",font=("times new roman",15,"bold"),bg="white").place(x=140,y=100)
        self.gr_no=Entry(self.root,textvariable=self.var_search,font=("times new roman",20),bg="lightyellow")
        self.gr_no.place(x=340,y=100,width=150)
        btn_search=Button(self.root,text='Search',command=self.search,font=("times new roman",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2").place(x=500,y=100,width=100,height=35)
        btn_clear=Button(self.root,text='Clear',font=("times new roman",15,"bold"),bg="gray",fg="white",cursor="hand2").place(x=620,y=100,width=100,height=35)
        btn_submit=Button(self.root,command=self.submit,text='Submit',font=("times new roman",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2").place(x=1400,y=100,width=100,height=35)

        #===================
        self.m_Frame = LabelFrame(self.root, text= "SEMESTER", font=("times new roman", 15), bg="white")

        self.btn_sem1 = Button(self.m_Frame, text="Sem 1", command=self.set_subject1,cursor="hand2",font=("times new roman",15,"bold"), bg="#0b5377", fg="white")
        self.btn_sem2 = Button(self.m_Frame, text="Sem 2", command=self.set_subject2,cursor="hand2",font=("times new roman",15,"bold"), bg="#0b5377", fg="white")
        self.btn_sem3 = Button(self.m_Frame, text="Sem 3", command=self.set_subject3,cursor="hand2",font=("times new roman",15,"bold"), bg="#0b5377", fg="white")
        self.btn_sem4 = Button(self.m_Frame, text="Sem 4", command=self.set_subject4,cursor="hand2",font=("times new roman",15,"bold"), bg="#0b5377", fg="white")
        self.btn_sem5 = Button(self.m_Frame, text="Sem 5", command=self.set_subject5,cursor="hand2",font=("times new roman",15,"bold"), bg="#0b5377", fg="white")
        self.btn_sem6 = Button(self.m_Frame, text="Sem 6", command=self.set_subject6,cursor="hand2",font=("times new roman",15,"bold"), bg="#0b5377", fg="white")
        self.btn_sem7 = Button(self.m_Frame, text="Sem 7", command=self.set_subject7,cursor="hand2",font=("times new roman",15,"bold"), bg="#0b5377", fg="white")
        self.btn_sem8 = Button(self.m_Frame, text="Sem 8", command=self.set_subject8,cursor="hand2",font=("times new roman",15,"bold"), bg="#0b5377", fg="white")
        #==========================tt1=============
        self.m1_Frame = LabelFrame(self.root, text= "TERM TEST 1", font=("times new roman", 15), bg="white")

        self.tt1_lbl_sub1 = Entry(self.m1_Frame, text="Sub 1", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt1_lbl_sub1.place(x=40, y=30, width=100, height=30)
        self.tt1_mark_sub1 = Entry(self.m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_mark_sub1.place(x=150, y=30, width=100, height=30)
        self.slash = Label(self.m1_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=30, width=10, height=30)
        self.tt1_out_sub1 = Entry(self.m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_out_sub1.place(x=280, y=30, width=100, height=30)

        self.tt1_lbl_sub2 = Entry(self.m1_Frame, text="Sub 2", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt1_lbl_sub2.place(x=40, y=70, width=100, height=30)
        self.tt1_mark_sub2 = Entry(self.m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_mark_sub2.place(x=150, y=70, width=100, height=30)
        self.slash = Label(self.m1_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=70, width=10, height=30)
        self.tt1_out_sub2 = Entry(self.m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_out_sub2.place(x=280, y=70, width=100, height=30)

        self.tt1_lbl_sub3 = Entry(self.m1_Frame, text="Sub 3", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt1_lbl_sub3.place(x=40, y=110, width=100, height=30)
        self.tt1_mark_sub3 = Entry(self.m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_mark_sub3.place(x=150, y=110, width=100, height=30)
        self.slash = Label(self.m1_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black").place(x=260, y=110, width=10, height=30)
        self.tt1_out_sub3 = Entry(self.m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_out_sub3.place(x=280, y=110, width=100, height=30)
       
        self.tt1_lbl_sub4 = Entry(self.m1_Frame, text="Sub 4", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt1_lbl_sub4.place(x=40, y=150, width=100, height=30)
        self.tt1_mark_sub4 = Entry(self.m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_mark_sub4.place(x=150, y=150, width=100, height=30)
        self.slash = Label(self.m1_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black").place(x=260, y=150, width=10, height=30)
        self.tt1_out_sub4 = Entry(self.m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_out_sub4.place(x=280, y=150, width=100, height=30)

        self.tt1_lbl_sub5 = Entry(self.m1_Frame, text="Sub 5", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt1_lbl_sub5.place(x=40, y=190, width=100, height=30)
        self.tt1_mark_sub5 = Entry(self.m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_mark_sub5.place(x=150, y=190, width=100, height=30)
        self.slash = Label(self.m1_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black").place(x=260, y=190, width=10, height=30)
        self.tt1_out_sub5 = Entry(self.m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_out_sub5.place(x=280, y=190, width=100, height=30)

       #==============================tt2==========================
        self.m2_Frame = LabelFrame(self.root, text= "TERM TEST 2", font=("times new roman", 15), bg="white")
        

        self.tt2_lbl_sub1 = Entry(self.m2_Frame, text="Sub 1", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt2_lbl_sub1.place(x=40, y=30, width=100, height=30)
        self.tt2_mark_sub1 = Entry(self.m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_mark_sub1.place(x=150, y=30, width=100, height=30)
        self.slash = Label(self.m2_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=30, width=10, height=30)
        self.tt2_out_sub1 = Entry(self.m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_out_sub1.place(x=280, y=30, width=100, height=30)
        
        self.tt2_lbl_sub2 = Entry(self.m2_Frame, text="Sub 2", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt2_lbl_sub2.place(x=40, y=70, width=100, height=30)
        self.tt2_mark_sub2 = Entry(self.m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_mark_sub2.place(x=150, y=70, width=100, height=30)
        self.slash = Label(self.m2_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=70, width=10, height=30)
        self.tt2_out_sub2 = Entry(self.m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_out_sub2.place(x=280, y=70, width=100, height=30)
        
        
        self.tt2_lbl_sub3  = Entry(self.m2_Frame, text="Sub 3", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt2_lbl_sub3.place(x=40, y=110, width=100, height=30)
        self.tt2_mark_sub3  = Entry(self.m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_mark_sub3.place(x=150, y=110, width=100, height=30)
        self.slash  = Label(self.m2_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=110, width=10, height=30)
        self.tt2_out_sub3  = Entry(self.m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_out_sub3.place(x=280, y=110, width=100, height=30)
        
        
        self.tt2_lbl_sub4 = Entry(self.m2_Frame, text="Sub 4", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt2_lbl_sub4.place(x=40, y=150, width=100, height=30)
        self.tt2_mark_sub4 = Entry(self.m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_mark_sub4 .place(x=150, y=150, width=100, height=30)
        self.slash = Label(self.m2_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=150, width=10, height=30)
        self.tt2_out_sub4 = Entry(self.m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_out_sub4.place(x=280, y=150, width=100, height=30)
        
        self.tt2_lbl_sub5= Entry(self.m2_Frame, text="Sub 5", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt2_lbl_sub5.place(x=40, y=190, width=100, height=30)
        self.tt2_mark_sub5 = Entry(self.m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_mark_sub5.place(x=150, y=190, width=100, height=30)
        self.slash = Label(self.m2_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=190, width=10, height=30)
        self.tt2_out_sub5 = Entry(self.m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_out_sub5.place(x=280, y=190, width=100, height=30)
        

       #==================semester===============
        self.m3_Frame = LabelFrame(self.root, text= "SEMESTER", font=("times new roman", 15), bg="white")
        

        self.ut_lbl_sub1= Entry(self.m3_Frame, text="Sub 1", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.ut_lbl_sub1.place(x=40, y=30, width=100, height=30)
        self.ut_mark_sub1 = Entry(self.m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_mark_sub1.place(x=150, y=30, width=100, height=30)
        self.slash = Label(self.m3_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=30, width=10, height=30)
        self.ut_out_sub1 = Entry(self.m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_out_sub1.place(x=280, y=30, width=100, height=30)
        
        self.ut_lbl_sub2 = Entry(self.m3_Frame, text="Sub 2", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.ut_lbl_sub2.place(x=40, y=70, width=100, height=30)
        self.ut_mark_sub2 = Entry(self.m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_mark_sub2.place(x=150, y=70, width=100, height=30)
        self.slash = Label(self.m3_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=70, width=10, height=30)
        self.ut_out_sub2 = Entry(self.m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_out_sub2.place(x=280, y=70, width=100, height=30)
        
        self.ut_lbl_sub3 = Entry(self.m3_Frame, text="Sub 3", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.ut_lbl_sub3.place(x=40, y=110, width=100, height=30)
        self.ut_mark_sub3 = Entry(self.m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_mark_sub3.place(x=150, y=110, width=100, height=30)
        self.slash = Label(self.m3_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=110, width=10, height=30)
        self.ut_out_sub3 = Entry(self.m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_out_sub3.place(x=280, y=110, width=100, height=30)
        
        self.ut_lbl_sub4 = Entry(self.m3_Frame, text="Sub 4", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.ut_lbl_sub4.place(x=40, y=150, width=100, height=30)
        self.ut_mark_sub4 = Entry(self.m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_mark_sub4.place(x=150, y=150, width=100, height=30)
        self.slash = Label(self.m3_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=150, width=10, height=30)
        self.ut_out_sub4 = Entry(self.m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_out_sub4.place(x=280, y=150, width=100, height=30)
        
        self.ut_lbl_sub5 = Entry(self.m3_Frame, text="Sub 5", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.ut_lbl_sub5.place(x=40, y=190, width=100, height=30)
        self.ut_mark_sub5 = Entry(self.m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_mark_sub5.place(x=150, y=190, width=100, height=30)
        self.slash = Label(self.m3_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=190, width=10, height=30)
        self.ut_out_sub5 = Entry(self.m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_out_sub5.place(x=280, y=190, width=100, height=30)

        Button(self.root,text='Upload',font=("times new roman",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2").place(x=1400,y=500,width=100,height=35)

    def search(self):
        self.get_gr_no = self.gr_no.get()
        self.get_dob = '03/01/2003'
        if(self.get_gr_no == ''):
            messagebox.showerror('error', 'Enter gr no')
        elif(self.get_dob == ''):
            messagebox.showerror('error', 'Enter dob no')
        else:
            query = f"select * from students where gr_no ={self.get_gr_no} and dob = '{self.get_dob}'"
            mycursor.execute(query)
            result = mycursor.fetchone()

            if(result):
                self.show_sem()
                self.m1_Frame.place(x=80, y=230, width=680, height=280)
                self.m2_Frame.place(x=770, y=230, width=690, height=280)
                self.m3_Frame.place(x=350, y=520, width=680, height=280)
                self.m_Frame.place(x=80, y=150, width=1380, height=80)

                messagebox.showinfo('message',  'Enter the marks')
            else:
                messagebox.showinfo('message', 'gr_no and dob no match!')

    def show_sem(self):
        query = f"select sem from students where gr_no = {self.gr_no.get()}"
        mycursor.execute(query)
        result = mycursor.fetchone()
        print(result[0])
        print(result)
        if(result[0] == 'sem 1'):
            self.btn_sem1.place(x=40, y=5, width=100, height=30)
        elif(result[0] == 'sem 2'):
            self.btn_sem1.place(x=40, y=5, width=100, height=30)
            self.btn_sem2.place(x=210, y=5, width=100, height=30)
        elif(result[0] == 'sem 3'):
            self.btn_sem1.place(x=40, y=5, width=100, height=30)
            self.btn_sem2.place(x=210, y=5, width=100, height=30)
            self.btn_sem3.place(x=380, y=5, width=100, height=30)
        elif(result[0] == 'sem 4'):
            self.btn_sem1.place(x=40, y=5, width=100, height=30)
            self.btn_sem2.place(x=210, y=5, width=100, height=30)
            self.btn_sem3.place(x=380, y=5, width=100, height=30)
            self.btn_sem4.place(x=550, y=5, width=100, height=30)
        elif(result[0] == 'sem 5'):
            self.btn_sem1.place(x=40, y=5, width=100, height=30)
            self.btn_sem2.place(x=210, y=5, width=100, height=30)
            self.btn_sem3.place(x=380, y=5, width=100, height=30)
            self.btn_sem4.place(x=550, y=5, width=100, height=30)
            self.btn_sem5.place(x=720, y=5, width=100, height=30)
        elif(result[0] == 'sem 6'):
            self.btn_sem1.place(x=40, y=5, width=100, height=30)
            self.btn_sem2.place(x=210, y=5, width=100, height=30)
            self.btn_sem3.place(x=380, y=5, width=100, height=30)
            self.btn_sem4.place(x=550, y=5, width=100, height=30)
            self.btn_sem5.place(x=720, y=5, width=100, height=30)
            self.btn_sem6.place(x=890, y=5, width=100, height=30)
        elif(result[0] == 'sem 7'):
            self.btn_sem1.place(x=40, y=5, width=100, height=30)
            self.btn_sem2.place(x=210, y=5, width=100, height=30)
            self.btn_sem3.place(x=380, y=5, width=100, height=30)
            self.btn_sem4.place(x=550, y=5, width=100, height=30)
            self.btn_sem5.place(x=720, y=5, width=100, height=30)
            self.btn_sem6.place(x=890, y=5, width=100, height=30)
            self.btn_sem7.place(x=1060, y=5, width=100, height=30)
        elif(result[0] == 'sem 8'):
            self.btn_sem1.place(x=40, y=5, width=100, height=30)
            self.btn_sem2.place(x=210, y=5, width=100, height=30)
            self.btn_sem3.place(x=380, y=5, width=100, height=30)
            self.btn_sem4.place(x=550, y=5, width=100, height=30)
            self.btn_sem5.place(x=720, y=5, width=100, height=30)
            self.btn_sem6.place(x=890, y=5, width=100, height=30)
            self.btn_sem7.place(x=1060, y=5, width=100, height=30)
            self.btn_sem8.place(x=1230, y=5, width=100, height=30)


    def set_subject1(self):
        self.sem = 'sem1'
        self.count = 0
        self.set()
    def set_subject2(self):
        self.sem = 'sem2'
        self.count = 1
        self.set()
    def set_subject3(self):
        self.sem = 'sem3'
        self.count = 2
        self.set()
    def set_subject4(self):
        self.sem = 'sem4'
        self.count = 3
        self.set()
    def set_subject5(self):
        self.sem = 'sem5'
        self.count = 4
        self.set()
    def set_subject6(self):
        self.sem = 'sem6'
        self.count = 5
        self.set()
    def set_subject7(self):
        self.sem = 'sem7'
        self.count = 6
        self.set()
    def set_subject8(self):
        self.sem = 'sem8'
        self.count = 7
        self.set()
    def set(self):
# ---------------setting the tt1 subjects
        self.tt1_lbl_sub1.config(state=NORMAL)
        self.tt1_lbl_sub2.config(state=NORMAL)
        self.tt1_lbl_sub3.config(state=NORMAL)
        self.tt1_lbl_sub4.config(state=NORMAL)
        self.tt1_lbl_sub5.config(state=NORMAL)

        self.tt1_lbl_sub1.delete(0, 'end')
        self.tt1_lbl_sub2.delete(0, 'end')
        self.tt1_lbl_sub3.delete(0, 'end')
        self.tt1_lbl_sub4.delete(0, 'end')
        self.tt1_lbl_sub5.delete(0, 'end')

        self.tt1_lbl_sub1.insert(0, subjects[self.count][0])
        self.tt1_lbl_sub2.insert(0, subjects[self.count][1])
        self.tt1_lbl_sub3.insert(0, subjects[self.count][2])
        self.tt1_lbl_sub4.insert(0, subjects[self.count][3])
        self.tt1_lbl_sub5.insert(0, subjects[self.count][4])

        self.tt1_lbl_sub1.config(state='readonly', fg="#0e064d")
        self.tt1_lbl_sub2.config(state='readonly', fg="#0e064d")
        self.tt1_lbl_sub3.config(state='readonly', fg="#0e064d")
        self.tt1_lbl_sub4.config(state='readonly', fg="#0e064d")
        self.tt1_lbl_sub5.config(state='readonly', fg="#0e064d")

        self.tt1_out_sub1.delete(0, 'end')
        self.tt1_out_sub2.delete(0, 'end')
        self.tt1_out_sub3.delete(0, 'end')
        self.tt1_out_sub4.delete(0, 'end')
        self.tt1_out_sub5.delete(0, 'end')

        self.tt1_out_sub1.insert(0, '20')
        self.tt1_out_sub2.insert(0, '20')
        self.tt1_out_sub3.insert(0, '20')
        self.tt1_out_sub4.insert(0, '20')
        self.tt1_out_sub5.insert(0, '20')
        
# ---------------setting the tt2 subjects
        self.tt2_lbl_sub1.config(state=NORMAL)
        self.tt2_lbl_sub2.config(state=NORMAL)
        self.tt2_lbl_sub3.config(state=NORMAL)
        self.tt2_lbl_sub4.config(state=NORMAL)
        self.tt2_lbl_sub5.config(state=NORMAL)

        self.tt2_lbl_sub1.delete(0, 'end')
        self.tt2_lbl_sub2.delete(0, 'end')
        self.tt2_lbl_sub3.delete(0, 'end')
        self.tt2_lbl_sub4.delete(0, 'end')
        self.tt2_lbl_sub5.delete(0, 'end')

        self.tt2_lbl_sub1.insert(0, subjects[self.count][0])
        self.tt2_lbl_sub2.insert(0, subjects[self.count][1])
        self.tt2_lbl_sub3.insert(0, subjects[self.count][2])
        self.tt2_lbl_sub4.insert(0, subjects[self.count][3])
        self.tt2_lbl_sub5.insert(0, subjects[self.count][4])

        self.tt2_lbl_sub1.config(state='readonly', fg="#0e064d")
        self.tt2_lbl_sub2.config(state='readonly', fg="#0e064d")
        self.tt2_lbl_sub3.config(state='readonly', fg="#0e064d")
        self.tt2_lbl_sub4.config(state='readonly', fg="#0e064d")
        self.tt2_lbl_sub5.config(state='readonly', fg="#0e064d")

        self.tt2_out_sub1.delete(0, 'end')
        self.tt2_out_sub2.delete(0, 'end')
        self.tt2_out_sub3.delete(0, 'end')
        self.tt2_out_sub4.delete(0, 'end')
        self.tt2_out_sub5.delete(0, 'end')

        self.tt2_out_sub1.insert(0, '20')
        self.tt2_out_sub2.insert(0, '20')
        self.tt2_out_sub3.insert(0, '20')
        self.tt2_out_sub4.insert(0, '20')
        self.tt2_out_sub5.insert(0, '20')
        
# ---------------setting the ut subjects
        self.ut_lbl_sub1.config(state=NORMAL)

        self.ut_lbl_sub2.config(state=NORMAL)
        self.ut_lbl_sub3.config(state=NORMAL)
        self.ut_lbl_sub4.config(state=NORMAL)
        self.ut_lbl_sub5.config(state=NORMAL)

        self.ut_lbl_sub1.delete(0, 'end')
        self.ut_lbl_sub2.delete(0, 'end')
        self.ut_lbl_sub3.delete(0, 'end')
        self.ut_lbl_sub4.delete(0, 'end')
        self.ut_lbl_sub5.delete(0, 'end')

        self.ut_lbl_sub1.insert(0, subjects[self.count][0])
        self.ut_lbl_sub2.insert(0, subjects[self.count][1])
        self.ut_lbl_sub3.insert(0, subjects[self.count][2])
        self.ut_lbl_sub4.insert(0, subjects[self.count][3])
        self.ut_lbl_sub5.insert(0, subjects[self.count][4])

        self.ut_lbl_sub1.config(state='readonly', fg="#0e064d")
        self.ut_lbl_sub2.config(state='readonly', fg="#0e064d")
        self.ut_lbl_sub3.config(state='readonly', fg="#0e064d")
        self.ut_lbl_sub4.config(state='readonly', fg="#0e064d")
        self.ut_lbl_sub5.config(state='readonly', fg="#0e064d")

        self.ut_out_sub1.delete(0, 'end')
        self.ut_out_sub2.delete(0, 'end')
        self.ut_out_sub3.delete(0, 'end')
        self.ut_out_sub4.delete(0, 'end')
        self.ut_out_sub5.delete(0, 'end')

        self.ut_out_sub1.insert(0, '100')
        self.ut_out_sub2.insert(0, '100')
        self.ut_out_sub3.insert(0, '100')
        self.ut_out_sub4.insert(0, '100')
        self.ut_out_sub5.insert(0, '100')

    def submit(self):
# -----------getting input 
        self.get_gr_no = self.gr_no.get()
        self.get_tt1_sub1_marks = self.tt1_mark_sub1.get()
        self.get_tt1_sub2_marks = self.tt1_mark_sub2.get()
        self.get_tt1_sub3_marks = self.tt1_mark_sub3.get()
        self.get_tt1_sub4_marks = self.tt1_mark_sub4.get()
        self.get_tt1_sub5_marks = self.tt1_mark_sub5.get()
        
        self.get_tt1_sub1_out = self.tt1_out_sub1.get()
        self.get_tt1_sub2_out = self.tt1_out_sub2.get()
        self.get_tt1_sub3_out = self.tt1_out_sub3.get()
        self.get_tt1_sub4_out = self.tt1_out_sub4.get()
        self.get_tt1_sub5_out = self.tt1_out_sub5.get()

        self.get_tt2_sub1_marks = self.tt2_mark_sub1.get()
        self.get_tt2_sub2_marks = self.tt2_mark_sub2.get()
        self.get_tt2_sub3_marks = self.tt2_mark_sub3.get()
        self.get_tt2_sub4_marks = self.tt2_mark_sub4.get()
        self.get_tt2_sub5_marks = self.tt2_mark_sub5.get()

        self.get_tt2_sub1_out = self.tt2_out_sub1.get()
        self.get_tt2_sub2_out = self.tt2_out_sub2.get()
        self.get_tt2_sub3_out = self.tt2_out_sub3.get()
        self.get_tt2_sub4_out = self.tt2_out_sub4.get()
        self.get_tt2_sub5_out = self.tt2_out_sub5.get()
        
        self.get_ut_sub1_marks = self.ut_mark_sub1.get()
        self.get_ut_sub2_marks = self.ut_mark_sub2.get()
        self.get_ut_sub3_marks = self.ut_mark_sub3.get()
        self.get_ut_sub4_marks = self.ut_mark_sub4.get()
        self.get_ut_sub5_marks = self.ut_mark_sub5.get()
        
        self.get_ut_sub1_out = self.ut_out_sub1.get()
        self.get_ut_sub2_out = self.ut_out_sub2.get()
        self.get_ut_sub3_out = self.ut_out_sub3.get()
        self.get_ut_sub4_out = self.ut_out_sub4.get()
        self.get_ut_sub5_out = self.ut_out_sub5.get()
    
        if(self.get_tt1_sub1_marks=='' or self.get_tt1_sub2_marks=='' or self.get_tt1_sub3_marks=='' or self.get_tt1_sub4_marks=='' or self.get_tt1_sub5_marks=='' or
           self.get_tt2_sub1_marks=='' or self.get_tt2_sub2_marks=='' or self.get_tt2_sub3_marks=='' or self.get_tt2_sub4_marks=='' or self.get_tt2_sub5_marks=='' or
           self.get_ut_sub1_marks=='' or self.get_ut_sub2_marks=='' or self.get_ut_sub3_marks=='' or self.get_ut_sub4_marks=='' or self.get_ut_sub5_marks==''):
           messagebox.showwarning('warn',"All field must be required!")
        else:
# ---------queries
            marks =[[self.get_tt1_sub1_marks, self.get_tt1_sub2_marks, self.get_tt1_sub3_marks, self.get_tt1_sub4_marks, self.get_tt1_sub5_marks ],
                    [self.get_tt2_sub1_marks, self.get_tt2_sub2_marks, self.get_tt2_sub3_marks, self.get_tt2_sub4_marks, self.get_tt2_sub5_marks ],
                    [self.get_ut_sub1_marks, self.get_ut_sub2_marks, self.get_ut_sub3_marks, self.get_ut_sub4_marks, self.get_ut_sub5_marks ],
                   ] 
            sum = 0
            for i in marks[2]:
                sum += int(i)
            cgpa = (sum/5)/9.5
            query = f"update students set {self.sem} = {cgpa}"
            print(query)
            try:
                for i in range(5):
                    query = f"update {self.sem}_{subjects[self.count][i]}_performance set tt1={marks[0][i]} , tt2={marks[1][i]}, ut={marks[2][i]} where gr_no = {self.get_gr_no};"
                    mycursor.execute(query)
                    mydb.commit()
            except Exception as e:
                print(e)
            messagebox.showinfo('message', 'marks inserted sucessfully.')
            self.root.destroy()
            

    # def convertToBinary(self, filename):
    #     with open(filename, 'rb') as f:
    #         binary = f.read()
    #     return binary
    # def upload(self):
    #     try:
    #         # filename= filedialog.askopenfilename(initialdir="/Downloads",title="Select A File ",filetypes=(("png files","*.png"),("all files","*.*")))
    #         # print(filename)
    #         global filename,img
    #         f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
    #         filename = filedialog.askopenfilename(filetypes=f_types)
    #         img = ImageTk.PhotoImage(file=filename)
    #         picture = self.convertToBinary(filename)
    #         query = "insert into img (i, sr,abc, adc, adcd) values (%s, 1,2 ,3,4 );"
    #         # mycursor.execute(query, base64.b64encode(picture))
    #         mycursor.execute(query, picture)
    #         print(query)
    #         mydb.commit()
    #     except Exception as e:
    #         print(e)

        # my_label = Label(self.root,text=self.root.filename).pack()
        # my_image = ImageTk.PhotoImage(Image.open(root.filename))
        # my_image_label = Label(image=my_image).pack()
        # my_btn = Button(root,text="open File")
    

        



root=Tk()
bj=enter_marks(root)
root.mainloop()