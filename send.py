# import PyPDF2
# from tkinter import *
# from tkinter import filedialog
# #Create an instance of tkinter frame
# win= Tk()
# #Set the Geometry
# win.geometry("750x450")
# #Create a Text Box
# text= Text(win,width= 80,height=30)
# text.pack(pady=20)
# #Define a function to clear the text
# def clear_text():
#    text.delete(1.0, END)
# #Define a function to open the pdf file
# def open_pdf():
#    file= filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files",".pdf"),("All Files",".*")))
#    if file:
#       #Open the PDF File
#       pdf_file= PyPDF2.PdfFileReader(file)
#       #Select a Page to read
#       page= pdf_file.getPage(0)
#       #Get the content of the Page
#       content=page.extractText()
#       #Add the content to TextBox
#       text.insert(1.0,content)

# #Define function to Quit the window
# def quit_app():
#    win.destroy()
# #Create a Menu
# my_menu= Menu(win)
# win.config(menu=my_menu)
# #Add dropdown to the Menus
# file_menu=Menu(my_menu,tearoff=False)
# my_menu.add_cascade(label="File",menu= file_menu)
# file_menu.add_command(label="Open",command=open_pdf)
# file_menu.add_command(label="Clear",command=clear_text)
# file_menu.add_command(label="Quit",command=quit_app)
# win.mainloop()



# importing tkinter module
from tkinter import * 
from tkinter.ttk import *

# creating tkinter window
root = Tk()

# Progress bar widget
progress = Progressbar(root, orient = HORIZONTAL,
			length = 100, mode = 'determinate')

# Function responsible for the updation
# of the progress bar value
def bar():
	import time
	progress['value'] = 20
	root.update_idletasks()
	time.sleep(1)

	progress['value'] = 40
	root.update_idletasks()
	time.sleep(1)

	progress['value'] = 50
	root.update_idletasks()
	time.sleep(1)

	progress['value'] = 60
	root.update_idletasks()
	time.sleep(1)

	progress['value'] = 80
	root.update_idletasks()
	time.sleep(1)
	progress['value'] = 100

progress.pack(pady = 10)

# This button will initialize
# the progress bar
Button(root, text = 'Start', command = bar).pack(pady = 10)

# infinite loop
mainloop()
