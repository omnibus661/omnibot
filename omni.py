import os
import re
import string
import subprocess
import time
from shutil import copy2, move
from time import gmtime, strftime
from tkinter import *
from tkinter import filedialog
import ctypes

from colorama import Back, Fore, Style, init



dir_path = os.path.dirname(os.path.realpath(__file__))
rel_path = '\import'

        
import_path = dir_path + rel_path

rel_error_path = '\error_log'
abs_error_path = dir_path + rel_error_path

selection = ""

#Init

class GUI:
    def __init__(self,master):
        self.master = master
        master.title("Omnibot")
        

        infotext = "Waiting for import..."
        

        #Widgets
        self.label = Label(master, text=infotext)
        self.import_button = Button(master, text = "Import File", command=self.imp)

        self.log = Listbox(master, height = 4, width = 40)

        self.close_button = Button(master, text = "Exit", command=self.quit)
        self.text_import = Listbox(master, height = 30, width = 100)
        self.select_button = Button(master,text = "Select", command = self.select)
        self.text_import_scroll = Scrollbar(master,command = self.text_import.yview)
        self.additemscope_button = Button(master, text = "Add Itemtype", command = self.additemtype)
        self.logscroll = Scrollbar(master,command = self.log.yview)

        self.up_button = Button(master, text = "Identify <div> elements", command = self.ident)
        self.down_button = Button(master, text = "▼", command = self.down)

        # Widget Placement
        self.label.place(x = 10,y = 500)
        self.import_button.place(x = 10, y = 570)
        self.select_button.place(x = 80, y = 570)
        self.close_button.place(x = 960, y = 570)
        self.text_import.place(x = 10, y = 10)
        self.additemscope_button.place(x = 650, y = 10)
        self.log.place(x = 10 , y = 500)

        self.up_button.place(x = 650, y = 40)
        self.down_button.place(x = 650, y = 70)
        self.logscroll.place(in_ = self.log, relx = 1.0, relheight = 1.0, bordermod = "outside")
        
        self.text_import_scroll.place(in_= self.text_import, relx = 1.0, relheight = 1.0, bordermod = "outside")
        #self.text_import.insert(0, "Waiting for import...")


        self.text_import.configure(yscrollcommand= self.text_import_scroll.set)
        self.log.configure(yscrollcommand = self.logscroll.set )

   

    def quit(self):
        sys.exit()

    

    def imp(self):
        os.system('python clean.py')
        root.source = filedialog.askopenfilename(initialdir="/", title="Select source file", filetypes=(("html files", ".html"), ("all files", ".*")))

        if root.source == "":

            self.log.insert(END, "No file selected.") 
            self.log.itemconfig(END, {'fg': '#ff0000'})

        else:
            
            self.log.insert(END, "Selected file " + root.source)
            self.log.itemconfig(END, {'fg': '#17d637'})



            copy2(root.source, import_path, follow_symlinks=True)
            self.log.insert(END, "Please wait")
            self.log.itemconfig(END, {'fg': '#d4ff00'})


    

            # Rename file

            os.chdir(import_path)
            os.system('rename * import.html') 

            importfile = rel_path + '\import.html'


            self.log.insert(END, "Ready")
            self.log.itemconfig(END, {'fg': '#17d637'})

            count = 0
    

            self.text_import.delete(0,END)
            with open("import.html") as i:
                with open("export.html", "w") as o:
                    for x in i:

                        self.text_import.insert(END, x)


    def select(self):
        selection = gui.text_import.get(ACTIVE)
        gui.label['text'] = selection

    def up(self):
       a

    def down(self): 
        selection = gui.text_import.get(ACTIVE)
        index = gui.text_import.get(0, "end").index(selection)
        gui.text_import.itemconfig(index, {'bg': 'white'})

        while not "<div " in selection:
            index +=1
            selection = gui.text_import.get(index)
            gui.text_import.yview(index)
            gui.text_import.activate(index)
            gui.text_import.see(index)
        gui.text_import.itemconfig(index, {'bg': '#5b5bff'})

        if "<div" in selection:
            a



        gui.label['text'] = selection
        
        #root.after(1, down(self))

    def ident(self):
        x = 0
        
        selection = gui.text_import.get(x)
        index = gui.text_import.get(0, "end").index(selection)
        while x <= gui.text_import.size():
            if "<div " in selection:
                gui.text_import.itemconfig(index - 1, {'bg': '#eaab70'}) 
            selection = gui.text_import.get(x) 
            index += 1    
            x+= 1
        gui.log.insert(END, "Highlighted all <div> elements")
        gui.log.itemconfig(END, {'fg': '#d4ff00'})

    def additemtype(self):
            
        a
    

root = Tk()
gui = GUI(root)
root.geometry("1000x600")




root.mainloop() 


init(convert=True)

abort = 0

count = 0


#     with open("import.html") as i:
#         with open("export.html", "w") as o:
#             for x in i:
#                 if "<div " in x:
#                     #line = x.split()
#                     valid = False
#                     validid = False
#                     validsel = False
#                     validconfirm = False
#                     selectedTypeID = 0

