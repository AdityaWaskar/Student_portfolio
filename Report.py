from pprint import pprint
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector as sql
from tkcalendar import DateEntry
from extracurriculaum_document import extracurriculaum_document

from show_document import document

mydb = sql.connect(host="localhost", user="root", passwd="", database="SP")
mycursor = mydb.cursor()

subjects =[["EM_1", "EC_1", "EP_1", "BEE", "Mechanics"],
            ["EM_2", "EC_2", "EP_2", "C_Programming", "ED"],
            ["EM_3", "Java", "DSA", "DBMS", "PCE_1"],
            ["EM_4", "Python", "CNND", "OS", "COA"],
            ["Internet_Programming", "CNS", "EEB", "Software_Engineering", "PCE_2"],
            ["Data_Mining", "Web_X", "Wireless_Technology", "AI_and_DS", "Ethical_Hacking"],
            ["Enterprise_Network_Design", "Infrastruction_Security","Soft_computing", "Cyber_security_and_Law", "AI"],
            ["Big_data_analytics", "Big_data_analytics", "Internet_of_Everything", "R_Programming", "Robotics" , "Project_management"]]
class report:
    def __init__(self,root):
# --------------variable
        self.sem = 'sem1'
        self.count = 0
# ---------------frame root
        self.root=root
        self.root.title("Student Result ")
        self.root.geometry("1520x820+0+6")
        self.root.config(bg="white")
        self.root.focus_force()
# -------------------------title
        title=Label(self.root,text="View Student Results",font=("times new roman",20,"bold"),bg="orange",fg="white").place(x=20,y=15,width=1500,height=50)
