from cProfile import label
from logging import root
from tkinter import *

from PIL import Image, ImageTk
root = Tk()
root.geometry("1600x800")
root.title("Student Portfolio")

#photo = PhotoImage(file="himanshu123.png")
# for jpg images

image = Image.open("D:\\VS CODE\\Python\\Lovepik_com-501679643-millennium-university-of-hunan-university.jpg")
image=image.resize((1600,800))
photo = ImageTk.PhotoImage(image)
label1 = Label(root,image=photo) 
label1.pack()

#root.config(bg='red')
'''
bg = PhotoImage(file = "D:\\VS CODE\\Python\\univ.png")
label1 = Label(root, image = bg)
label1.place(x=0,y=0)
bg.pack()
'''
def myfunc():
    print("Himanshu Upadhyay")



filemenu = Menu(root)  #mainmenu

m1 = Menu(filemenu,tearoff=0)
m1.add_command(label="ADD TEACHER",command=myfunc)
m1.add_command(label="ADD STUDENT",command=myfunc)
root.config(menu=filemenu)
filemenu.add_cascade(label="ADD",menu=m1)

m2 = Menu(filemenu,tearoff=0)
m2.add_command(label="TEACHER",command=myfunc)
m2.add_command(label="STUDENT",command=myfunc)
root.config(menu=filemenu)
filemenu.add_cascade(label="DETAILS",menu=m2)

m3 = Menu(filemenu,tearoff=0)
m3.add_command(label="ATTENDENCE",command=myfunc)
root.config(menu=filemenu)
filemenu.add_cascade(label="ATTENDENCE",menu=m3)

m4 = Menu(filemenu,tearoff=0)
m4.add_command(label="PERFORMANCE",command=myfunc)
m4.add_command(label="DEFAULTER LIST",command=myfunc)
root.config(menu=filemenu)
filemenu.add_cascade(label="REPORT",menu=m4)

m5 = Menu(filemenu,tearoff=0)
m5.add_command(label="ADD MARKS",command=myfunc)
m5.add_command(label="SHOW MARKS",command=myfunc)
root.config(menu=filemenu)
filemenu.add_cascade(label="MARKS",menu=m5)

m6 = Menu(filemenu,tearoff=0)
m6.add_command(label="EXIT",command=exit,accelerator="ctrl+Q")
root.config(menu=filemenu)
filemenu.add_cascade(label="LOGOUT",menu=m6)




root.mainloop()