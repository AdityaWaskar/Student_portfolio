import os
from turtle import width
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


        # ---------------------------queires
        sql = "select roll_no, name from sem1_students;"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        # ---------------------------getting current date, month and year 
        date = dt.datetime.now()
        self.current_date = int(f"{date:%d}")
        self.current_month = int(f"{date:%m}")
        self.current_year = int(f"{date:%Y}")

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
        self.sem.place(x=300, y=self.y, width=100, height=21)
        self.sem.current(0)

        date = Label(self.root, text="Date", font=("times new roman",self.font), fg="black", bg="#d1e2f4").place(x=400, y=self.y, width=150, height=20)
        self.date = DateEntry(self.root, selectmode="day",date_pattern = 'dd/mm/yyyy',background="blue",Cursor="hand1",year=self.current_year, month=self.current_month, date=self.current_date,foreground='black', font=("Arial", 12))
        self.date.place(x=520, y=self.y, width=150, height=21)

        Button(self.root, text="Submit",cursor="hand2",bg="#1ab402",fg="black" ,bd=0, font=("times new roman",self.font)).place(x=1000, y=self.y)

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
# -----------------------------------------------set the column size
        self.my_table.column("#0", width=0, stretch=NO)
        self.my_table.column("Gr No.", width=80,anchor=CENTER)
        self.my_table.column("Roll No.", width=80,anchor=CENTER)
        self.my_table.column("name", width=180, anchor=CENTER)
        self.my_table.column("attendance", width=80, anchor=CENTER)
        
        button = Button(self.root,text="Present", command=self.put_present).place(x=900, y=self.table_from_y, height=self.table_height, width=100)        
        button = Button(self.root,text="Absent", command=self.put_absent).place(x=1000, y=self.table_from_y, height=self.table_height, width=100)        

#-----------------------------------------------Create Headings 
        self.my_table.heading("Gr No.",text="Gr No.",anchor=CENTER)
        self.my_table.heading("Roll No.",text="Roll No.",anchor=CENTER)
        self.my_table.heading("name",text="Name",anchor=CENTER)
        self.my_table.heading("attendance",text="Attendance",anchor=CENTER)
        a=0

        for i in result:
            query_gr_no = f"select gr_no from students where name = '{i[1]}'"
            mycursor.execute(query_gr_no)
            student_gr_no = mycursor.fetchall() 
            self.my_table.insert(parent='',index='end',iid=a,text='',values=(student_gr_no[0],i[0], i[1], "none"))
            a+=1

        self.my_table.place(x=0, y=0, width=self.table_width, height=self.table_height)

        frame = Frame(root)
        frame.pack(pady=20)
    

    # def update_record(self):
    #     selected=self.my_table.focus()
    #     self.my_table.item(selected,text="",values=(self.values[0],self.values[1],"Present"))
    
    def put_present(self):
        selected=self.my_table.focus()
        values = self.my_table.item(selected,'values')
        self.my_table.item(selected,text="",values=(values[0],values[1],values[2],"Present"))

    def put_absent(self):
        select = self.my_table.focus()
        self.values = self.my_table.item(select,'values')
        self.my_table.item(select,text="",values=(self.values[0],self.values[1],self.values[2],"Absent"))


if __name__ == "__main__":
    root=Tk()
    obj = take_attendance(root)
    root.mainloop()