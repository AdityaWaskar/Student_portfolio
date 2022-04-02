
import base64
import io
from tkinter import Tk, filedialog
from tkinter import *
import mysql.connector as sql
from PIL import Image

mydb = sql.connect(host="localhost", user="root", passwd="", database="SP")
mycursor = mydb.cursor()


class teacher_Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1199x600+150+100")
        self.root.resizable(False, False)
        global filename,img
        f_types =[('Png files','*.png'),('Jpg Files', '*.jpg')]
        # filename = filedialog.askopenfilename(filetypes=f_types)
        # print(filename)
        # # img = IMAGETEXT.PhotoImage(file=filename)
        # # picture = self.convertToBinary(filename)
        # query = f"insert into img (sr, i) values (1,load_File('{filename}'));"
        # # mycursor.execute(query, base64.b64encode(picture))
        # mycursor.execute(query)
        # print(query)
        # mydb.commit()


        filename = filedialog.askopenfilename(filetypes=f_types)
        file = open(filename, 'rb').read()
        file = base64.b64encode(file)
        query = "insert into img values (%s, %s)"
        ar = (file, 1)
        mycursor.execute(query, ar)
        mydb.commit()
        query1 = 'select i from img;'
        mycursor.execute(query1)
        result = mycursor.fetchall()
        bim = base64.b64decode(result[0][0])

        img = Image.open(io.BytesIO(bim))
        img.show()




        
         
if __name__ == "__main__":
    root=Tk()
    obj = teacher_Login(root)
    root.mainloop()