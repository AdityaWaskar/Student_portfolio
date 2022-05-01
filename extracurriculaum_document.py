from cgitb import text
from cmath import e
from tkinter import *
from tkinter import messagebox
import mysql.connector as sql
from PIL import ImageTk, Image

mydb = sql.connect(host="localhost", user="root", passwd="", database="SP")
mycursor = mydb.cursor()


class extracurriculaum_document:
    def __init__(self, root, gr_no, category):
        self.root = root
        self.gr_no = gr_no
        # self.filepath = filepath
        self.category = category
        self.root.title("Documents")
        self.root.geometry("800x800+0+0")
        self.root.focus_force()
        self.root.configure(bg='#d8dfed')
        
        self.frame = Frame(self.root, width=600, height=400)
        self.frame.place(anchor='center', relx=0.5, rely=0.5)
        try:
            query = f"select {self.category} from students WHERE gr_no = {self.gr_no};"
            print(query)
            mycursor.execute(query)
            result = mycursor.fetchone()
            for i in result:
                result = i.replace('\\','/')
            

            img = Image.open(f"student_documents/event/{self.category}/{self.gr_no}.jpg")
            img = img.resize((700, 750))
            img = ImageTk.PhotoImage(img)
            label1 = Label(self.frame, image = img)
            label1.image = img
            label1.pack()

        except Exception as e:
            print(e)
            # messagebox.showerror("error", "Some error to fetch images! Try again later:) ")

# ----------------------Create a Label Widget to display the text or Image

if __name__ == "__main__":
    root=Tk()
    obj = extracurriculaum_document(root, 1004,"non_technical_event")
    root.mainloop()
