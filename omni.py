from tkinter import filedialog 
from tkinter import *
from shutil import copy2
from shutil import move
import glob
import time
import os
import string
import re
import subprocess


#Select Source file
root = Tk()
root.withdraw()
root.source = filedialog.askopenfilename(initialdir = "/",title = "Select source file",filetypes = (("html files",".html"),("all files",".*"))) 

if root.source == "": 
    os.system('color 4')
    print("No file selected. Aborting...")
else:
    print ("Selected file " + root.source)
    time.sleep(1)

    #Get absolute path to import directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    rel_path = '\import'
    import_path = dir_path + rel_path

    #Copy file to import directory
    copy2(root.source, import_path, follow_symlinks=True)
    print ("Copied file to selected directory.")
    time.sleep(1)

    #Rename file

    os.chdir(import_path)
    os.system('rename * import.html')
    print("Renamed File")
