import os
from tkinter import messagebox
import mysql.connector as sql
from tkinter import *
from tkinter import ttk
import datetime as dt
from tkcalendar import DateEntry

# ----------------------Connection with database
mydb = sql.connect(host="localhost", user="root", passwd="", database="SP")
mycursor = mydb.cursor()


class add_student:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("900x750+350+50") 
        self.root.resizable(False, False)
        self.root.config(bg="#d1e2f4")
        self.root.focus_force()


#-----------------------getting Current year
        date = dt.datetime.now()
        self.current_year = int(f"{date:%Y}")
        self.batch_years = {"Select",2016,2017,2018,2019,2020,2021}
        self.batch_years.add(self.current_year)

# --------------------queries
        sql = "select count(*) from students"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        form_no = 1000+ result[0][0]  

        print((form_no))
        

# --------------------- title
        title = Label(self.root, text="Add Student", font=("Impact",30,"bold"), fg="#167303", bg="#d1e2f4").place(x=90, y=30)

# --------------------- another Frame
        Frame_student = Frame(self.root, bg="light blue")
        Frame_student.config(bg="#d1e2f4")
        Frame_student.place(x=50, y=80, height=600, width=800)

# --------------------row 1
        stu_gr = Label(Frame_student, text="GR No.", font=("times new roman",15) ,fg="black", bg="#d1e2f4").place(x=30, y=30)
        self.stu_gr = Entry(Frame_student,font=("times new roman", 15),justify=CENTER ,bg="white")
        self.stu_gr.insert(END, form_no)
        self.stu_gr.config(state="readonly")
        self.stu_gr.place(x=30, y=60, width=300, height=30)

        roll_no = Label(Frame_student, text="Roll No.", font=("times new roman",15), fg="black", bg="#d1e2f4").place(x=450, y=30)
        self.roll_no = Entry(Frame_student, font=("times new roman", 15), bg ="white")
        self.roll_no.place(x=450, y=60, width=300, height=30)

# --------------------row 2
        name = Label(Frame_student, text="Name", font=("times new roman",15), fg="black", bg="#d1e2f4").place(x=30, y=120)
        self.name = Entry(Frame_student, font=("times new roman", 15), bg ="white")
        self.name.place(x=30, y=150, width=300, height=30)
        
        DOB = Label(Frame_student, text="DOB", font=("times new roman",15), fg="black", bg="#d1e2f4").place(x=450, y=120)
        # self.DOB = Entry(Frame_student, font=("times new roman", 15), bg="white")
        self.DOB = DateEntry(Frame_student, selectmode="day",date_pattern = 'dd/mm/yyyy',background="blue",Cursor="hand1",year=2003, month=1, foreground='black', font=("Arial", 12))
        self.DOB.place(x=450, y=150, width=300, height=30)


# --------------------row 3
        phone_no = Label(Frame_student, text="Phone No.", font=("times new roman",15), fg="black", bg="#d1e2f4").place(x=30, y=220)
        self.phone_no = Entry(Frame_student, font=("times new roman", 15), bg="white")
        self.phone_no.place(x=30, y=250, width=300, height=30)

        email = Label(Frame_student, text="Email", font=("times new roman",15), fg="black", bg="#d1e2f4").place(x=450, y=220)
        self.email = Entry(Frame_student, font=("times new roman", 15), bg="white")
        self.email.place(x=450, y=250, width=300, height=30)
        
# --------------------row 4
        Xth = Label(Frame_student, text="Xth marks", font=("times new roman",15), fg="black", bg="#d1e2f4").place(x=30, y=320)
        self.Xth = Entry(Frame_student, font=("times new roman", 15), bg="white")
        self.Xth.place(x=30, y=350, width=300, height=30)

        XIIth = Label(Frame_student, text="XIIth marks", font=("times new roman",15), fg="black", bg="#d1e2f4").place(x=450, y=320)
        self.XIIth = Entry(Frame_student, font=("times new roman", 15), bg="white")
        self.XIIth.place(x=450, y=350, width=300, height=30)

