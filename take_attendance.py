import os
from tkinter import messagebox
import mysql.connector as sql
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import datetime as dt

# ----------------------Connection with database
mydb = sql.connect(host="localhost", user="root", passwd="", database="SP")
mycursor = mydb.cursor()


class take_attendance:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1150x600+180+120")
        self.root.resizable(False, False)
        self.root.config(bg="#d1e2f4")
        title = Label(self.root, text="Attendance", font=("goudy old style",20,"bold"), fg="white", bg="#033054").place(x=30, y=10,width= 1090, height=50)
        self.root.focus_force()

# ---------------------------getting current date, month and year 
        date = dt.datetime.now()
        self.current_date = int(f"{date:%d}")
        self.current_month = int(f"{date:%m}")
        self.current_year = int(f"{date:%Y}")

# ---------------------------batchs
        date = dt.datetime.now()
        self.current_year = int(f"{date:%Y}")
        a = {'Select',2016,2017,2018,2019,2020,2021}
        a.add(self.current_year)
        self.batch_years = list(a)
# ---------------------------defining variables
        self.table_width = 800
        self.table_height = 350
        self.table_from_y = 200
        self.y= 100
        self.font = 13

# ---------------------------combobox
        self.branch = ttk.Combobox(self.root, text="Branch", font=("times new roman",self.font), state="readonly", justify=CENTER)
        self.branch['values'] = ("Select","Information Technology")
        self.branch.place(x=50, y=self.y, width=200, height=21)
        self.branch.current(0)
        
        self.sem = ttk.Combobox(self.root, text="semester", font=("times new roman",self.font), state="readonly", justify=CENTER)
        self.sem['values'] = ("Select","sem 1", "sem 2", "sem 3", "sem 4", "sem 5", "sem 6", "sem 7", "sem 8")
        self.sem.place(x=270, y=self.y, width=100, height=21)
        self.sem.current(0)
        
        self.subject = ttk.Combobox(self.root, text="Subject", font=("times new roman",self.font), state="readonly", justify=CENTER)
        self.subject['values'] = ("Select","---sem1----", "EM_1", "EC_1", "EP_1", "BEE", "Mechanics_1",
                                  "---sem2---", "EM_2", "EC_2", "EP_2", "C_Programming", "ED", 
                                  "---sem3--", "EM_1", "Java", "DSA", "DBMS", "PCE_1",
                                  "---sem4--", "EM_4", "Python", "CNND", "OS", "COA",
                                  "---sem5--","Internet_Programming","CNS", "EEB", "Software_Engineering", "PCE_2", 
                                  "---sem6--","Data_Mining", "Web_X", "Wireless_Technology", "AI_and_DS", "Ethical_Hacking",
                                  "---sem7--","Enterprise_Network_Design","Infrastruction_Security","Soft_computing", "Cyber_security_and_Law", "AI",
                                  "---sem8--", "Big_data_analytics", "Internet_of_Everything", "R_Programming", "Robotics" , "Project_management")
        self.subject.place(x=390, y=self.y, width=150, height=21)
        self.subject.current(0)
        
        self.batch = ttk.Combobox(self.root, text="Batch", font=("times new roman",self.font), state="readonly", justify=CENTER)
        self.batch['values'] = list(self.batch_years)
        self.batch.place(x=560, y=self.y, width=100, height=21)
        index1 = self.batch_years.index('Select')
        self.batch.current(index1)

        date = Label(self.root, text="Date", font=("times new roman",self.font), fg="black", bg="#d1e2f4").place(x=660, y=self.y, width=100, height=20)
        self.date = DateEntry(self.root, selectmode="day",date_pattern = 'dd/mm/yyyy',background="blue",Cursor="hand1",year=self.current_year, month=self.current_month, date=self.current_date,foreground='black', font=("Arial", 12))
        self.date.place(x=740, y=self.y, width=150, height=21)

        Button(self.root, text="Search",command=self.get_sorting_data,cursor="hand2",bg="#1ab402",fg="black" ,bd=0, font=("times new roman",self.font)).place(x=1000, y=self.y)
        Button(self.root, text="Submit",command=self.submit,cursor="hand2",bg="#1ab402",fg="black" ,bd=0, font=("times new roman",self.font)).place(x=1050, y=550)

# ---------------------------creating table frame
        self.table_frame = Frame(root)
        self.table_frame.place(x=50, y=self.table_from_y, width=self.table_width, height=self.table_height)

#-----------------------------scrollbar
        table_scrolly = Scrollbar(self.table_frame, orient=VERTICAL)
        table_scrolly.pack(side=RIGHT, fill=Y)

        table_scrollx = Scrollbar(self.table_frame,orient=HORIZONTAL)
        table_scrollx.pack(side= BOTTOM,fill=X)

        self.my_table = ttk.Treeview(self.table_frame,yscrollcommand=table_scrolly.set, xscrollcommand =table_scrollx.set)
        self.my_table.pack()

        table_scrolly.config(command=self.my_table.yview)
        table_scrollx.config(command=self.my_table.xview)

