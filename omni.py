from tkinter import filedialog 
from tkinter import *
from shutil import copy2
import time
import os

 
root = Tk()
root.withdraw()
root.source = filedialog.askopenfilename(initialdir = "/",title = "Select source file",filetypes = (("html files",".html"),("all files",".*"))) 
print ("Selected file " + root.source)
time.sleep(1)
root.target = filedialog.askdirectory(initialdir = "/",title = "Select target directory")
print ("Selected directory " + root.target)
copy2(root.source, root.target, follow_symlinks=True)
print ("Copied file to selected directory.")
time.sleep(1)

#os.rename(root.)