# --------------------row 5
        address = Label(Frame_student, text="Address", font=("times new roman",15), fg="black", bg="#d1e2f4").place(x=30, y=420)
        self.address = Entry(Frame_student, font=("times new roman", 15), bg="white")
        self.address.place(x=30, y=450, width=300, height=30)
        
        branch = Label(Frame_student, text="branch", font=("times new roman",15), fg="black", bg="#d1e2f4").place(x=450, y=420)
        self.branch = ttk.Combobox(Frame_student, font=("times new roman", 15),state="readonly", justify=CENTER)
        self.branch['values'] = ("Select","Information Technology")
        self.branch.place(x=450, y=450, width=300, height=30)
        self.branch.current(0)
# --------------------row 6

        sem = Label(Frame_student, text="Semester", font=("times new roman",15), fg="black", bg="#d1e2f4").place(x=30, y=520)
        self.sem = ttk.Combobox(Frame_student, text="semester", font=("times new roman",15), state="readonly", justify=CENTER)
        self.sem['values'] = ("Select","sem 1", "sem 2", "sem 3", "sem 4", "sem 5", "sem 6", "sem 7", "sem 8")
        self.sem.place(x=30, y=550, width=300, height=30)
        self.sem.current(0)
        
        batch = Label(Frame_student, text="Batch", font=("times new roman",15), fg="black", bg="#d1e2f4").place(x=450, y=520)
        self.batch = ttk.Combobox(Frame_student, text="Batch", font=("times new roman",15), state="readonly", justify=CENTER)
        self.batch['values'] = list(self.batch_years)
        self.batch.place(x=450, y=550, width=300, height=30)
        self.batch.current(0)



# --------------------Button
        Button(self.root, text="Submit", command=self.submit,cursor="hand2",bg="#1ab402",fg="black" ,bd=0, font=("times new roman",18)).place(x=750, y=680)

# --------------------submit function
    def submit(self):
        # -----------------Getting all values
        self.get_name = self.name.get()
        self.get_roll_no = self.roll_no.get()
        self.get_DOB = self.DOB.get()
        self.get_email = self.email.get()
        self.get_phone_no = self.phone_no.get()
        self.get_Xth = self.Xth.get()
        self.get_XIIth = self.XIIth.get()
        self.get_address = self.address.get()
        self.get_branch = self.branch.get()
        self.get_sem = self.sem.get()

        if(self.get_name=="" or self.get_roll_no=="" or self.get_DOB=="" or self.email=="" or self.phone_no=="" or self.get_Xth=="" or self.get_XIIth=="" or self.address=="" or self.branch=="Select" or self.get_sem=="Select"):
                messagebox.showerror("showerror", "All field must be required!")
        else:
                sql1 = "INSERT INTO students(gr_no, name, DOB, email, phone_no, Xth, XIIth, address, branch, sem, batch) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                mycursor.execute(sql1, [self.stu_gr.get(),self.get_name, self.get_DOB, self.get_email, self.get_phone_no, self.get_Xth, self.get_XIIth, self.get_address, self.get_branch, self.get_sem, self.batch.get()])

                sql = f"INSERT INTO sem{self.get_sem[-1]}_students(gr_no, roll_no, name, DOB, email, phone_no, Xth, XIIth, address, branch, batch) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                mycursor.execute(sql, [self.stu_gr.get() ,int(self.get_roll_no), self.get_name, self.get_DOB, self.get_email, self.get_phone_no, self.get_Xth, self.get_XIIth, self.get_address, self.get_branch, self.batch.get()])
                messagebox.showinfo("showinfo", "Data Inserted sucessfully.")
                import show_student