#-------------------------------define our column
        self.my_table['columns'] = ('Gr No.','Roll No.', 'name', 'attendance')
# -------------------------------set the column size
        self.my_table.column("#0", width=0, stretch=NO)
        self.my_table.column("Gr No.", width=80,anchor=CENTER)
        self.my_table.column("Roll No.", width=80,anchor=CENTER)
        self.my_table.column("name", width=180, anchor=CENTER)
        self.my_table.column("attendance", width=80, anchor=CENTER)
        
        button = Button(self.root,text="Present", command=self.put_present).place(x=900, y=self.table_from_y+50, height=100, width=100)        
        button = Button(self.root,text="Absent", command=self.put_absent).place(x=900, y=self.table_from_y+200, height=100, width=100)        
        button = Button(self.root,text="Present ALL", command=self.put_present_all).place(x=1020, y=self.table_from_y+50, height=100, width=100)        
        button = Button(self.root,text="Absent ALL", command=self.put_absent_all).place(x=1020, y=self.table_from_y+200, height=100, width=100)        

#-----------------------------------------------Create Headings 
        self.my_table.heading("Gr No.",text="Gr No.",anchor=CENTER)
        self.my_table.heading("Roll No.",text="Roll No.",anchor=CENTER)
        self.my_table.heading("name",text="Name",anchor=CENTER)
        self.my_table.heading("attendance",text="Attendance",anchor=CENTER)
        self.my_table.place(x=0, y=0, width=self.table_width, height=self.table_height)

        frame = Frame(root)
        frame.pack(pady=20)
# ----------------empty list
        self.table_values1 = []

# ----------------methods
    def get_sorting_data(self):
        self.get_branch = self.branch.get()
        self.get_sem = self.sem.get()
        self.get_subject = self.subject.get()
        self.get_date = self.date.get()
        self.get_batch = self.batch.get()
        flag = False
# -------------------if-else ladder for selecting right option
        if(self.get_sem=='sem 1'):
            print(self.get_sem, self.get_subject)
            if(self.get_subject !='EM_1' and self.get_subject !='EC_1' and self.get_subject !='EP_1' and self.get_subject !='BEE' and self.get_subject !='Mechanics'):
                messagebox.showerror('error', 'Select either EM_1 or EC_1 or EP_1 or BEE or Mechanics')
            else:
                flag=True
        elif(self.get_sem == 'sem 2'):
            if(self.get_subject !='EM_2' and self.get_subject !='EC_2' and self.get_subject !='EP_2' and self.get_subject !='C_Programming' and self.get_subject !='ED'):
                messagebox.showerror('error', 'Select either EM_2 or EC_2 or EP_2 or C_Programming or ED')
            else:
                flag=True
        elif(self.get_sem == 'sem 3'):
            if(self.get_subject !='EM_3' and self.get_subject !='Java' and self.get_subject !='DSA' and self.get_subject !='DBMS' and self.get_subject !='PCE_1'):
                messagebox.showerror('error', 'Select either EM_3 or Java or DSA or DBMS or PCE_1')
            else:
                flag=True
        elif(self.get_sem == 'sem 4'):
            if(self.get_subject !='EM_4' and self.get_subject !='Pyhton' and self.get_subject !='CNND' and self.get_subject !='OS' and self.get_subject !='COA'):
                messagebox.showerror('error', 'Select either EM_4 or Pyhton or CNND or OS or COA')
            else:
                flag=True
        elif(self.get_sem == 'sem 5' ):
            if(self.get_subject !='Internet_Programming' and self.get_subject !='CNS' and self.get_subject !='EEB' and self.get_subject !='Software_Engineering' and self.get_subject !='PCE_2'):
                messagebox.showerror('error', 'Select Internet_Programming or CNS or EEB or Software_Engineering or PCE_2')
            else:
                flag=True
        elif(self.get_sem == 'sem 6' ):
            if(self.get_subject !='Data_Mining' and self.get_subject !='Web_X' and self.get_subject !='Wireless_Technology' and self.get_subject !='AI_and_DS' and self.get_subject !='Ethical_Hacking' ):
                messagebox.showerror('error', 'Select Data_Mining or Web_X or Wireless_Technology or AI_and_DS or Ethical_Hacking ')
            else:
                flag=True
        elif(self.get_sem == 'sem 7' ):
            if(self.get_subject !='Enterprise_Network' and self.get_subject !='Infrastruction_Security' and self.get_subject !='Soft_computing' and self.get_subject !='Cyber_security_and_Law' and self.get_subject !='AI'):
                messagebox.showerror('error', 'Select Enterprise_Network or Infrastruction_Security or Soft_computing or Cyber_security_and_Law or AI ')
            else:
                flag=True
        elif(self.get_sem == 'sem 8' ):
            if(self.get_subject != 'Big_data_analytics' and self.get_subject !='Project_management' and self.get_subject !='Internet_of_Everything' and self.get_subject !='R_Programming' and self.get_subject !='Robotics'):
                messagebox.showerror('error', 'Select Big_data_analytics or Project_management or Insternet_of_Everything or R_Programming or Robotics ')
            else:
                flag=True
        else:
            print("main else")

        if(True):
            self.my_table.delete(*self.my_table.get_children())
            if(flag):
                print("adflk")

