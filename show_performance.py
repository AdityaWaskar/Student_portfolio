import os
import string
from tkinter import messagebox
import mysql.connector as sql
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import datetime as dt


# ----------------------Connection with database
mydb = sql.connect(host="localhost", user="root", passwd="", database="SP")
mycursor = mydb.cursor()

class show_performance:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1150x600+180+120")
        self.root.resizable(False, False)
        self.root.config(bg="#d1e2f4")
        title = Label(self.root, text="Performance", font=("goudy old style",20,"bold"), fg="white", bg="#033054").place(x=30, y=10,width= 1090, height=50)
        self.root.focus_force()

        # ---------------------------getting current date, month and year 
        date = dt.datetime.now()
        self.current_year = int(f"{date:%Y}")

        # ---------------------------batchs
        date = dt.datetime.now()
        self.current_year = int(f"{date:%Y}")
        a = {'Select',2016,2017,2018,2019,2020,2021}
        a.add(self.current_year)
        self.batch_years = list(a)

        # ---------------------------defining variables
        self.table_width = 1000  
        self.table_height = 350
        self.table_from_y = 180
        self.y= 100
        self.font = 13

        # ---------------------------combobox
        self.branch = ttk.Combobox(self.root, text="Branch", font=("times new roman",self.font), state="readonly", justify=CENTER)
        self.branch['values'] = ("Select","Information Technology")
        self.branch.place(x=50, y=self.y, width=200, height=21)
        self.branch.current(0)
        
        self.sem = ttk.Combobox(self.root, text="semester", font=("times new roman",self.font), state="readonly", justify=CENTER)
        self.sem['values'] = ("Select","sem 1", "sem 2", "sem 3", "sem 4", "sem 5", "sem 6", "sem 7", "sem 8")
        self.sem.place(x=300, y=self.y, width=100, height=21)
        self.sem.current(0)
        
        self.subject = ttk.Combobox(self.root, text="Subject", font=("times new roman",self.font), state="readonly", justify=CENTER)
        self.subject['values'] = ("Select","-------", "EM_1", "EC_1", "EP_1", "BEE", "Mechanics_1", "------", "EM_2", "EC_2", "EP_2", "C_Programming", "ED", "-----", "EM_1", "Java", "DSA", "DBMS", "PCE_1", "-----", "EM_4", "Python", "CNND", "OS", "COA","-----","Internet_Programming","-----","Data_Mining","-----","Enterprise_Network_Design","-----", "Big_data_analytics")
        self.subject.place(x=450, y=self.y, width=100, height=21)
        self.subject.current(0)

        self.batch = ttk.Combobox(self.root, text="Batch", font=("times new roman",self.font), state="readonly", justify=CENTER)
        self.batch['values'] = list(self.batch_years)
        self.batch.place(x=580, y=self.y, width=100, height=21)
        index1 = self.batch_years.index('Select')
        self.batch.current(index1)

# --------------buttons
        Button(self.root, text="Search",command=self.get_sorting_data,cursor="hand2",bg="#1ab402",fg="black" ,bd=0, font=("times new roman",self.font)).place(x=1000, y=self.y)
        Button(self.root, text="Back",command=self.back,cursor="hand2",bg="#1ab402",fg="black" ,bd=0, font=("times new roman",self.font)).place(x=1080, y=550)

# ---------------------------creating table frame
        self.table_frame = Frame(root)
        self.table_frame.place(x=75, y=self.table_from_y, width=self.table_width, height=self.table_height)

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
        self.my_table['columns'] = ('Gr No.','Roll No.', 'name', 'Email','Performance')
# ------------------------------set the column size
        self.my_table.column("#0", width=0, stretch=NO)
        self.my_table.column("Gr No.", width=80,anchor=CENTER)
        self.my_table.column("Roll No.", width=80,anchor=CENTER)
        self.my_table.column("name", width=180, anchor=CENTER)
        self.my_table.column("Email", width=180, anchor=CENTER)
        self.my_table.column("Performance", width=80, anchor=CENTER)

#-----------------------------------------------Create Headings 
        self.my_table.heading("Gr No.",text="Gr No.",anchor=CENTER)
        self.my_table.heading("Roll No.",text="Roll No.",anchor=CENTER)
        self.my_table.heading("name",text="Name",anchor=CENTER)
        self.my_table.heading("Email",text="Email",anchor=CENTER)
        self.my_table.heading("Performance",text="Performance",anchor=CENTER)
        self.my_table.place(x=0, y=0, width=self.table_width, height=self.table_height)

        frame = Frame(root)
        frame.pack(pady=20)
