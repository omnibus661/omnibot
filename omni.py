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
from colorama import init, Fore, Back, Style

init(convert=True)

#Select Source file
root = Tk()
root.withdraw()
root.source = filedialog.askopenfilename(initialdir = "/",title = "Select source file",filetypes = (("html files",".html"),("all files",".*"))) 

if root.source == "": 

    print(Fore.RED + "No file selected. Aborting...")
else:
    print (Fore.GREEN + "Selected file " + root.source)
    time.sleep(1)

    #Get absolute path to import directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    rel_path = '\import'
    import_path = dir_path + rel_path

    #Copy file to import directory
    copy2(root.source, import_path, follow_symlinks=True)
    print (Fore.GREEN + "Copied file to directory.")
    time.sleep(1)

    #Rename file
    os.chdir(import_path)
    os.system('rename * import.html')
    print(Fore.GREEN + "Renamed File")

    importfile = rel_path + '\import.html'

    #Read import file and copy to export file
    print ("Reading...")

    count = 0

    #Write to file
    with open("import.html") as i:
        with open("export.html","w") as o:
            for x in i:
                if "<div " in x:
                    line = x.split()
                    valid = False
                    validid = False
                    
                    while valid != True:
                        print("\n \n")
                        

                        confirmadd = input(Fore.WHITE + "Add " + Fore.CYAN + "itemscope " + Fore.WHITE + "to " + Fore.GREEN + x.replace("\n","") + Fore.WHITE + " ? (y/n)")
                        if confirmadd.lower() == "y" or confirmadd.lower() == "n":
                            valid = True

                            if confirmadd.lower() == "y":
                                print("\n")
                                
                                while validid != True:
                                    print("\n")
                                    idselect = input(Fore.WHITE + "Which " +Fore.CYAN + "itemscope" + Fore.WHITE + "?")

                                    if idselect.isdigit():

                                    #ID Check goes here


                                        pass
                                        validid = True

                                    else:
                                        print(Fore.RED + "Invalid input.")
                                        validid = False
                            
                            else:
                                pass

                        

                        else:
                            print(Fore.RED + "Invalid input.") 
                            valid = False

                                
                        





                    
                count +=1
                o.write(x)

    exportfile = rel_path +  '\export.html'
    print(Fore.WHITE + "Copied " + Fore.GREEN + str(count) + Fore.WHITE + " lines to" + Fore.GREEN + " export.html" + Fore.WHITE + ".")
     


    
        
            

