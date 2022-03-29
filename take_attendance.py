import os
import mysql.connector as sql
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

# ----------------------Connection with database
mydb = sql.connect(host="localhost", user="root", passwd="", database="SP")
mycursor = mydb.cursor()

class take_attendance:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1200x600+180+120")
        self.root.resizable(False, False)

        # ---------------------------queires
        sql = "select roll_no, name from sem1_students;"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        # ---------------------------defining variables
        self.table_width = 800
        self.table_height = 500
        self.table_from_y = 200

        # ---------------------------creating table frame
        self.table_frame = Frame(root)
        self.table_frame.place(x=50, y=self.table_from_y, width=800, height=500)

        #-----------------------------scrollbar
        table_scrolly = Scrollbar(self.table_frame, orient='vertical')
        table_scrolly.pack(side=RIGHT, fill=Y)

        table_scrollx = Scrollbar(self.table_frame,orient='horizontal')
        table_scrollx.pack(side= BOTTOM,fill=X)

        self.my_table = ttk.Treeview(self.table_frame,yscrollcommand=table_scrolly.set, xscrollcommand =table_scrollx.set)
        self.my_table.pack()

        table_scrolly.config(command=self.my_table.yview)
        table_scrollx.config(command=self.my_table.xview)

        #-------------------------------define our column
        self.my_table['columns'] = ('Gr No.', 'name', 'attendance')
        
        button = Button(self.root,text="Select Record", command=self.put_present).place(x=900, y=self.table_from_y, height=self.table_height, width=100)        
        button = Button(self.root,text="Select Record", command=self.put_absent).place(x=900, y=self.table_from_y, height=self.table_height, width=100)        

#-----------------------------------------------Create Headings 
        self.my_table.heading("#0",text="sdjhsd",anchor=CENTER)
        self.my_table.heading("Gr No.",text="ID",anchor=CENTER)
        self.my_table.heading("name",text="Name",anchor=CENTER)
        self.my_table.heading("attendance",text="Attendance",anchor=CENTER)
        a=0
        for i in result:
            self.my_table.insert(parent='',index='end',iid=a,text='',values=(i[0], i[1], "none"))
            a+=1

        self.my_table.place(x=0, y=0, width=self.table_width, height=self.table_height)

        frame = Frame(root)
        frame.pack(pady=20)
    

    def update_record(self):
        selected=self.my_table.focus()
        self.my_table.item(selected,text="",values=(self.values[0],self.values[1],"Present"))

    def put_present(self):
        #-------------------------------grab the particular row
        selected=self.my_table.focus()
        self.values = self.my_table.item(selected,'values')
        print(self.values)
        self.update_record()

    def put_absent(self):
        pass
       
if __name__ == "__main__":
    root=Tk()
    obj = take_attendance(root)
    root.mainloop()