# ---------------add new coloumn to attendance table
                if(self.get_sem == "sem 1"):
                        query1 = f"ALTER TABLE sem1_em_1_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"
                        query2 = f"ALTER TABLE sem1_EC_1_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"
                        query3 = f"ALTER TABLE sem1_EP_1_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"
                        query4 = f"ALTER TABLE sem1_BEE_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"
                        query5 = f"ALTER TABLE sem1_Mechanics_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"

                        query6= f"INSERT INTO sem1_em_1_performance(gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query7= f"INSERT INTO sem1_EC_1_performance(gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query8= f"INSERT INTO sem1_EP_1_performance(gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query9= f"INSERT INTO sem1_BEE_performance(gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query10= f"INSERT INTO sem1_Mechanics_performance(gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                     

                if(self.get_sem == "sem 2"):
                        query1 = f"ALTER TABLE sem2_EM_2_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"
                        query2 = f"ALTER TABLE sem2_EC_2_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"
                        query3 = f"ALTER TABLE sem2_EP_2_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"
                        query4 = f"ALTER TABLE sem2_C_Programming_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"
                        query5 = f"ALTER TABLE sem2_ED_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"

                        query6= f"INSERT INTO sem2_EM_2_performance(gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query7= f"INSERT INTO sem2_EC_2_performance(gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query8= f"INSERT INTO sem2_EP_2_performance(gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query9= f"INSERT INTO sem2_C_Programming_performance(gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query10= f"INSERT INTO sem2_ED_performance(gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"

                        
                if(self.get_sem == "sem 3"):
                        query1 = f"ALTER TABLE sem3_EM_3_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"
                        query2 = f"ALTER TABLE sem3_Java_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"
                        query3 = f"ALTER TABLE sem3_DSA_3_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"
                        query4 = f"ALTER TABLE sem3_DBMS_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"
                        query5 = f"ALTER TABLE sem3_PCE_1_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"

                        query6= f"INSERT INTO sem3_EM_3_performance(gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query7= f"INSERT INTO sem3_Java_performance(gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query8= f"INSERT INTO sem3_DSA_3_performance(gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query9= f"INSERT INTO sem3_DBMS_performance(gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query10= f"INSERT INTO sem3_PCE_1_performance(gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"

                if(self.get_sem == "sem 4"):
                        query1 = f"ALTER TABLE sem4_EM_4_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"
                        query2 = f"ALTER TABLE sem4_Python_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"
                        query3 = f"ALTER TABLE sem4_CNND_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"
                        query4 = f"ALTER TABLE sem4_OS_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"                        
                        query5 = f"ALTER TABLE sem4_COA_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"                        

                        query6= f"INSERT INTO sem4_EM_4_performance(gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query7= f"INSERT INTO sem4_Python_performance(gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query8= f"INSERT INTO sem4_CNND_performance(gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query9= f"INSERT INTO sem4_OS_performance(gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query10= f"INSERT INTO sem4_COA_performance(gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"

                if(self.get_sem == "sem 5"):
                        query1 = f"ALTER TABLE sem5_Internet_Programming_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"
                        query2 = f"ALTER TABLE sem5_CNS_attendance ADD {self.stu_gr.get()} varchar(10) default 'Absent';"
                        query3 = f"ALTER TABLE sem5_EEB_attendance ADD {self.stu_gr.get()} varchar(10) default 'Absent';"
                        query4 = f"ALTER TABLE sem5_Software_Engineering_attendance ADD {self.stu_gr.get()} varchar(10) default 'Absent';"
                        query5 = f"ALTER TABLE sem5_PCE_2_attendance ADD {self.stu_gr.get()} varchar(10) default 'Absent';"

                        query6= f"INSERT INTO sem5_Internet_Programming_performance (gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query7= f"INSERT INTO sem5_CNS_performance (gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query8= f"INSERT INTO sem5_EEB_performance (gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query9= f"INSERT INTO sem5_Software_Engineering_5_performance (gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query10= f"INSERT INTO sem5_PCE_2_performance (gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
 
                if(self.get_sem == "sem 6"):
                        query1 = f"ALTER TABLE sem6_Data_Mining_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"
                        query2 = f"ALTER TABLE sem6_Web_X_attendance ADD {self.stu_gr.get()} varchar(10) default 'Absent';"
                        query3 = f"ALTER TABLE sem6_wireless_technology_attendance ADD {self.stu_gr.get()} varchar(10) default 'Absent';"
                        query4 = f"ALTER TABLE sem6_AI_and_DS_attendance ADD {self.stu_gr.get()} varchar(10) default 'Absent';"
                        query5 = f"ALTER TABLE sem6_AI_and_DS_attendance ADD {self.stu_gr.get()} varchar(10) default 'Absent';"

                        query6= f"INSERT INTO sem6_Data_Mining_performance (gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query7= f"INSERT INTO sem6_Web_X_performance (gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query8= f"INSERT INTO sem6_wireless_technology_performance (gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query9= f"INSERT INTO sem6_AI_and_DS_performance (gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query10= f"INSERT INTO sem6_Ethical_Hacking_performance (gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
 
                if(self.get_sem == "sem 7"):
                        query1 = f"ALTER TABLE sem7_Enterprise_Network_Design_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"
                        query2 = f"ALTER TABLE sem7_Infrastruction_Security_attendance ADD {self.stu_gr.get()} varchar(10) default 'Absent';"
                        query3 = f"ALTER TABLE sem7_Soft_computing_attendance ADD {self.stu_gr.get()} varchar(10) default 'Absent';"
                        query4 = f"ALTER TABLE sem7_Cyber_security_and_Law_attendance ADD {self.stu_gr.get()} varchar(10) default 'Absent';"
                        query5 = f"ALTER TABLE sem7_AI_attendance ADD {self.stu_gr.get()} varchar(10) default 'Absent';"

                        query6= f"INSERT INTO sem7_Enterprise_Network_Design_performance (gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query7= f"INSERT INTO sem7_Infrastruction_Security_performance (gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query8= f"INSERT INTO sem7_Soft_computing_performance (gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query9= f"INSERT INTO sem7_Cyber_security_and_Law_performance (gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query10= f"INSERT INTO sem7_AI_performance (gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
 
                if(self.get_sem == "sem 8"):
                        query1 = f"ALTER TABLE sem8_Big_data_analytics_attendance ADD a{self.stu_gr.get()} varchar(10) default 'Absent';"
                        query2 = f"ALTER TABLE sem8_Internet_of_Everything_attendance ADD {self.stu_gr.get()} varchar(10) default 'Absent';"
                        query3 = f"ALTER TABLE sem8_R_Programming_attendance ADD {self.stu_gr.get()} varchar(10) default 'Absent';"
                        query4 = f"ALTER TABLE sem8_Robotics_attendance ADD {self.stu_gr.get()} varchar(10) default 'Absent';"
                        query5 = f"ALTER TABLE sem8_Project_management_attendance ADD {self.stu_gr.get()} varchar(10) default 'Absent';"

                        query6= f"INSERT INTO sem8_Big_data_analytics_performance (gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query7= f"INSERT INTO sem8_Internet_of_Everything_performance (gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query8= f"INSERT INTO sem8_R_Programming_performance (gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query9= f"INSERT INTO sem8_Robotics_performance (gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
                        query10= f"INSERT INTO sem8_Project_management_performance (gr_no, batch) values ({self.stu_gr.get()}, {self.batch.get()})"
 
                mycursor.execute(query1)
                mycursor.execute(query2)
                mycursor.execute(query3)
                mycursor.execute(query4)
                mycursor.execute(query5)
                mycursor.execute(query6)
                mycursor.execute(query7)
                mycursor.execute(query8)
                mycursor.execute(query9)
                mycursor.execute(query10)
                mydb.commit()
# --------------destorying the frame
                self.root.destroy()
    
if __name__ == "__main__":
    root=Tk()
    obj = add_student(root)
    root.mainloop()