# ----------------getting the student data into the database
                try:
                    query1 = f"select gr_no, name, email from students where sem = '{self.get_sem}' and branch='{self.get_branch}' and batch = '{self.get_batch}' ;"
                    print(query1)
                    mycursor.execute(query1)
                    result1 = mycursor.fetchall()
                except Exception as e:
                    print(e)

# ----------------inserting the date into the database
                try:
                    abc1 = f"select count(*) from sem{self.get_sem[-1]}_{self.get_subject}_attendance;"
                    mycursor.execute(abc1)
                    result_abc1 = mycursor.fetchall()
                    mydb.commit()
                    abc = f"insert into sem{self.get_sem[-1]}_{self.get_subject}_attendance (sr_no, date) values ({int(result_abc1[0][0]+1)},'{self.date.get()}');"
                    mycursor.execute(abc)
                    mydb.commit()     
                    print("inserint ")

# ---------------display the data to the table
                    a=0
                    for i in result1:
                        print(i)
                        query2 = f"select roll_no from sem{self.get_sem[-1]}_students where gr_no = {i[0]};"
                        mycursor.execute(query2)
                        result2 = mycursor.fetchone() 
                        self.my_table.insert(parent='',index='end',iid=a,text='',values=(i[0],result2[0], i[1], "none"))
                        a+=1
                except:

                    a=0
                    for i in result1:
                        abc1 = f"select a{i[0]} from sem{self.get_sem[-1]}_{self.get_subject}_attendance where  date = '{self.get_date}';"
                        print(abc1)
                        mycursor.execute(abc1)
                        abc = mycursor.fetchall()
                        print(i)
                        query2 = f"select roll_no from sem{self.get_sem[-1]}_students where gr_no = {i[0]};"
                        print(query2)
                        print(abc1)
                        mycursor.execute(query2)
                        result2 = mycursor.fetchone() 
                        self.my_table.insert(parent='',index='end',iid=a,text='',values=(i[0],result2[0], i[1], abc[0][0]))
                        a+=1
                        mydb.commit()     
        # except Exception as e:
        #     messagebox.showerror("error", e)       

    def put_present(self):
        selected=self.my_table.focus()
        values = self.my_table.item(selected,'values')
        self.my_table.item(selected,text="",values=(values[0],values[1],values[2],"Present"))
        values = self.my_table.item(selected,'values')
        self.table_values1.append((values[0], values[3]))
        

    def put_absent(self):
        select = self.my_table.focus()
        self.values = self.my_table.item(select,'values')
        self.my_table.item(select,text="",values=(self.values[0],self.values[1],self.values[2],"Absent"))
        values = self.my_table.item(select,'values')
        self.table_values1.append([values[0], values[3]])

    def submit(self):
# -------------inserting the attendance to the database
        try:
            for i in self.table_values1:
                query1 = f"UPDATE sem{self.get_sem[-1]}_{self.get_subject}_attendance SET a{i[0]} = '{i[1]}' where date = '{self.get_date}';"
                mycursor.execute(query1)
                mydb.commit()

        except Exception as e:
            print(e)
# -----------destroying the current frame
        messagebox.showinfo('info', f"{self.get_date} attendance is inserted sucessfully.")
        self.root.destroy()
        

    def put_present_all(self):
        print("present all")
        query1 = f"select gr_no, name, email from students where sem = '{self.get_sem}' and branch='{self.get_branch}' ;"
        mycursor.execute(query1)
        result1 = mycursor.fetchall()

        a=0
        self.my_table.delete(*self.my_table.get_children())        
        for i in result1:
            query2 = f"select roll_no from sem{self.get_sem[-1]}_students where name = '{i[1]}' and email = '{i[2]}' ;"
            mycursor.execute(query2)
            result2 = mycursor.fetchone() 
            self.my_table.insert(parent='',index='end',iid=a,text='',values=(i[0],result2[0], i[1], "Present"))
            self.table_values1.append([i[0], 'Present'])
            a+=1

    def put_absent_all(self):
        print("present all")
        query1 = f"select gr_no, name, email from students where sem = '{self.get_sem}' and branch='{self.get_branch}' and batch ='{self.get_batch}' ;"
        mycursor.execute(query1)
        result1 = mycursor.fetchall()

        a=0
        self.my_table.delete(*self.my_table.get_children())        
        for i in result1:
            query2 = f"select roll_no from sem{self.get_sem[-1]}_students where gr_no = {i[0]}; ;"
            mycursor.execute(query2)
            result2 = mycursor.fetchone() 
            self.my_table.insert(parent='',index='end',iid=a,text='',values=(i[0],result2[0], i[1], "Absent"))
            self.table_values1.append([i[0], 'Absent'])
            a+=1

if __name__ == "__main__":
    root=Tk()
    obj = take_attendance(root)
    root.mainloop()