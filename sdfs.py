
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
        query = "insert into img (i, sr,abc, adc, adcd) values (%s, %s,2 ,3,4 );"
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

# from tkinter import *
# from tkinter.ttk import *
# from tkinter.filedialog import askopenfile 
# import time

# ws = Tk()
# ws.title('PythonGuides')
# ws.geometry('400x200') 


# def open_file():
#     file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpeg')])
#     if file_path is not None:
#         pass


# def uploadFiles():
#     pb1 = Progressbar(
#         ws, 
#         orient=HORIZONTAL, 
#         length=300, 
#         mode='determinate'
#         )
#     pb1.grid(row=4, columnspan=3, pady=20)
#     for i in range(5):
#         ws.update_idletasks()
#         pb1['value'] += 20
#         time.sleep(1)
#     pb1.destroy()
#     Label(ws, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)
        
    
    
# adhar = Label(
#     ws, 
#     text='Upload Government id in jpg format '
#     )
# adhar.grid(row=0, column=0, padx=10)

# adharbtn = Button(
#     ws, 
#     text ='Choose File', 
#     command = lambda:open_file()
#     ) 
# adharbtn.grid(row=0, column=1)

# dl = Label(
#     ws, 
#     text='Upload Driving License in jpg format '
#     )
# dl.grid(row=1, column=0, padx=10)

# dlbtn = Button(
#     ws, 
#     text ='Choose File ', 
#     command = lambda:open_file()
#     ) 
# dlbtn.grid(row=1, column=1)

# ms = Label(
#     ws, 
#     text='Upload Marksheet in jpg format '
#     )
# ms.grid(row=2, column=0, padx=10)

# msbtn = Button(
#     ws, 
#     text ='Choose File', 
#     command = lambda:open_file()
#     ) 
# msbtn.grid(row=2, column=1)

# upld = Button(
#     ws, 
#     text='Upload Files', 
#     command=uploadFiles
#     )
# upld.grid(row=3, columnspan=3, pady=10)



# ws.mainloop()