from cgitb import text
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox

class reportClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result ")
        self.root.geometry("1600x800")
        self.root.config(bg="white")
        self.root.focus_force()
        #================title===================
        title=Label(self.root,text="View Student Results",font=("times new roman",20,"bold"),bg="orange",fg="white").place(x=10,y=15,width=1600,height=50)
        #==============search=============
        self.var_search=StringVar()
        lbl_search=Label(self.root,text="Search by GR no.",font=("goudy old style",15,"bold"),bg="white").place(x=150,y=100)
        txt_search=Entry(self.root,textvariable=self.var_search,font=("goudy old style",20),bg="lightyellow").place(x=300,y=100,width=150)
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2").place(x=480,y=100,width=100,height=35)
        btn_clear=Button(self.root,text='Clear',font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2").place(x=600,y=100,width=100,height=35)

        

        m_Frame = LabelFrame(self.root, text= "Semester", font=("times new roman", 15), bg="white")
        m_Frame.place(x=80, y=150, width=1380, height=80)

        btn_sem1 = Button(m_Frame, text="Sem 1", cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white").place(x=40, y=5, width=100, height=30)
        btn_sem2 = Button(m_Frame, text="Sem 2", cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white").place(x=210, y=5, width=100, height=30)
        btn_sem3 = Button(m_Frame, text="Sem 3", cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white").place(x=380, y=5, width=100, height=30)
        btn_sem4 = Button(m_Frame, text="Sem 4", cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white").place(x=550, y=5, width=100, height=30)
        btn_sem5 = Button(m_Frame, text="Sem 5", cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white").place(x=720, y=5, width=100, height=30)
        btn_sem6 = Button(m_Frame, text="Sem 6", cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white").place(x=890, y=5, width=100, height=30)
        btn_sem7 = Button(m_Frame, text="Sem 7", cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white").place(x=1060, y=5, width=100, height=30)
        btn_sem8 = Button(m_Frame, text="Sem 8", cursor="hand2",font=("goudy lod style",15,"bold"), bg="#0b5377", fg="white").place(x=1230, y=5, width=100, height=30)
        #================= tt1===============
        lbl_tt1=Label(self.root,text="TERM TEST 1",font=("goudy old style",15,"bold"),bg="white").place(x=650,y=250)
        lbl_sub1=Label(self.root,text="SUB 1",font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE).place(x=350,y=280,width=150,height=50)
        lbl_sub2=Label(self.root,text="SUB 2",font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE).place(x=500,y=280,width=150,height=50)
        lbl_sub3=Label(self.root,text="SUB 3",font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE).place(x=650,y=280,width=150,height=50)
        lbl_sub4=Label(self.root,text="SUB 4",font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE).place(x=800,y=280,width=150,height=50)
        lbl_sub5=Label(self.root,text="SUB 5",font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE).place(x=950,y=280,width=150,height=50)

        self.sub1=Label(self.root,font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE)
        self.sub1.place(x=350,y=320,width=150,height=50)
        self.sub2=Label(self.root,font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE)
        self.sub2.place(x=500,y=320,width=150,height=50)
        self.sub3=Label(self.root,font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE)
        self.sub3.place(x=650,y=320,width=150,height=50)
        self.sub4=Label(self.root,font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE)
        self.sub4.place(x=800,y=320,width=150,height=50)
        self.sub5=Label(self.root,font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE)
        self.sub5.place(x=950,y=320,width=150,height=50)

        #======================= tt2=============
        lbl_tt1=Label(self.root,text="TERM TEST 2",font=("goudy old style",15,"bold"),bg="white").place(x=650,y=400)
        lbl_sub1=Label(self.root,text="SUB 1",font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE).place(x=350,y=430,width=150,height=50)
        lbl_sub2=Label(self.root,text="SUB 2",font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE).place(x=500,y=430,width=150,height=50)
        lbl_sub3=Label(self.root,text="SUB 3",font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE).place(x=650,y=430,width=150,height=50)
        lbl_sub4=Label(self.root,text="SUB 4",font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE).place(x=800,y=430,width=150,height=50)
        lbl_sub5=Label(self.root,text="SUB 5",font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE).place(x=950,y=430,width=150,height=50)
        self.sub1=Label(self.root,font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE)
        self.sub1.place(x=350,y=470,width=150,height=50)
        self.sub2=Label(self.root,font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE)
        self.sub2.place(x=500,y=470,width=150,height=50)
        self.sub3=Label(self.root,font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE)
        self.sub3.place(x=650,y=470,width=150,height=50)
        self.sub4=Label(self.root,font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE)
        self.sub4.place(x=800,y=470,width=150,height=50)
        self.sub5=Label(self.root,font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE)
        self.sub5.place(x=950,y=470,width=150,height=50)
        
        #========================SeMESTER=====================
        lbl_tt1=Label(self.root,text="SEMESTER",font=("goudy old style",15,"bold"),bg="white").place(x=650,y=550)
        lbl_sub1=Label(self.root,text="SUB 1",font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE).place(x=350,y=580,width=150,height=50)
        lbl_sub2=Label(self.root,text="SUB 2",font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE).place(x=500,y=580,width=150,height=50)
        lbl_sub3=Label(self.root,text="SUB 3",font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE).place(x=650,y=580,width=150,height=50)
        lbl_sub4=Label(self.root,text="SUB 4",font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE).place(x=800,y=580,width=150,height=50)
        lbl_sub5=Label(self.root,text="SUB 5",font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE).place(x=950,y=580,width=150,height=50)
        self.sub1=Label(self.root,font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE)
        self.sub1.place(x=350,y=620,width=150,height=50)
        self.sub2=Label(self.root,font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE)
        self.sub2.place(x=500,y=620,width=150,height=50)
        self.sub3=Label(self.root,font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE)
        self.sub3.place(x=650,y=620,width=150,height=50)
        self.sub4=Label(self.root,font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE)
        self.sub4.place(x=800,y=620,width=150,height=50)
        self.sub5=Label(self.root,font=("goudy old style",12,"bold"),bg="white",bd=2,relief=GROOVE)
        self.sub5.place(x=950,y=620,width=150,height=50)



        btn_search=Button(self.root,text='Delete',font=("goudy old style",15,"bold"),bg="red",fg="white",cursor="hand2").place(x=650,y=700,width=150,height=35)









#if __name__=="__main__":
root=Tk()
bj=reportClass(root)
root.mainloop()