#                     while valid != True:
#                         print("\n \n")
#                         # Ask if add itemscope
#                         confirmadd = input(Fore.WHITE + "Add " + Fore.CYAN + "itemtype " + Fore.WHITE +
#                                         "to " + Fore.GREEN + x.replace("\n", "") + Fore.WHITE + " ? (y/n) ")
#                         if confirmadd.lower() == "y" or confirmadd.lower() == "n":
#                             valid = True

#                             if confirmadd.lower() == "y":
#                                 print("\n")
#                                 # Specify which itemscope
#                                 while validid != True:
#                                     print("\n")

#                                     idselect = input(
#                                         Fore.WHITE + "Which " + Fore.CYAN + "itemtype" + Fore.WHITE + "? (n to abort) ")

#                                     if idselect.isdigit():

#                                         selectedTypeID = idselect

                                        

#                                         os.chdir(dir_path)
                                            
#                                         try:
#                                             with open("typelist.txt") as types:
#                                                 for i in types:
#                                                     rln = types.readlines()

#                                                     amt_lines = (len(rln)) + 1
                 
#                                                     try:
                                                        
#                                                         ln = rln[int(selectedTypeID) + 2]
#                                                         selectedTypeSplit = ln.split('#')
#                                                         selectedType = selectedTypeSplit[1]
#                                                         selectedType = selectedType.strip()
#                                                         ID = int(selectedTypeID)

                                                        
#                                                         if ID < 108:
#                                                             print (Fore.CYAN + selectedType + Fore.LIGHTYELLOW_EX + " is JSON-LD only and cannot be applied as itemtype.")
#                                                             time.sleep(1)
#                                                             validid = False
                                                        
#                                                         else:
#                                                               validid = True
#                                                               while validsel != True:
#                                                                 print("\n")
#                                                                 confirsel = input(Fore.WHITE + "Add " + Fore.CYAN + selectedType + Fore.WHITE + "? (y/n) ")

#                                                                 if confirsel.lower() == "y" or confirsel.lower() == "n":
#                                                                     print("\n")
                                                                    
#                                                                     if confirsel == "y":
#                                                                         validsel = True
#                                                                         # Add itemscope
#                                                                         x = x.replace('<div ', '<div itemscope itemtype="http://schema.org/' + selectedType.replace("\n" ,"")  + '" ')
#                                                                         #print(x)
#                                                                         print(Fore.WHITE + "Added " + Fore.CYAN + selectedType + Fore.WHITE + ".")
                                                                        


#                                                                         # Add more specific itemprops
#                                                                         if ID == 109:       #Article
                                                                           
#                                                                             validconfirm_itemprop = False 

#                                                                             while validconfirm_itemprop != True:
#                                                                                 confirmadd_itemprop = input(Fore.WHITE + "Add "+ Fore.CYAN + "itemprop(s) "+ Fore.WHITE + "to " + Fore.GREEN + selectedType + Fore.WHITE + " ? (y/n) ")
#                                                                         elif ID == 110:
#                                                                             pass
#                                                                         else:
#                                                                             pass

                                                                            

#                                                                     elif confirsel == "n":

#                                                                         validid = False
#                                                                         validsel = False
#                                                                         validconfirm = False
#                                                                         validsel = False
#                                                                         break
#                                                                 else:
#                                                                     print(Fore.RED + "Invalid input.")
#                                                                     validsel = False
                                        
#                                                     except IndexError:
#                                                         print(Fore.LIGHTRED_EX + "itemscope out of range")             
#                                                         validid = False





#                                         except FileNotFoundError:
#                                             os.chdir(abs_error_path)
#                                             errorfilename = str(strftime("%d_%m-%H_%M_%S",gmtime())) + ".txt"
#                                             error = open(errorfilename,"w+")
#                                             error.write("File typelist.txt deleted / not found in directory.")
#                                             error.close()

#                                             sys.exit(Fore.RED + "An error occurred. View " + Fore.LIGHTMAGENTA_EX + errorfilename + Fore.RED +" for further information.")                                  
                                                                                              
#                                         #Ask if add specified itemscope 1
                                            
#                                     else:
#                                         if idselect.lower() == "n":
#                                             valid = False
#                                             validid = False
#                                             validsel = False
#                                             validconfirm = False
#                                             break
#                                         else:
#                                             print(
#                                                 Fore.RED + "Invalid input.")
#                                             validid = False
#                             else:
#                                 pass
#                         else:
#                             print(Fore.RED + "Invalid input.")
#                             valid = False

#                 count += 1
#                 with open("export.html", "a") as export:
#                     export.write(x)

#     # Export file

# os.system('cls')
# print(Fore.GREEN + 'Writing File. . .')
# time.sleep(3)

# os.system('python clean.py')
# exportfile = rel_path + '\export.html'
# print(Fore.WHITE + "Copied " + Fore.GREEN + str(count) + Fore.WHITE +
#       " lines to" + Fore.GREEN + " export.html" + Fore.WHITE + ".")
# print("\n")

