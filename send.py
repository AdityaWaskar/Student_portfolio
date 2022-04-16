
from tkinter import *
from tkinter import messagebox
from unittest import result
import mysql.connector as sql
from PIL import ImageTk, Image

mydb = sql.connect(host="localhost", user="root", passwd="", database="SP")
mycursor = mydb.cursor()

class extracurriculaum_document:
    def __init__(self, root):
        self.root = root
        self.root.title("Documents")
        self.root.geometry("800x800+0+0")
        self.root.focus_force()
        self.root.configure(bg='#d8dfed')
        
        query = "select technical_event, non_technical_event from students where gr_no=1001;"
        mycursor.execute(query)
        result= mycursor.fetchone()
        print(f"{result[1]},{result[0]}")
        if(result[0] == None or result[1] == None):
            print("Yes")
        else:
            print("No")
#         self.frame = Frame(self.root, width=600, height=400)
#         # self.frame.pack()
#         self.frame.place(anchor='center', relx=0.5, rely=0.5)
    


#         try:
# # -----------------------------Create an object of tkinter ImageTk
#             img = Image.open(f"student_documents/event/technical_event/1000.jpg")
        
# # ----------------------img = img.resize((500, 200), Image.ANTIALIAS)
#             img = ImageTk.PhotoImage(img)

#         except:
#             messagebox.showerror("error", "Some error to fetch images! Try again later:) ")

# # ----------------------Create a Label Widget to display the text or Image
#         label1 = Label(self.frame, image = img)
#         label1.image = img
#         label1.pack()

if __name__ == "__main__":
    root=Tk()
    obj = extracurriculaum_document(root)
    root.mainloop()
