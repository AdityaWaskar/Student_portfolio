from tkinter import messagebox
import mysql.connector as sql
from tkinter import *
from tkinter import ttk
import datetime as dt

# ----------------------Connection with database
mydb = sql.connect(host="localhost", user="root", passwd="", database="SP")
mycursor = mydb.cursor()

class show_defaulter:
    def __init__(self, root):
        self.root = root
        self.root.title("Defaulter Page")
        self.root.geometry("1150x600+180+120")
        self.root.resizable(False, False)
        self.root.config(bg="#d1e2f4")
        self.root.focus_force()
        title = Label(self.root, text="Defaulter", font=("goudy old style",20,"bold"), fg="white", bg="#033054").place(x=30, y=10,width= 1090, height=50)

        # ---------------------------getting current date, month and year 
        date = dt.datetime.now()
        self.current_date = int(f"{date:%d}")
        self.current_month = int(f"{date:%m}")
        self.current_year = int(f"{date:%Y}")
# ------------------------batches
        
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
        self.subject['values'] = ("Select","---sem1----", "EM_1", "EC_1", "EP_1", "BEE", "Mechanics_1",
                                  "---sem2---", "EM_2", "EC_2", "EP_2", "C_Programming", "ED", 
                                  "---sem3--", "EM_1", "Java", "DSA", "DBMS", "PCE_1",
                                  "---sem4--", "EM_4", "Python", "CNND", "OS", "COA",
                                  "---sem5--","Internet_Programming","CNS", "EEB", "Software_Engineering", "PCE_2", 
                                  "---sem6--","Data_Mining", "Web_X", "Wireless_Technology", "AI_and_DS", "Ethical_Hacking",
                                  "---sem7--","Enterprise_Network_Design","Infrastruction_Security","Soft_computing", "Cyber_security_and_Law", "AI",
                                  "---sem8--", "Big_data_analytics", "Internet_of_Everything", "R_Programming", "Robotics" , "Project_management")
        self.subject.place(x=450, y=self.y, width=150, height=21)
        self.subject.current(0)

        self.batch = ttk.Combobox(self.root, text="Batch", font=("times new roman",self.font), state="readonly", justify=CENTER)
        self.batch['values'] = list(self.batch_years)
        self.batch.place(x=650, y=self.y, width=100, height=21)
        index1 = self.batch_years.index('Select')
        self.batch.current(index1)

        # self.sem = ttk.Combobox(self.root, text="days", font=("times new roman",self.font), state="readonly", justify=CENTER)
        # self.sem['values'] = ("Select","last 30 days", "last 60 days","last 6 months" )
        # self.sem.place(x=600, y=self.y, width=10, height=21)
        # self.sem.current(0)

        Button(self.root, text="Search",command=self.get_sorting_data,cursor="hand2",bg="#1ab402",fg="black" ,bd=0, font=("times new roman",self.font)).place(x=1000, y=self.y)
        Button(self.root, text="Back",command=self.submit,cursor="hand2",bg="#1ab402",fg="black" ,bd=0, font=("times new roman",self.font)).place(x=1080, y=550)

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
# -----------------------------------------------set the column size
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

# -----------methods
    def get_sorting_data(self):
        self.get_branch = self.branch.get()
        self.get_sem = self.sem.get()
        self.get_subject = self.subject.get()
        self.get_batch = self.batch.get()
        flag = False

# -------------------if-else ladder for selecting right option
        if(self.get_branch =="Select"):
            messagebox.showerror('error', 'Select branch!',parent=self.root)
        else:
            if(self.get_sem == "Select" and self.get_subject == "Select"):
                messagebox.showerror('error', 'Select Semester and subject!',parent=self.root)
            elif(self.get_sem=='sem 1'):
                if(self.get_subject !='EM_1' and self.get_subject !='EC_1' and self.get_subject !='EP_1' and self.get_subject !='BEE' and self.get_subject !='Mechanics'):
                    messagebox.showerror('error', 'Select either EM_1 or EC_1 or EP_1 or BEE or Mechanics',parent=self.root)
                else:
                    flag=True
            elif(self.get_sem == 'sem 2'):
                if(self.get_subject !='EM_2' and self.get_subject !='EC_2' and self.get_subject !='EP_2' and self.get_subject !='C_Programming' and self.get_subject !='ED'):
                    messagebox.showerror('error', 'Select either EM_2 or EC_2 or EP_2 or C_Programming or ED',parent=self.root)
                else:
                    flag=True
            elif(self.get_sem == 'sem 3'):
                if(self.get_subject !='EM_3' and self.get_subject !='Java' and self.get_subject !='DSA' and self.get_subject !='DBMS' and self.get_subject !='PCE_1'):
                    messagebox.showerror('error', 'Select either EM_3 or Java or DSA or DBMS or PCE_1',parent=self.root)
                else:
                    flag=True
            elif(self.get_sem == 'sem 4'):
                if(self.get_subject !='EM_4' and self.get_subject !='Pyhton' and self.get_subject !='CNND' and self.get_subject !='OS' and self.get_subject !='COA'):
                    messagebox.showerror('error', 'Select either EM_4 or Pyhton or CNND or OS or COA',parent=self.root)
                else:
                    flag=True
            elif(self.get_sem == 'sem 5' ):
                if(self.get_subject !='Internet_Programming'):
                    messagebox.showerror('error', 'Select Internet_Programming ',parent=self.root)
                else:
                    flag=True
            elif(self.get_sem == 'sem 6' ):
                if(self.get_subject !='Data_Mining' ):
                    messagebox.showerror('error', 'Select Data_Mining',parent=self.root)
                else:
                    flag=True
            elif(self.get_sem == 'sem 7' ):
                if(self.get_subject !='Enterprise_Network'):
                    messagebox.showerror('error', 'Select Enterprise_Network',parent=self.root)
                else:
                    flag=True
            elif(self.get_sem == 'sem 8' ):
                if(self.get_subject !='Big_data_analytics'):
                    messagebox.showerror('error', 'Select Big_data_analytics',parent=self.root)
                else:
                    flag=True
            else:
                print("main else")

            try:   
                    query1 = f"select gr_no, avg_attendacne from sem{self.get_sem[-1]}_{self.get_subject}_performance where avg_attendacne < 75.00 and batch = {self.get_batch};"
                    print(query1)
                    mycursor.execute(query1)
                    result1 = mycursor.fetchall()
                    a=0
                    self.my_table.delete(*self.my_table.get_children())

# ---------------display the data to the table
                    if result1:
                        for i in result1:
                            # query = f"select gr_no, avg_attendacne from sem{self.get_sem[-1]}_{self.get_subject}_performance where avg_attendacne < 75.00 ;"
                            # mycursor.execute(query)
                            # result = mycursor.fetchall()

                            query2 = f"select roll_no, name, email from sem{self.get_sem[-1]}_students where gr_no = '{i[0]}';"
                            print(query2)
                            mycursor.execute(query2)
                            result2 = mycursor.fetchone() 
                            self.my_table.insert(parent='',index='end',iid=a,text='',values=(i[0],result2[0], result2[1], result2[2], i[1]))
                            a+=1
                    else:
                        messagebox.showinfo('info',f'There is no student in {self.get_batch}',parent=self.root)
            except Exception as e:
                messagebox.showerror("error", e,parent=self.root)       

    def submit(self):
        self.root.destroy()

if __name__ == "__main__":
    root=Tk()
    obj = show_defaulter(root)
    root.mainloop()