# ----------------empty list
        self.table_values1 = []

# ------------methods
    def get_sorting_data(self):
        self.get_branch = self.branch.get()
        self.get_sem = self.sem.get()
        self.get_subject = self.subject.get()
        self.get_batch = self.batch.get()
        
# -------------------if-else ladder for selecting right option
        try:
            if(self.get_branch =="Select"):
                messagebox.showerror('error', 'Select branch!')
            else:
                if(self.get_sem == "Select" and self.get_subject == "Select"):
                    messagebox.showerror('error', 'Select Semester and subject!')
                elif(self.get_sem=='sem 1'):
                    if(self.get_subject !='EM_1' and self.get_subject !='EC_1' and self.get_subject !='EP_1' and self.get_subject !='BEE' and self.get_subject !='Mechanics'):
                        messagebox.showerror('error', 'Select either EM_1 or EC_1 or EP_1 or BEE or Mechanics')
                elif(self.get_sem == 'sem 2'):
                    if(self.get_subject !='EM_2' and self.get_subject !='EC_2' and self.get_subject !='EP_2' and self.get_subject !='C_Programming' and self.get_subject !='ED'):
                        messagebox.showerror('error', 'Select either EM_2 or EC_2 or EP_2 or C_Programming or ED')
                elif(self.get_sem == 'sem 3'):
                    if(self.get_subject !='EM_3' and self.get_subject !='Java' and self.get_subject !='DSA' and self.get_subject !='DBMS' and self.get_subject !='PCE_1'):
                        messagebox.showerror('error', 'Select either EM_3 or Java or DSA or DBMS or PCE_1')
                elif(self.get_sem == 'sem 4'):
                    if(self.get_subject !='EM_4' and self.get_subject !='Pyhton' and self.get_subject !='CNND' and self.get_subject !='OS' and self.get_subject !='COA'):
                        messagebox.showerror('error', 'Select either EM_4 or Pyhton or CNND or OS or COA')
                elif(self.get_sem == 'sem 5' ):
                    if(self.get_subject !='Internet_Programming'):
                        messagebox.showerror('error', 'Select Internet_Programming ')
                elif(self.get_sem == 'sem 6' ):
                    if(self.get_subject !='Data_Mining' ):
                        messagebox.showerror('error', 'Select Data_Mining')
                elif(self.get_sem == 'sem 7' ):
                    if(self.get_subject !='Enterprise_Network'):
                        messagebox.showerror('error', 'Select Enterprise_Network')
                elif(self.get_sem == 'sem 8' ):
                    if(self.get_subject !='Big_data_analytics'):
                        messagebox.showerror('error', 'Select Big_data_analytics')
                else:
                    print("main else")
        except Exception as e:
            messagebox.showerror('error', e)
            

# --------------getting the student data
        # try:
        if(True):   
                query1 = f"select gr_no, name, email from students where sem = '{self.get_sem}' and branch='{self.get_branch}' and batch = {self.get_batch} ;"
                mycursor.execute(query1)
                result1 = mycursor.fetchall()

# ---------------display the data to the table
                a=0
                self.my_table.delete(*self.my_table.get_children())
                for i in result1:
                    query = f"select (count(a{i[0]})*100/(select count(*) from sem{self.get_sem[-1]}_{self.get_subject}_attendance)) as score from sem{self.get_sem[-1]}_{self.get_subject}_attendance where a{i[0]} = 'Present' ;"
                    mycursor.execute(query)
                    result = mycursor.fetchall()
                    
                    query_a = f"UPDATE sem{self.get_sem[-1]}_{self.get_subject}_performance set avg_attendacne = {result[0][0]} where gr_no = '{i[0]}'"
                    mycursor.execute(query_a)

                    query_b = f"Select * from sem{self.get_sem[-1]}_{self.get_subject}_performance where gr_no = {i[0]}"
                    mycursor.execute(query_b)
                    result_b = mycursor.fetchone()
                    print(query_b,result_b)
                    query2 = f"select roll_no from sem{self.get_sem[-1]}_students where gr_no = {i[0]};"
                    mycursor.execute(query2)
                    result2 = mycursor.fetchone()
                    
                    mydb.commit() 
                    
                    self.my_table.insert(parent='',index='end',iid=a,text='',values=(i[0],result2[0], i[1], i[2], f"{result_b[1]}%"))
                    a+=1
        # except Exception as e:
        #     messagebox.showerror("error", e)       

    def back(self):
        self.root.destroy()

if __name__ == "__main__":
    root=Tk()
    obj = show_performance(root)
    root.mainloop()