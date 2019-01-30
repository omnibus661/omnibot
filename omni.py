from tkinter import filedialog
from tkinter import *
from shutil import copy2
 
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("HTML Files","*.html"),("all files","*.*")))
print ("Selected file " + root.filename)
copy2(root.filename, '/')