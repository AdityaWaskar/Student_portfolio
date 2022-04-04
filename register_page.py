from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Regiseration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.root.focus_force()
        #-----bg Image-------
        self.bg=ImageTk.PhotoImage(file="images\wallpaper.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        #-------LEFT Image---------
        self.left=ImageTk.PhotoImage(file="images\img.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        #-------Register Frame--------
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        #---------First ans last name , Row 1-----------------
        #self.var_fname=StringVar()     #fetch data by creating variable
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray") #imultanusly creating object to fetch the data  
        self.txt_lname.place(x=370,y=130,width=250)
        #--------------Contact no. and email, Row 2------------
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)

        #----------Row 3---------------
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.cnb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cnb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cnb_quest.place(x=50,y=270,width=250)
        self.cnb_quest.current(0)

        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)

        #---------------Password , Row 4------------
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)

        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)

        #------------Terms-----------
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)

       # self.btn_img=ImageTk.PhotoImage(file="D:\VS CODE\Miniproject\abc.png")
       # btn=Button(frame1,image=self.btn_img).place(x=50,y=420)

        btn_register=Button(frame1,text="Register Now",font=("times new roman",15,"bold"),bg="green",fg="black",bd=0,cursor="hand2",command=self.register_data).place(x=270,y=420)

        btn_login=Button(self.root,text="Sign In",font=("times new roman",20,"bold"),bg="green",fg="black",bd=0,cursor="hand2").place(x=200,y=460,width=180)

    def register_data(self):
       
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cnb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="" :
            messagebox.showerror("Error","All Field Are Required",parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password Should Be Same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms & Conditions",parent=self.root)
        else:
            messagebox.showinfo("Success","Register Successful",parent=self.root)

        #print(self.txt_fname.get(),self.txt_lname.get())
        #print(self.txt_contact.get(),self.txt_email.get())
        #print(self.cnb_quest.get(),self.txt_answer.get())
        #print(self.txt_password.get(),self.txt_cpassword.get())


root=Tk()
obj=Register(root)
root.mainloop()