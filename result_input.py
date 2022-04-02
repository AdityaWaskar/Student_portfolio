from cProfile import label
from cgitb import text
from email.mime import image
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from tkinter import filedialog

subjects =[["EM_1", "EC_1", "EP_1", "BEE", "Mechanics_1"],
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
        lbl_search=Label(self.root,text="ENTER GR NO.",font=("times new roman",15,"bold"),bg="white").place(x=140,y=100)
        mark_search=Entry(self.root,textvariable=self.var_search,font=("times new roman",20),bg="lightyellow").place(x=340,y=100,width=150)
        btn_search=Button(self.root,text='Search',font=("times new roman",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2").place(x=500,y=100,width=100,height=35)
        btn_clear=Button(self.root,text='Clear',font=("times new roman",15,"bold"),bg="gray",fg="white",cursor="hand2").place(x=620,y=100,width=100,height=35)
        btn_submit=Button(self.root,text='Submit',font=("times new roman",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2").place(x=1400,y=100,width=100,height=35)

        #===================
        m_Frame = LabelFrame(self.root, text= "SEMESTER", font=("times new roman", 15), bg="white")
        m_Frame.place(x=80, y=150, width=1380, height=80)

        btn_sem1 = Button(m_Frame, text="Sem 1", command=self.set_subject1,cursor="hand2",font=("times new roman",15,"bold"), bg="#0b5377", fg="white").place(x=40, y=5, width=100, height=30)
        btn_sem2 = Button(m_Frame, text="Sem 2", command=self.set_subject2,cursor="hand2",font=("times new roman",15,"bold"), bg="#0b5377", fg="white").place(x=210, y=5, width=100, height=30)
        btn_sem3 = Button(m_Frame, text="Sem 3", command=self.set_subject3,cursor="hand2",font=("times new roman",15,"bold"), bg="#0b5377", fg="white").place(x=380, y=5, width=100, height=30)
        btn_sem4 = Button(m_Frame, text="Sem 4", command=self.set_subject4,cursor="hand2",font=("times new roman",15,"bold"), bg="#0b5377", fg="white").place(x=550, y=5, width=100, height=30)
        btn_sem5 = Button(m_Frame, text="Sem 5", command=self.set_subject5,cursor="hand2",font=("times new roman",15,"bold"), bg="#0b5377", fg="white").place(x=720, y=5, width=100, height=30)
        btn_sem6 = Button(m_Frame, text="Sem 6", command=self.set_subject6,cursor="hand2",font=("times new roman",15,"bold"), bg="#0b5377", fg="white").place(x=890, y=5, width=100, height=30)
        btn_sem7 = Button(m_Frame, text="Sem 7", command=self.set_subject7,cursor="hand2",font=("times new roman",15,"bold"), bg="#0b5377", fg="white").place(x=1060, y=5, width=100, height=30)
        btn_sem8 = Button(m_Frame, text="Sem 8", command=self.set_subject8,cursor="hand2",font=("times new roman",15,"bold"), bg="#0b5377", fg="white").place(x=1230, y=5, width=100, height=30)
        #==========================tt1=============
        m1_Frame = LabelFrame(self.root, text= "TERM TEST 1", font=("times new roman", 15), bg="white")
        m1_Frame.place(x=80, y=230, width=680, height=280)

        self.tt1_lbl_sub1 = Entry(m1_Frame, text="Sub 1", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt1_lbl_sub1.place(x=40, y=30, width=100, height=30)
        self.tt1_mark_sub1 = Entry(m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_mark_sub1.place(x=150, y=30, width=100, height=30)
        self.slash = Label(m1_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=30, width=10, height=30)
        self.tt1_out_sub1 = Entry(m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_out_sub1.place(x=280, y=30, width=100, height=30)

        self.tt1_lbl_sub2 = Entry(m1_Frame, text="Sub 2", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt1_lbl_sub2.place(x=40, y=70, width=100, height=30)
        self.tt1_mark_sub2 = Entry(m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_mark_sub2.place(x=150, y=70, width=100, height=30)
        self.slash = Label(m1_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=70, width=10, height=30)
        self.tt1_out_sub2 = Entry(m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_out_sub2.place(x=280, y=70, width=100, height=30)

        self.tt1_lbl_sub3 = Entry(m1_Frame, text="Sub 3", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt1_lbl_sub3.place(x=40, y=110, width=100, height=30)
        self.tt1_mark_sub3 = Entry(m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_mark_sub3.place(x=150, y=110, width=100, height=30)
        self.slash = Label(m1_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black").place(x=260, y=110, width=10, height=30)
        self.tt1_out_sub3 = Entry(m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_out_sub3.place(x=280, y=110, width=100, height=30)
       
        self.tt1_lbl_sub4 = Entry(m1_Frame, text="Sub 4", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt1_lbl_sub4.place(x=40, y=150, width=100, height=30)
        self.tt1_mark_sub4 = Entry(m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_mark_sub4.place(x=150, y=150, width=100, height=30)
        self.slash = Label(m1_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black").place(x=260, y=150, width=10, height=30)
        self.tt1_out_sub4 = Entry(m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_out_sub4.place(x=280, y=150, width=100, height=30)

        self.tt1_lbl_sub5 = Entry(m1_Frame, text="Sub 5", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt1_lbl_sub5.place(x=40, y=190, width=100, height=30)
        self.tt1_mark_sub5 = Entry(m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_mark_sub5.place(x=150, y=190, width=100, height=30)
        self.slash = Label(m1_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black").place(x=260, y=190, width=10, height=30)
        self.tt1_out_sub5 = Entry(m1_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt1_out_sub5.place(x=280, y=190, width=100, height=30)

       #==============================tt2==========================
        m2_Frame = LabelFrame(self.root, text= "TERM TEST 2", font=("times new roman", 15), bg="white")
        m2_Frame.place(x=770, y=230, width=690, height=280)

        self.tt2_lbl_sub1 = Entry(m2_Frame, text="Sub 1", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt2_lbl_sub1.place(x=40, y=30, width=100, height=30)
        self.tt2_mark_sub1 = Entry(m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_mark_sub1.place(x=150, y=30, width=100, height=30)
        self.slash = Label(m2_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=30, width=10, height=30)
        self.tt2_out_sub1 = Entry(m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_out_sub1.place(x=280, y=30, width=100, height=30)
        
        self.tt2_lbl_sub2 = Entry(m2_Frame, text="Sub 2", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt2_lbl_sub2.place(x=40, y=70, width=100, height=30)
        self.tt2_mark_sub2 = Entry(m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_mark_sub2.place(x=150, y=70, width=100, height=30)
        self.slash = Label(m2_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=70, width=10, height=30)
        self.tt2_out_sub2 = Entry(m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_out_sub2.place(x=280, y=70, width=100, height=30)
        
        
        self.tt2_lbl_sub3  = Entry(m2_Frame, text="Sub 3", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt2_lbl_sub3.place(x=40, y=110, width=100, height=30)
        self.tt2_mark_sub3  = Entry(m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_mark_sub3.place(x=150, y=110, width=100, height=30)
        self.slash  = Label(m2_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=110, width=10, height=30)
        self.tt2_out_sub3  = Entry(m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_out_sub3.place(x=280, y=110, width=100, height=30)
        
        
        self.tt2_lbl_sub4 = Entry(m2_Frame, text="Sub 4", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt2_lbl_sub4.place(x=40, y=150, width=100, height=30)
        self.tt2_mark_sub4 = Entry(m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_mark_sub4 .place(x=150, y=150, width=100, height=30)
        self.slash = Label(m2_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=150, width=10, height=30)
        self.tt2_out_sub4 = Entry(m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_out_sub4.place(x=280, y=150, width=100, height=30)
        
        self.tt2_lbl_sub5= Entry(m2_Frame, text="Sub 5", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.tt2_lbl_sub5.place(x=40, y=190, width=100, height=30)
        self.tt2_mark_sub5 = Entry(m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_mark_sub5.place(x=150, y=190, width=100, height=30)
        self.slash = Label(m2_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=190, width=10, height=30)
        self.tt2_out_sub5 = Entry(m2_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.tt2_out_sub5.place(x=280, y=190, width=100, height=30)
        

       #==================semester===============
        m3_Frame = LabelFrame(self.root, text= "SEMESTER", font=("times new roman", 15), bg="white")
        m3_Frame.place(x=350, y=520, width=680, height=280)

        self.ut_lbl_sub1= Entry(m3_Frame, text="Sub 1", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.ut_lbl_sub1.place(x=40, y=30, width=100, height=30)
        self.ut_mark_sub1 = Entry(m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_mark_sub1.place(x=150, y=30, width=100, height=30)
        self.slash = Label(m3_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=30, width=10, height=30)
        self.ut_out_sub1 = Entry(m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_out_sub1.place(x=280, y=30, width=100, height=30)
        
        self.ut_lbl_sub2 = Entry(m3_Frame, text="Sub 2", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.ut_lbl_sub2.place(x=40, y=70, width=100, height=30)
        self.ut_mark_sub2 = Entry(m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_mark_sub2.place(x=150, y=70, width=100, height=30)
        self.slash = Label(m3_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=70, width=10, height=30)
        self.ut_out_sub2 = Entry(m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_out_sub2.place(x=280, y=70, width=100, height=30)
        
        self.ut_lbl_sub3 = Entry(m3_Frame, text="Sub 3", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.ut_lbl_sub3.place(x=40, y=110, width=100, height=30)
        self.ut_mark_sub3 = Entry(m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_mark_sub3.place(x=150, y=110, width=100, height=30)
        self.slash = Label(m3_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=110, width=10, height=30)
        self.ut_out_sub3 = Entry(m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_out_sub3.place(x=280, y=110, width=100, height=30)
        
        self.ut_lbl_sub4 = Entry(m3_Frame, text="Sub 4", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.ut_lbl_sub4.place(x=40, y=150, width=100, height=30)
        self.ut_mark_sub4 = Entry(m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_mark_sub4.place(x=150, y=150, width=100, height=30)
        self.slash = Label(m3_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=150, width=10, height=30)
        self.ut_out_sub4 = Entry(m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_out_sub4.place(x=280, y=150, width=100, height=30)
        
        self.ut_lbl_sub5 = Entry(m3_Frame, text="Sub 5", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="#0b5377", fg="white")
        self.ut_lbl_sub5.place(x=40, y=190, width=100, height=30)
        self.ut_mark_sub5 = Entry(m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_mark_sub5.place(x=150, y=190, width=100, height=30)
        self.slash = Label(m3_Frame, text=" / ", cursor="hand2",font=("goudy old style",11,"bold"), justify=CENTER,bg="white", fg="black")
        self.slash.place(x=260, y=190, width=10, height=30)
        self.ut_out_sub5 = Entry(m3_Frame,font=("goudy old style",11,"bold"), justify=CENTER,bg="lightgray", fg="black")
        self.ut_out_sub5.place(x=280, y=190, width=100, height=30)

        Button(self.root,text='Upload',font=("times new roman",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2").place(x=1400,y=800,width=100,height=35)

    def set_subject1(self):
        self.count = 0
        self.set()
    def set_subject2(self):
        self.count = 1
        self.set()
    def set_subject3(self):
        self.count = 2
        self.set()
    def set_subject4(self):
        self.count = 3
        self.set()
    def set_subject5(self):
        self.count = 4
        self.set()
    def set_subject6(self):
        self.count = 5
        self.set()
    def set_subject7(self):
        self.count = 6
        self.set()
    def set_subject8(self):
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
        try:
            self.tt1_lbl_sub1.config(state='readonly', fg='')
            self.tt1_lbl_sub2.config(state='readonly', fg='')
            self.tt1_lbl_sub3.config(state='readonly', fg='')
            self.tt1_lbl_sub4.config(state='readonly', fg='')
            self.tt1_lbl_sub5.config(state='readonly', fg='')
        except:
            print("e")
        
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
        try:
            self.tt2_lbl_sub1.config(state='readonly', fg='')
            self.tt2_lbl_sub2.config(state='readonly', fg='')
            self.tt2_lbl_sub3.config(state='readonly', fg='')
            self.tt2_lbl_sub4.config(state='readonly', fg='')
            self.tt2_lbl_sub5.config(state='readonly', fg='')
        except:
            print("e")
        
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
        try:
            self.ut_lbl_sub1.config(state='readonly', fg='')
            self.ut_lbl_sub2.config(state='readonly', fg='')
            self.ut_lbl_sub3.config(state='readonly', fg='')
            self.ut_lbl_sub4.config(state='readonly', fg='')
            self.ut_lbl_sub5.config(state='readonly', fg='')
        except:
            print("e")
        


root=Tk()
bj=enter_marks(root)
# root.filename= filedialog.askopenfilename(initialdir="/gui/images",title="Select A File ",filetypes=(("png files","*.png"),("all files","*.*")))
# my_label = Label(root,text=root.filename).pack()
# my_image = ImageTk.PhotoImage(Image.open(root.filename))
# my_image_label = Label(image=my_image).pack()
# my_btn = Button(root,text="open File")
root.mainloop()