
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox

subjects =[["EM_1", "EC_1", "EP_1", "BEE", "Mechanics_1"],
            ["EM_2", "EC_2", "EP_2", "C_Programming", "ED"],
            ["EM_3", "Java", "DSA", "DBMS", "PCE_1"],
            ["EM_4", "Python", "CNND", "OS", "COA"],
            ["Internet_Programming"],
            ["Data_Mining"],
            ["Enterprise_Network_Design"],
            ["Big_data_analytics"]]
class reportClass:
    def __init__(self,root):
        self.count = -1
        self.root=root
        self.root.title("Student Result ")
        self.root.geometry("1600x800+0+0")
        self.root.config(bg="white")
        self.root.focus_force()
        #================title===================
        title=Entry(self.root,text="View Student Results",font=("times new roman",20,"bold"),bg="orange",fg="white").place(x=10,y=15,width=1600,height=50)
        #==============search=============
        self.var_search=StringVar()
        lbl_search=Label(self.root,text="Search by GR no.",justify=CENTER,font=("goudy old style",15,"bold"),bg="white").place(x=150,y=100)
        txt_search=Entry(self.root,textvariable=self.var_search,justify=CENTER,font=("goudy old style",20),bg="lightyellow").place(x=300,y=100,width=150)
        btn_search=Button(self.root,text='Search',justify=CENTER,font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2").place(x=480,y=100,width=100,height=35)
        btn_clear=Button(self.root,text='Clear',justify=CENTER,font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2").place(x=600,y=100,width=100,height=35)

        

        m_Frame = LabelFrame(self.root, text= "Semester", font=("times new roman", 15), bg="white")
        m_Frame.place(x=80, y=150, width=1380, height=80)

        Button(m_Frame, text="Sem 1", command=self.set_subject1, cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white").place(x=40, y=5, width=100, height=30)
        Button(m_Frame, text="Sem 2", command=self.set_subject2, cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white").place(x=210, y=5, width=100, height=30)
        Button(m_Frame, text="Sem 3", command=self.set_subject3, cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white").place(x=380, y=5, width=100, height=30)
        Button(m_Frame, text="Sem 4", command=self.set_subject4, cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white").place(x=550, y=5, width=100, height=30)
        Button(m_Frame, text="Sem 5", command=self.set_subject5, cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white").place(x=720, y=5, width=100, height=30)
        Button(m_Frame, text="Sem 6", command=self.set_subject6, cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white").place(x=890, y=5, width=100, height=30)
        Button(m_Frame, text="Sem 7", command=self.set_subject7, cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white").place(x=1060, y=5, width=100, height=30)
        Button(m_Frame, text="Sem 8", command=self.set_subject8, cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white").place(x=1530, y=5, width=100, height=30)
        #================= tt1===============
        self.tt1_lbl=Label(self.root,text="TERM TEST 1",justify=CENTER,font=("goudy old style",15,"bold"),bg="white")
        self.tt1_lbl.place(x=650,y=250)
        self.tt1_lbl_sub1=Entry(self.root, justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt1_lbl_sub1.place(x=350,y=280,width=150,height=50)
        self.tt1_lbl_sub2=Entry(self.root, justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt1_lbl_sub2.place(x=500,y=280,width=150,height=50)
        self.tt1_lbl_sub3=Entry(self.root, justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt1_lbl_sub3.place(x=650,y=280,width=150,height=50)
        self.tt1_lbl_sub4=Entry(self.root, justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt1_lbl_sub4.place(x=800,y=280,width=150,height=50)
        self.tt1_lbl_sub5=Entry(self.root, justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt1_lbl_sub5.place(x=950,y=280,width=150,height=50)

        self.tt1_sub1=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt1_sub1.place(x=350,y=320,width=150,height=50)
        self.tt1_sub2=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt1_sub2.place(x=500,y=320,width=150,height=50)
        self.tt1_sub3=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt1_sub3.place(x=650,y=320,width=150,height=50)
        self.tt1_sub4=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt1_sub4.place(x=800,y=320,width=150,height=50)
        self.tt1_sub5=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt1_sub5.place(x=950,y=320,width=150,height=50)

        #======================= tt2=============
        lbl_tt1=Label(self.root,text="TERM TEST 2",justify=CENTER,font=("goudy old style",15,"bold"),bg="white").place(x=650,y=400)
        self.tt2_lbl_sub1=Entry(self.root,text="SUB 1",justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt2_lbl_sub1.place(x=350,y=430,width=150,height=50)
        self.tt2_lbl_sub2=Entry(self.root,text="SUB 2",justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt2_lbl_sub2.place(x=500,y=430,width=150,height=50)
        self.tt2_lbl_sub3=Entry(self.root,text="SUB 3",justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt2_lbl_sub3.place(x=650,y=430,width=150,height=50)
        self.tt2_lbl_sub4=Entry(self.root,text="SUB 4",justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt2_lbl_sub4.place(x=800,y=430,width=150,height=50)
        self.tt2_lbl_sub5=Entry(self.root,text="SUB 5",justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt2_lbl_sub5.place(x=950,y=430,width=150,height=50)

        self.tt2_sub1=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt2_sub1.place(x=350,y=470,width=150,height=50)
        self.tt2_sub2=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt2_sub2.place(x=500,y=470,width=150,height=50)
        self.tt2_sub3=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt2_sub3.place(x=650,y=470,width=150,height=50)
        self.tt2_sub4=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt2_sub4.place(x=800,y=470,width=150,height=50)
        self.tt2_sub5=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.tt2_sub5.place(x=950,y=470,width=150,height=50)
        
        #========================SeMESTER=====================
        ut_lbl_tt1=Label(self.root,text="SEMESTER",justify=CENTER,font=("goudy old style",15,"bold"),bg="white").place(x=680,y=550)
        self.ut_lbl_sub1=Entry(self.root,text="SUB 1",justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.ut_lbl_sub1.place(x=350,y=580,width=150,height=50)
        self.ut_lbl_sub2=Entry(self.root,text="SUB 2",justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.ut_lbl_sub2.place(x=500,y=580,width=150,height=50)
        self.ut_lbl_sub3=Entry(self.root,text="SUB 3",justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.ut_lbl_sub3.place(x=650,y=580,width=150,height=50)
        self.ut_lbl_sub4=Entry(self.root,text="SUB 4",justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.ut_lbl_sub4.place(x=800,y=580,width=150,height=50)
        self.ut_lbl_sub5=Entry(self.root,text="SUB 5",justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.ut_lbl_sub5.place(x=950,y=580,width=150,height=50)

        self.ut_sub1=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.ut_sub1.place(x=350,y=620,width=150,height=50)
        self.ut_sub2=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.ut_sub2.place(x=500,y=620,width=150,height=50)
        self.ut_sub3=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.ut_sub3.place(x=650,y=620,width=150,height=50)
        self.ut_sub4=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.ut_sub4.place(x=800,y=620,width=150,height=50)
        self.ut_sub5=Entry(self.root,justify=CENTER,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.ut_sub5.place(x=950,y=620,width=150,height=50)



        btn_search=Button(self.root,text='Delete',justify=CENTER,font=("goudy old style",15,"bold"),bg="red",fg="white",cursor="hand2").place(x=650,y=700,width=150,height=35)

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
# -----------setting the subjects to correct position of tt1
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

        self.tt1_lbl_sub1.config(state='readonly')
        self.tt1_lbl_sub2.config(state='readonly')
        self.tt1_lbl_sub3.config(state='readonly')
        self.tt1_lbl_sub4.config(state='readonly')
        self.tt1_lbl_sub5.config(state='readonly')

# -----------setting the subjects to correct position of tt2
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

        self.tt2_lbl_sub1.config(state='readonly')
        self.tt2_lbl_sub2.config(state='readonly')
        self.tt2_lbl_sub3.config(state='readonly')
        self.tt2_lbl_sub4.config(state='readonly')
        self.tt2_lbl_sub5.config(state='readonly')

# -----------setting the subjects to correct position of ut
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

        self.ut_lbl_sub1.config(state='readonly')
        self.ut_lbl_sub2.config(state='readonly')
        self.ut_lbl_sub3.config(state='readonly')
        self.ut_lbl_sub4.config(state='readonly')
        self.ut_lbl_sub5.config(state='readonly')
        





if (__name__=="__main__"):
    root=Tk()
    bj=reportClass(root)
    root.mainloop()
