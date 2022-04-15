from tkinter import*
from tkinter import ttk,messagebox
import mysql.connector as sql
from tkcalendar import DateEntry
import shutil
from tkinter import Tk, filedialog

mydb = sql.connect(host="localhost", user="root", passwd="", database="SP")
mycursor = mydb.cursor()

subjects =[["EM_1", "EC_1", "EP_1", "BEE", "Mechanics"],
            ["EM_2", "EC_2", "EP_2", "C_Programming", "ED"],
            ["EM_3", "Java", "DSA", "DBMS", "PCE_1"],
            ["EM_4", "Python", "CNND", "OS", "COA"],
            ["Data_Mining", "Web_X", "Wireless_Technology", "AI_and_DS", "Ethical_Hacking"],
            ["Internet_Programming", "CNS", "EEB", "Software_Engineering", "PCE_2"],
            ["Enterprise_Network_Design", "Infrastruction_Security","Soft_computing", "Cyber_security_and_Law", "AI"],
            ["Big_data_analytics", "Big_data_analytics", "Internet_of_Everything", "R_Programming", "Robotics" , "Project_management"]]

class enter_marks:
    def __init__(self,root):
        self.root=root
        self.root.title("Enter Marks ")
        self.root.geometry("1520x820+0+6")
        self.root.config(bg="white")
        self.root.focus_force()
        self.root.grab_set()
        self.count = -1
        #================title===================
        title=Label(self.root,text="Enter Your Marks",font=("times new roman",20,"bold"),bg="orange",fg="white").place(x=20,y=15,width=1500,height=50)

        #==============search=============
        self.var_search=StringVar()
        gr_no=Label(self.root,text="Enter Gr No.",font=("times new roman",15),bg="white").place(x=140,y=100)
        self.gr_no=Entry(self.root,textvariable=self.var_search,justify=CENTER,font=("times new roman",15),bg="lightyellow")
        self.gr_no.place(x=280,y=100,width=150)
        lbl_dob=Label(self.root,text="DOB.",font=("times new roman",15),bg="white").place(x=500,y=100)
        self.dob=DateEntry(self.root, selectmode="day",date_pattern = 'dd/mm/yyyy',background="blue",Cursor="hand1",year=2003, month=1,foreground='black', font=("Arial", 12))
        self.dob.place(x=560,y=100,width=150)
        btn_search=Button(self.root,text='Search',command=self.search,font=("times new roman",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2").place(x=800,y=100,width=100,height=35)
        btn_clear=Button(self.root,text='Clear',font=("times new roman",15,"bold"),bg="gray",fg="white",cursor="hand2").place(x=920,y=100,width=100,height=35)
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
        self.tt1_lbl_sub1.place(x=140, y=30, width=100, height=30)
        self.tt1_mark_sub1 = Entry(self.m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_mark_sub1.place(x=250, y=30, width=100, height=30)
        self.slash = Label(self.m1_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=360, y=30, width=10, height=30)
        self.tt1_out_sub1 = Entry(self.m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_out_sub1.place(x=380, y=30, width=100, height=30)

        self.tt1_lbl_sub2 = Entry(self.m1_Frame, text="Sub 2", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt1_lbl_sub2.place(x=140, y=70, width=100, height=30)
        self.tt1_mark_sub2 = Entry(self.m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_mark_sub2.place(x=250, y=70, width=100, height=30)
        self.slash = Label(self.m1_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=360, y=70, width=10, height=30)
        self.tt1_out_sub2 = Entry(self.m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_out_sub2.place(x=380, y=70, width=100, height=30)

        self.tt1_lbl_sub3 = Entry(self.m1_Frame, text="Sub 3", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt1_lbl_sub3.place(x=140, y=110, width=100, height=30)
        self.tt1_mark_sub3 = Entry(self.m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_mark_sub3.place(x=250, y=110, width=100, height=30)
        self.slash = Label(self.m1_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black").place(x=360, y=110, width=10, height=30)
        self.tt1_out_sub3 = Entry(self.m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_out_sub3.place(x=380, y=110, width=100, height=30)
       
        self.tt1_lbl_sub4 = Entry(self.m1_Frame, text="Sub 4", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt1_lbl_sub4.place(x=140, y=150, width=100, height=30)
        self.tt1_mark_sub4 = Entry(self.m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_mark_sub4.place(x=250, y=150, width=100, height=30)
        self.slash = Label(self.m1_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black").place(x=360, y=150, width=10, height=30)
        self.tt1_out_sub4 = Entry(self.m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_out_sub4.place(x=380, y=150, width=100, height=30)

        self.tt1_lbl_sub5 = Entry(self.m1_Frame, text="Sub 5", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt1_lbl_sub5.place(x=140, y=190, width=100, height=30)
        self.tt1_mark_sub5 = Entry(self.m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_mark_sub5.place(x=250, y=190, width=100, height=30)
        self.slash = Label(self.m1_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black").place(x=360, y=190, width=10, height=30)
        self.tt1_out_sub5 = Entry(self.m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_out_sub5.place(x=380, y=190, width=100, height=30)

       #==============================tt2==========================
        self.m2_Frame = LabelFrame(self.root, text= "TERM TEST 2", font=("times new roman", 15), bg="white")
        

        self.tt2_lbl_sub1 = Entry(self.m2_Frame, text="Sub 1", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt2_lbl_sub1.place(x=140, y=30, width=100, height=30)
        self.tt2_mark_sub1 = Entry(self.m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_mark_sub1.place(x=250, y=30, width=100, height=30)
        self.slash = Label(self.m2_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=360, y=30, width=10, height=30)
        self.tt2_out_sub1 = Entry(self.m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_out_sub1.place(x=380, y=30, width=100, height=30)
        
        self.tt2_lbl_sub2 = Entry(self.m2_Frame, text="Sub 2", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt2_lbl_sub2.place(x=140, y=70, width=100, height=30)
        self.tt2_mark_sub2 = Entry(self.m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_mark_sub2.place(x=250, y=70, width=100, height=30)
        self.slash = Label(self.m2_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=360, y=70, width=10, height=30)
        self.tt2_out_sub2 = Entry(self.m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_out_sub2.place(x=380, y=70, width=100, height=30)
        
        
        self.tt2_lbl_sub3  = Entry(self.m2_Frame, text="Sub 3", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt2_lbl_sub3.place(x=140, y=110, width=100, height=30)
        self.tt2_mark_sub3  = Entry(self.m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_mark_sub3.place(x=250, y=110, width=100, height=30)
        self.slash  = Label(self.m2_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=360, y=110, width=10, height=30)
        self.tt2_out_sub3  = Entry(self.m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_out_sub3.place(x=380, y=110, width=100, height=30)
        
        
        self.tt2_lbl_sub4 = Entry(self.m2_Frame, text="Sub 4", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt2_lbl_sub4.place(x=140, y=150, width=100, height=30)
        self.tt2_mark_sub4 = Entry(self.m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_mark_sub4 .place(x=250, y=150, width=100, height=30)
        self.slash = Label(self.m2_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=360, y=150, width=10, height=30)
        self.tt2_out_sub4 = Entry(self.m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_out_sub4.place(x=380, y=150, width=100, height=30)
        
        self.tt2_lbl_sub5= Entry(self.m2_Frame, text="Sub 5", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt2_lbl_sub5.place(x=140, y=190, width=100, height=30)
        self.tt2_mark_sub5 = Entry(self.m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_mark_sub5.place(x=250, y=190, width=100, height=30)
        self.slash = Label(self.m2_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=360, y=190, width=10, height=30)
        self.tt2_out_sub5 = Entry(self.m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_out_sub5.place(x=380, y=190, width=100, height=30)
        

       #==================semester===============
        self.m3_Frame = LabelFrame(self.root, text= "SEMESTER", font=("times new roman", 15), bg="white")
        

        self.ut_lbl_sub1= Entry(self.m3_Frame, text="Sub 1", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.ut_lbl_sub1.place(x=140, y=30, width=100, height=30)
        self.ut_mark_sub1 = Entry(self.m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_mark_sub1.place(x=250, y=30, width=100, height=30)
        self.slash = Label(self.m3_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=360, y=30, width=10, height=30)
        self.ut_out_sub1 = Entry(self.m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_out_sub1.place(x=380, y=30, width=100, height=30)
        
        self.ut_lbl_sub2 = Entry(self.m3_Frame, text="Sub 2", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.ut_lbl_sub2.place(x=140, y=70, width=100, height=30)
        self.ut_mark_sub2 = Entry(self.m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_mark_sub2.place(x=250, y=70, width=100, height=30)
        self.slash = Label(self.m3_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=360, y=70, width=10, height=30)
        self.ut_out_sub2 = Entry(self.m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_out_sub2.place(x=380, y=70, width=100, height=30)
        
        self.ut_lbl_sub3 = Entry(self.m3_Frame, text="Sub 3", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.ut_lbl_sub3.place(x=140, y=110, width=100, height=30)
        self.ut_mark_sub3 = Entry(self.m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_mark_sub3.place(x=250, y=110, width=100, height=30)
        self.slash = Label(self.m3_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=360, y=110, width=10, height=30)
        self.ut_out_sub3 = Entry(self.m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_out_sub3.place(x=380, y=110, width=100, height=30)
        
        self.ut_lbl_sub4 = Entry(self.m3_Frame, text="Sub 4", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.ut_lbl_sub4.place(x=140, y=150, width=100, height=30)
        self.ut_mark_sub4 = Entry(self.m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_mark_sub4.place(x=250, y=150, width=100, height=30)
        self.slash = Label(self.m3_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=360, y=150, width=10, height=30)
        self.ut_out_sub4 = Entry(self.m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_out_sub4.place(x=380, y=150, width=100, height=30)
        
        self.ut_lbl_sub5 = Entry(self.m3_Frame, text="Sub 5", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.ut_lbl_sub5.place(x=140, y=190, width=100, height=30)
        self.ut_mark_sub5 = Entry(self.m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_mark_sub5.place(x=250, y=190, width=100, height=30)
        self.slash = Label(self.m3_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=360, y=190, width=10, height=30)
        self.ut_out_sub5 = Entry(self.m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_out_sub5.place(x=380, y=190, width=100, height=30)

        self.upload = Button(self.root,text='Upload',font=("times new roman",15,"bold"),command = self.upload,bg="#03a9f4",fg="white",cursor="hand2")
        self.upload_warn = Label(self.root, bg= "white", fg="red", justify=CENTER)

# ---------progress bar 
        self.progress = ttk.Progressbar(self.root, orient = HORIZONTAL,length = 100, mode = 'determinate')

    def search(self):
        self.get_gr_no = self.gr_no.get()
        self.get_dob = self.dob.get()
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
        self.progress['value'] = 0
        self.sem = 'sem1'
        self.count = 0
        self.set()
    def set_subject2(self):
        self.progress['value'] = 0
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
        self.upload.place(x=1350,y=700,width=100,height=35)
        self.upload_warn.config(text="*upload your result in pdf file.", fg= "red")
        self.upload_warn.place(x=1340 ,y=750)
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
            query1 = f"update students set {self.sem} = {cgpa}"
            mycursor.execute(query1)
            mydb.commit()
            try:
                for i in range(5):
                    query = f"update {self.sem}_{subjects[self.count][i]}_performance set tt1={marks[0][i]} , tt2={marks[1][i]}, ut={marks[2][i]} where gr_no = {self.get_gr_no};"
                    mycursor.execute(query)
                    mydb.commit()
            except Exception as e:
                print(e)
            messagebox.showinfo('message', 'marks inserted sucessfully.')
            self.root.destroy()    
  
    def upload(self):
        if(self.tt1_mark_sub1.get()=='' or self.tt1_mark_sub2.get()=='' or self.tt1_mark_sub3.get()=='' or self.tt1_mark_sub4.get()=='' or self.tt1_mark_sub5.get()=='' or
           self.tt2_mark_sub1.get()=='' or self.tt2_mark_sub2.get()=='' or self.tt2_mark_sub3.get()=='' or self.tt2_mark_sub4.get()=='' or self.tt2_mark_sub5.get()=='' or
           self.ut_mark_sub1.get()=='' or self.ut_mark_sub2.get()=='' or self.ut_mark_sub3.get()=='' or self.ut_mark_sub4.get()=='' or self.ut_mark_sub5.get()==''):
            messagebox.showerror("error", "All field must be required!")
        else:
# --------------open the directory
            f_types =[('jpg files','*.jpg')]
            source = filedialog.askopenfilename(filetypes=f_types)
# --------------upload the filepath to database
            if(source == ""):
                print("no")
                self.upload_warn.place(x=1340, y=750)
            else:
                destination = f"E:/python/project/Student Portfoilo/student_documents/results/Information Technology/{self.sem}/{self.get_gr_no}.jpg"
                dest = shutil.copy(source, destination)
                self.bar()
                self.upload_warn.config(text="Sucessfully Uploaded", fg="green")
                self.upload_warn.place(x=1340 ,y=750)
                try:
                    query = f"UPDATE {self.sem}_students set result_path = '{destination}' WHERE gr_no = {self.gr_no.get()} ;"
                    mycursor.execute(query)
                    mydb.commit()
                except Exception as e:
                    print("some error to upload the file!")

# -----------progress bar running method
    def bar(self):
            self.progress.place(x=1350,y=740, height=10)
            import time
            self.progress['value'] = 20
            root.update_idletasks()
            time.sleep(1)

            self.progress['value'] = 40
            root.update_idletasks()
            time.sleep(1)

            self.progress['value'] = 50
            root.update_idletasks()
            time.sleep(1)

            self.progress['value'] = 60
            root.update_idletasks()
            time.sleep(1)

            self.progress['value'] = 80
            root.update_idletasks()
            time.sleep(1)
            self.progress['value'] = 100


if __name__ == "__main__":
    root=Tk()
    obj=enter_marks(root)
    root.mainloop()