# -------------------------search box
        self.var_search=StringVar()
        gr_no=Label(self.root, text="Search by GR no.", justify=CENTER,font=("times new roman",15),bg="white").place(x=150,y=100)
        self.gr_no=Entry(self.root,textvariable=self.var_search,justify=CENTER,font=("times new roman",15),bg="lightyellow")
        self.gr_no.place(x=300,y=100,width=150)
        lbl_dob=Label(self.root,text="DOB.",font=("times new roman",15),bg="white").place(x=500,y=100)
        self.dob=DateEntry(self.root, selectmode="day",date_pattern = 'dd/mm/yyyy',background="blue",Cursor="hand1",year=2003, month=1,foreground='black', font=("Arial", 12))
        self.dob.place(x=560,y=100,width=150)
        self.btn_search=Button(self.root,text='Search', command=self.search_by_gr,justify=CENTER,font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2")
        self.btn_search.place(x=820,y=100,width=100,height=35)
        self.btn_clear=Button(self.root,text='Clear',command=self.clear,justify=CENTER,font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2")
        self.btn_clear.place(x=940,y=100,width=100,height=35)

        self.m_Frame = LabelFrame(self.root, text= "Semester", font=("times new roman", 15), bg="white")
        

        self.btn_sem1 = Button(self.m_Frame, text="Sem 1", command=self.set_subject1, cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white")
        self.btn_sem2 = Button(self.m_Frame, text="Sem 2", command=self.set_subject2, cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white")
        self.btn_sem3 = Button(self.m_Frame, text="Sem 3", command=self.set_subject3, cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white")
        self.btn_sem4 = Button(self.m_Frame, text="Sem 4", command=self.set_subject4, cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white")
        self.btn_sem5 = Button(self.m_Frame, text="Sem 5", command=self.set_subject5, cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white")
        self.btn_sem6 = Button(self.m_Frame, text="Sem 6", command=self.set_subject6, cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white")
        self.btn_sem7 = Button(self.m_Frame, text="Sem 7", command=self.set_subject7, cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white")
        self.btn_sem8 = Button(self.m_Frame, text="Sem 8", command=self.set_subject8, cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white")
# -------------------tt1 entry boxes
        self.tt1_lbl=Label(self.root,text="TERM TEST 1",justify=CENTER,font=("goudy old style",15,"bold"),bg="white")
        self.tt1_lbl.place(x=100,y=250)
        self.tt1_lbl_sub1=Entry(self.root, justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt1_lbl_sub1.place(x=350-250,y=280,width=150,height=50)
        self.tt1_lbl_sub2=Entry(self.root, justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt1_lbl_sub2.place(x=500-250,y=280,width=150,height=50)
        self.tt1_lbl_sub3=Entry(self.root, justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt1_lbl_sub3.place(x=650-250,y=280,width=150,height=50)
        self.tt1_lbl_sub4=Entry(self.root, justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt1_lbl_sub4.place(x=800-250,y=280,width=150,height=50)
        self.tt1_lbl_sub5=Entry(self.root, justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt1_lbl_sub5.place(x=950-250,y=280,width=150,height=50)

        self.tt1_sub1=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt1_sub1.place(x=350-250,y=320,width=150,height=50)
        self.tt1_sub2=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt1_sub2.place(x=500-250,y=320,width=150,height=50)
        self.tt1_sub3=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt1_sub3.place(x=650-250,y=320,width=150,height=50)
        self.tt1_sub4=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt1_sub4.place(x=800-250,y=320,width=150,height=50)
        self.tt1_sub5=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt1_sub5.place(x=950-250,y=320,width=150,height=50)

# -------------------------tt2 entry boxes
        lbl_tt1=Label(self.root,text="TERM TEST 2",justify=CENTER,font=("goudy old style",15,"bold"),bg="white").place(x=100,y=400)
        self.tt2_lbl_sub1=Entry(self.root,text="SUB 1",justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt2_lbl_sub1.place(x=350-250,y=430,width=150,height=50)
        self.tt2_lbl_sub2=Entry(self.root,text="SUB 2",justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt2_lbl_sub2.place(x=500-250,y=430,width=150,height=50)
        self.tt2_lbl_sub3=Entry(self.root,text="SUB 3",justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt2_lbl_sub3.place(x=650-250,y=430,width=150,height=50)
        self.tt2_lbl_sub4=Entry(self.root,text="SUB 4",justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt2_lbl_sub4.place(x=800-250,y=430,width=150,height=50)
        self.tt2_lbl_sub5=Entry(self.root,text="SUB 5",justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt2_lbl_sub5.place(x=950-250,y=430,width=150,height=50)

        self.tt2_sub1=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt2_sub1.place(x=350-250,y=470,width=150,height=50)
        self.tt2_sub2=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt2_sub2.place(x=500-250,y=470,width=150,height=50)
        self.tt2_sub3=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt2_sub3.place(x=650-250,y=470,width=150,height=50)
        self.tt2_sub4=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt2_sub4.place(x=800-250,y=470,width=150,height=50)
        self.tt2_sub5=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt2_sub5.place(x=950-250,y=470,width=150,height=50)
        
# ------------------------------Semester entry boxes
        ut_lbl_tt1=Label(self.root,text="SEMESTER",justify=CENTER,font=("goudy old style",15,"bold"),bg="white").place(x=100,y=550)
        self.ut_lbl_sub1=Entry(self.root,text="SUB 1",justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.ut_lbl_sub1.place(x=350-250,y=580,width=150,height=50)
        self.ut_lbl_sub2=Entry(self.root,text="SUB 2",justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.ut_lbl_sub2.place(x=500-250,y=580,width=150,height=50)
        self.ut_lbl_sub3=Entry(self.root,text="SUB 3",justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.ut_lbl_sub3.place(x=650-250,y=580,width=150,height=50)
        self.ut_lbl_sub4=Entry(self.root,text="SUB 4",justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.ut_lbl_sub4.place(x=800-250,y=580,width=150,height=50)
        self.ut_lbl_sub5=Entry(self.root,text="SUB 5",justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.ut_lbl_sub5.place(x=950-250,y=580,width=150,height=50)

        self.ut_sub1=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.ut_sub1.place(x=350-250,y=620,width=150,height=50)
        self.ut_sub2=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.ut_sub2.place(x=500-250,y=620,width=150,height=50)
        self.ut_sub3=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.ut_sub3.place(x=650-250,y=620,width=150,height=50)
        self.ut_sub4=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.ut_sub4.place(x=800-250,y=620,width=150,height=50)
        self.ut_sub5=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.ut_sub5.place(x=950-250,y=620,width=150,height=50)

# ----------------information
        self.m1_Frame = LabelFrame(self.root, text= "DETAILS", font=("times new roman", 15), bg="white")
        self.m1_Frame.place(x=900, y=300, width=550, height=330)

        lbl_gr_no = Label(self.m1_Frame, text="Gr No. =", cursor="hand2",font=("goudy lod style",15), bg="white", fg="black").place(x=140-80, y=30, width=100, height=30)
        self.lbl_gr_no = Label(self.m1_Frame,font=("times new roman",15), bg="white", fg="#0b5377")
        self.lbl_gr_no.place(x=250-80, y=30, width=250, height=30)
        
               
        lbl_name = Label(self.m1_Frame, text="Name =", cursor="hand2",font=("goudy lod style",15), bg="white", fg="black").place(x=140-80, y=70, width=100, height=30)
        self.lbl_name = Label(self.m1_Frame,font=("times new roman",15), bg="white", fg="#0b5377")
        self.lbl_name.place(x=250-80, y=70, width=250, height=30)
        

        lbl_dob = Label(self.m1_Frame, text="DOB =", cursor="hand2",font=("goudy lod style",15), bg="white", fg="black").place(x=140-80, y=110, width=100, height=30)
        self.lbl_dob = Label(self.m1_Frame,font=("times new roman",15), bg="white", fg="#0b5377")
        self.lbl_dob.place(x=250-80, y=110, width=250, height=30)
       

        lbl_email = Label(self.m1_Frame, text="Email =", cursor="hand2",font=("goudy lod style",15), bg="white", fg="black").place(x=140-80, y=150, width=100, height=30)
        self.lbl_email = Label(self.m1_Frame,font=("times new roman",15), bg="white", fg="#0b5377")
        self.lbl_email.place(x=250-80, y=150, width=250, height=30)
        

        lbl_sem = Label(self.m1_Frame, text="Semester =", cursor="hand2",font=("goudy lod style",15), bg="white", fg="black").place(x=140-80, y=190, width=100, height=30)
        self.lbl_sem = Label(self.m1_Frame,font=("times new roman",15), bg="white", fg="#0b5377")
        self.lbl_sem.place(x=250-80, y=190, width=250, height=30)
        
        lbl_pointer = Label(self.m1_Frame, text="POINTER=", cursor="hand2",font=("goudy lod style",15), bg="white", fg="black").place(x=140-80, y=230, width=100, height=30)
        self.lbl_pointer = Label(self.m1_Frame,font=("times new roman",15), bg="white", fg="#0b5377")
        self.lbl_pointer.place(x=250-80, y=230, width=250, height=30)
    
        self.document = Button(self.root,bd=0,text='See the uploaded documents(Result).',bg="white",command = self.show_document ,justify=CENTER,font=("goudy old style",13,"bold","underline"),fg="orange",cursor="hand2")
        self.extra_activity_document_tech = Button(self.root,bd=0,text='See the curriculum technical activity documents.',bg="white",command = self.show_extra_curriculm_tech_document ,justify=CENTER,font=("goudy old style",13,"bold","underline"),fg="orange",cursor="hand2")
        self.extra_activity_document_non_tech = Button(self.root,bd=0,text='See the curriculum non technical activity documents.',bg="white",command = self.show_extra_curriculm__non_tech_document,justify=CENTER,font=("goudy old style",13,"bold","underline"),fg="orange",cursor="hand2")

# -------------------------methods

    def search_by_gr(self):
        self.get_gr_no = self.gr_no.get()
        self.get_dob = self.dob.get()
        if(self.get_gr_no == ''):
            messagebox.showerror('error', 'Enter gr no')
        elif(self.get_dob == ''):
            messagebox.showerror('error', 'Enter dob no')
        else:
            query = f"select sem from students where gr_no = {self.get_gr_no} and dob = '{self.get_dob}';"
            print(query)
            mycursor.execute(query)
            self.get_sem = mycursor.fetchone()
            if(self.get_sem):
                self.show_sem()    
                self.m_Frame.place(x=80, y=150, width=1380, height=80)
            else:
                messagebox.showinfo('message', 'gr_no and dob no match!')    

    def get_marks(self):
        self.list = []
        for i in range(5): 
            try:   
                query1 = f"select tt1, tt2, ut from {self.sem}_{subjects[self.count][i]}_performance where gr_no = {self.get_gr_no};"
                print(query1)
                mycursor.execute(query1)
                result = mycursor.fetchall()
                self.list.append(result[0])
            except :
                messagebox.showerror("error", "Please Enter your marks.")
            

        '''query = f"update {self.sem}_{subjects[self.count][i]}_performance set tt1={marks[0][i]} , tt2={marks[1][i]}, ut={marks[2][i]} where gr_no = {self.get_gr_no};"
                    mycursor.execute(query)'''
        print(self.list)

    def show_sem(self):
        query = f"select sem from students where gr_no = {self.gr_no.get()}"
        mycursor.execute(query)
        result = mycursor.fetchone()
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
        self.count = 0
        self.sem = 'sem1'
        self.get_marks()
        self.set()
        self.show_information()
        
    def set_subject2(self):
        self.extra_activity_document_tech.place(x=65000,y=730,width=400,height=35)
        self.extra_activity_document_non_tech.place(x=65000,y=760,width=400,height=35)
        self.count = 1
        self.sem = 'sem2'
        self.get_marks()
        self.set()
        self.show_information()
    def set_subject3(self):
        self.extra_activity_document_tech.place(x=65000,y=730,width=400,height=35)
        self.extra_activity_document_non_tech.place(x=65000,y=760,width=400,height=35)
        self.count = 2
        self.sem = 'sem3'
        self.get_marks()
        self.set()
        self.show_information()
    def set_subject4(self):
        self.extra_activity_document_tech.place(x=65000,y=730,width=400,height=35)
        self.extra_activity_document_non_tech.place(x=65000,y=760,width=400,height=35)
        self.count = 3
        self.sem = 'sem4'
        self.get_marks()
        self.set()
        self.show_information()
        self.extra_activity_document_tech.place(x=65000,y=730,width=400,height=35)
        self.extra_activity_document_non_tech.place(x=65000,y=760,width=400,height=35)
    def set_subject5(self):
        self.count = 4
        self.sem = 'sem5'
        self.set()
        self.show_information()
        self.extra_activity_document_tech.place(x=65000,y=730,width=400,height=35)
        self.extra_activity_document_non_tech.place(x=65000,y=760,width=400,height=35)
    def set_subject6(self):
        self.count = 5
        self.sem = 'sem6'
        self.set()
        self.show_information()
        self.extra_activity_document_tech.place(x=65000,y=730,width=400,height=35)
        self.extra_activity_document_non_tech.place(x=65000,y=760,width=400,height=35)
    def set_subject7(self):
        self.count = 6
        self.sem = 'sem7'
        self.set()
        self.show_information()
        self.extra_activity_document_tech.place(x=65000,y=730,width=400,height=35)
        self.extra_activity_document_non_tech.place(x=65000,y=760,width=400,height=35)
    def set_subject8(self):
        self.count = 7
        self.sem = 'sem8'
        self.set()
        self.show_information()
    def show_information(self):
# Placing the buttons 
        self.document.place(x=650,y=700,width=400,height=35)
        query = f"select technical_event, non_technical_event from students where gr_no={self.gr_no.get()};"
        mycursor.execute(query)
        result= mycursor.fetchone()
        print(result[0], result[1])
        if(result[0] != None): 
            self.extra_activity_document_tech.place(x=650,y=730,width=400,height=35)
            print(":)")
        if(result[1] != None):
            self.extra_activity_document_non_tech.place(x=650,y=760,width=400,height=35)
            print("(:")



        query = f"select * from {self.sem}_students where gr_no ={self.get_gr_no};"
        mycursor.execute(query)
        result = mycursor.fetchall()
        query1 = f"select {self.sem} from students where gr_no ={self.get_gr_no};"
        mycursor.execute(query1)
        result1 = mycursor.fetchall()
        print(result)

        self.lbl_gr_no.config(text = result[0][0])
        self.lbl_name.config(text = result[0][2])
        self.lbl_dob.config(text = result[0][3])
        self.lbl_email.config(text = result[0][4])
        self.lbl_sem.config(text = self.sem)
        self.lbl_pointer.config(text = result1[0][0])
    def set(self):
# --------------------making all labels normal
        self.tt1_lbl_sub1.config(state=NORMAL)
        self.tt1_lbl_sub2.config(state=NORMAL)
        self.tt1_lbl_sub3.config(state=NORMAL)
        self.tt1_lbl_sub4.config(state=NORMAL)
        self.tt1_lbl_sub5.config(state=NORMAL)
        self.tt1_sub1.config(state=NORMAL)
        self.tt1_sub2.config(state=NORMAL)
        self.tt1_sub3.config(state=NORMAL)
        self.tt1_sub4.config(state=NORMAL)
        self.tt1_sub5.config(state=NORMAL)
    
        self.tt2_lbl_sub1.config(state=NORMAL)
        self.tt2_lbl_sub2.config(state=NORMAL)
        self.tt2_lbl_sub3.config(state=NORMAL)
        self.tt2_lbl_sub4.config(state=NORMAL)
        self.tt2_lbl_sub5.config(state=NORMAL)
        self.tt2_sub1.config(state=NORMAL)
        self.tt2_sub2.config(state=NORMAL)
        self.tt2_sub3.config(state=NORMAL)
        self.tt2_sub4.config(state=NORMAL)
        self.tt2_sub5.config(state=NORMAL)

        self.ut_lbl_sub1.config(state=NORMAL)
        self.ut_lbl_sub2.config(state=NORMAL)
        self.ut_lbl_sub3.config(state=NORMAL)
        self.ut_lbl_sub4.config(state=NORMAL)
        self.ut_lbl_sub5.config(state=NORMAL)
        self.ut_sub1.config(state=NORMAL)
        self.ut_sub2.config(state=NORMAL)
        self.ut_sub3.config(state=NORMAL)
        self.ut_sub4.config(state=NORMAL)
        self.ut_sub5.config(state=NORMAL)

# ----------------deleting the content in the label and entry
        self.tt1_lbl_sub1.delete(0, 'end')
        self.tt1_lbl_sub2.delete(0, 'end')
        self.tt1_lbl_sub3.delete(0, 'end')
        self.tt1_lbl_sub4.delete(0, 'end')
        self.tt1_lbl_sub5.delete(0, 'end')
        self.tt1_sub1.delete(0, 'end')
        self.tt1_sub2.delete(0, 'end')
        self.tt1_sub3.delete(0, 'end')
        self.tt1_sub4.delete(0, 'end')
        self.tt1_sub5.delete(0, 'end')

        self.tt2_lbl_sub1.delete(0, 'end')
        self.tt2_lbl_sub2.delete(0, 'end')
        self.tt2_lbl_sub3.delete(0, 'end')
        self.tt2_lbl_sub4.delete(0, 'end')
        self.tt2_lbl_sub5.delete(0, 'end')
        self.tt2_sub1.delete(0, 'end')
        self.tt2_sub2.delete(0, 'end')
        self.tt2_sub3.delete(0, 'end')
        self.tt2_sub4.delete(0, 'end')
        self.tt2_sub5.delete(0, 'end')
        
        self.ut_lbl_sub1.delete(0, 'end')
        self.ut_lbl_sub2.delete(0, 'end')
        self.ut_lbl_sub3.delete(0, 'end')
        self.ut_lbl_sub4.delete(0, 'end')
        self.ut_lbl_sub5.delete(0, 'end')
        self.ut_sub1.delete(0, 'end')
        self.ut_sub2.delete(0, 'end')
        self.ut_sub3.delete(0, 'end')
        self.ut_sub4.delete(0, 'end')
        self.ut_sub5.delete(0, 'end')




# -----------Inserting the subject name

        self.tt1_lbl_sub1.insert(0, subjects[self.count][0])
        self.tt1_lbl_sub2.insert(0, subjects[self.count][1])
        self.tt1_lbl_sub3.insert(0, subjects[self.count][2])
        self.tt1_lbl_sub4.insert(0, subjects[self.count][3])
        self.tt1_lbl_sub5.insert(0, subjects[self.count][4])

        self.tt2_lbl_sub1.insert(0, subjects[self.count][0])
        self.tt2_lbl_sub2.insert(0, subjects[self.count][1])
        self.tt2_lbl_sub3.insert(0, subjects[self.count][2])
        self.tt2_lbl_sub4.insert(0, subjects[self.count][3])
        self.tt2_lbl_sub5.insert(0, subjects[self.count][4])

        # self.ut_lbl_sub1.insert(0, subjects[self.count][0])
        # self.ut_lbl_sub2.insert(0, subjects[self.count][1])
        # self.ut_lbl_sub3.insert(0, subjects[self.count][2])
        # self.ut_lbl_sub4.insert(0, subjects[self.count][3])
        # self.ut_lbl_sub5.insert(0, subjects[self.count][4])

# ----------------inserting the subject marks
        try:
            self.tt1_sub1.insert(0, self.list[0][0])
            self.tt1_sub2.insert(0, self.list[1][0])
            self.tt1_sub3.insert(0, self.list[2][0])
            self.tt1_sub4.insert(0, self.list[3][0])
            self.tt1_sub5.insert(0, self.list[4][0])

            self.tt2_sub1.insert(0, self.list[0][1])
            self.tt2_sub2.insert(0, self.list[1][1])
            self.tt2_sub3.insert(0, self.list[2][1])
            self.tt2_sub4.insert(0, self.list[3][1])
            self.tt2_sub5.insert(0, self.list[4][1])

            self.ut_sub1.insert(0, self.list[0][2])
            self.ut_sub2.insert(0, self.list[1][2])
            self.ut_sub3.insert(0, self.list[2][2])
            self.ut_sub4.insert(0, self.list[3][2])
            self.ut_sub5.insert(0, self.list[4][2])
        except:
            messagebox.showerror("error", "Enter your marks first!", parent=self.root)
        
# ---------------------remove the normal state in the label and entry
        self.tt1_lbl_sub1.config(state='readonly', fg='#18258c')
        self.tt1_lbl_sub2.config(state='readonly', fg='#18258c')
        self.tt1_lbl_sub3.config(state='readonly', fg='#18258c')
        self.tt1_lbl_sub4.config(state='readonly', fg='#18258c')
        self.tt1_lbl_sub5.config(state='readonly', fg='#18258c')
        self.tt1_sub1.config(state='readonly')
        self.tt1_sub2.config(state='readonly')
        self.tt1_sub3.config(state='readonly')
        self.tt1_sub4.config(state='readonly')
        self.tt1_sub5.config(state='readonly')
        
        self.tt2_lbl_sub1.config(state='readonly', fg='#18258c')
        self.tt2_lbl_sub2.config(state='readonly', fg='#18258c')
        self.tt2_lbl_sub3.config(state='readonly', fg='#18258c')
        self.tt2_lbl_sub4.config(state='readonly', fg='#18258c')
        self.tt2_lbl_sub5.config(state='readonly', fg='#18258c')
        self.tt2_sub1.config(state='readonly')
        self.tt2_sub2.config(state='readonly')
        self.tt2_sub3.config(state='readonly')
        self.tt2_sub4.config(state='readonly')
        self.tt2_sub5.config(state='readonly')

        self.ut_lbl_sub1.config(state='readonly', fg='#18258c')
        self.ut_lbl_sub2.config(state='readonly', fg='#18258c')
        self.ut_lbl_sub3.config(state='readonly', fg='#18258c')
        self.ut_lbl_sub4.config(state='readonly', fg='#18258c')
        self.ut_lbl_sub5.config(state='readonly', fg='#18258c')
        self.ut_sub1.config(state='readonly')
        self.ut_sub2.config(state='readonly')
        self.ut_sub3.config(state='readonly')
        self.ut_sub4.config(state='readonly')
        self.ut_sub5.config(state='readonly')

    def show_document(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = document(self.new_win, self.gr_no.get(),self.sem)
    
     
    def show_extra_curriculm_tech_document(self):
        self.new_win1 = Toplevel(self.root)
        self.new_obj1 = extracurriculaum_document(self.new_win1, self.gr_no.get(), "technical_event")
    
    def show_extra_curriculm__non_tech_document(self):
        self.new_win1 = Toplevel(self.root)
        self.new_obj1 = extracurriculaum_document(self.new_win1, self.gr_no.get(), "non_technical_event")
        
        # self.new_obj = extracurriculaum_document(self.new_win, self.gr_no.get(),self.destination, self.category.get())

    def clear(self):
        self.root.destroy()
        root=Tk()
        bj=report(root)
        root.mainloop()
                



if (__name__=="__main__"):
    root=Tk()
    bj=report(root)
    root.mainloop()
