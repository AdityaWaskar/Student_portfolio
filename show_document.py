from tkinter import *
from tkinter import messagebox
import mysql.connector as sql
from PIL import ImageTk, Image

mydb = sql.connect(host="localhost", user="root", passwd="", database="SP")
mycursor = mydb.cursor()


class document:
    def __init__(self, root, gr_no, sem):
        self.root = root
        self.gr_no = gr_no
        self.sem = sem
        self.root.title("Login Page")
        self.root.geometry("1600x500+0+150")
        self.root.focus_force()
        self.root.configure(bg='#d8dfed')
        
        self.frame = Frame(self.root, width=600, height=400)
        self.frame.pack()
        self.frame.place(anchor='center', relx=0.5, rely=0.5)
        try:
            query = f"SELECT result_path from {self.sem}_students WHERE gr_no = {self.gr_no} "
            mycursor.execute(query)
            result = mycursor.fetchone()
            for i in result:
                result = i.replace('\\','/')
                print(result)
        except:
            messagebox.showerror("error", "Some error to fetch images! Try again later:) ")


        try:
# -----------------------------Create an object of tkinter ImageTk
            img = Image.open(f"student_documents/results/Information Technology/{self.sem}/{self.gr_no}.jpg")
        
# ----------------------img = img.resize((500, 200), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)

        except:
            messagebox.showerror("error", "Some error to fetch images! Try again later:) ")

# ----------------------Create a Label Widget to display the text or Image
        label = Label(self.frame, image = img)
        label.image = img
        label.pack()

if __name__ == "__main__":
    root=Tk()
    obj = document(root, 1000, "sem1")
    root.mainloop()
