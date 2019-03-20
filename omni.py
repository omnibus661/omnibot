import os
import re
import string
import subprocess
import time
from shutil import copy2, move
from time import gmtime, strftime
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import ctypes


from colorama import Back, Fore, Style, init



dir_path = os.path.dirname(os.path.realpath(__file__))
rel_path = '\import'

        
import_path = dir_path + rel_path
 
rel_error_path = '\error_log'
abs_error_path = dir_path + rel_error_path

selection = ""

    
value1 = ""
value = ""


imported = False

#Init

class GUI:
    def __init__(self,master):
        self.master = master
        master.title("Omnibot")
        

        infotext = ""
        
        
        #Widgets
        self.searchterm = StringVar()


        self.label = Label(master, text=infotext)
        self.import_button = Button(master, text = "Import File", command=self.imp, state = NORMAL)
        self.log = Listbox(master, height = 4, width = 43)
        #self.close_button = Button(master, text = "Exit", command=self.quit)
        self.text_import = Listbox(master, selectmode = SINGLE, height = 30, width = 100, exportselection = 0)
        self.select_button = Button(master,text = "Select", command = self.select, state = DISABLED)
        self.text_import_scroll = Scrollbar(master,command = self.text_import.yview)
        self.additemscope_button = Button(master, text = "Add Itemtype", command = self.additemtype, state = DISABLED)
        self.logscroll = Scrollbar(master,command = self.log.yview)
        self.itemprops = Listbox(master, selectmode = SINGLE, height = 15, width = 50, exportselection = 0)
        self.itemscroll = Scrollbar(master,command = self.itemprops.yview)
        self.ident_button = Button(master, text = "Identify <div> elements", command = self.ident, state = DISABLED)
        #self.searchbar = Entry(master,textvariable = self.searchterm, width = 35)
        #self.searchresults = Listbox(master, selectmode = SINGLE, height = 3, width = 50, exportselection = 0)
        #self.searchresults_scroll = Scrollbar(master, command = self.searchresults.yview) 

        # Widget Placement
        self.itemprops.place(x = 650, y = 40)
        self.label.place(x = 10,y = 500)
        self.import_button.place(x = 10, y = 570)
        self.select_button.place(x = 85, y = 570)
        #self.close_button.place(x = 960, y = 570)
        self.text_import.place(x = 10, y = 10)
        self.additemscope_button.place(x = 650, y = 10)
        self.log.place(x = 10 , y = 500)
        self.ident_button.place(x = 135, y = 570)
        self.logscroll.place(in_ = self.log, relx = 1.0, relheight = 1.0, bordermod = "outside")
        self.itemscroll.place(in_ = self.itemprops, relx = 1.0, relheight = 1.0, bordermod = "outside")
        self.text_import_scroll.place(in_= self.text_import, relx = 1.0, relheight = 1.0, bordermod = "outside")
        #self.searchbar.place(x = 740, y = 17)
        self.text_import.configure(yscrollcommand= self.text_import_scroll.set)
        self.log.configure(yscrollcommand = self.logscroll.set )
        self.itemprops.configure(yscrollcommand = self.itemscroll.set)
        #self.searchresults.place(x = 650, y = 40)

        #self.searchresults_scroll.place(in_ = self.searchresults, relx = 1.0, relheight = 1.0, bordermod = "outside")
        #self.searchresults.configure(yscrollcommand = self.searchresults_scroll.set)

        #Bindings
        self.text_import.bind("<<ListboxSelect>>", self.selectLine)
        self.itemprops.bind("<<ListboxSelect>>", self.selectProp)


    def selectLine(self, event):
        widget = event.widget
        selection1 = widget.curselection()
        global value1
        value1 = widget.get(selection1[0])
        return value1
        print ("selection: " + value1.replace("\n", "") + " at index " + str(selection1[0]))
        self.log.insert(END, "selection: " + value1.replace("\n", "") + " at index " + str(selection1[0]))
        self.log.itemconfig(END, {'fg': '#17d637'})

        

    def selectProp(self, event):
        widget = event.widget
        selection=widget.curselection()
        global value
        value = widget.get(selection[0])
        return value
        print ("selection: " + value.replace("\n", "") + " at index " + str(selection[0]))
        self.log.insert(END, "selection: " + value.replace("\n", "") + " at index " + str(selection[0]))
        self.log.itemconfig(END, {'fg': '#17d637'})
        

    def additemtype(self):
        if value1 != "":
            if value != "":
                #print("stuff goes here")
                if "<div " not in value1:
                    print("<div> element not recognized")
        else:
            print('Selections cannot be ""')

            
        
        

    def quit(self):
        sys.exit()

    # def search_itemprops(self):
    #     search_term = self.searchterm.get()
    #     print(search_term)
    #     with open("typelist.txt") as typelist:
    #         types = typelist.readlines()

    #         for x in types:
    #             ln = x
    #             ind,tmp  = ln.split('#')


    #     if search_term != "":
    #         try:
    #             index = self.itemprops.get(0,"END").index()
    #         except ValueError:
    #             pass



    #     root.after(10, gui.search_itemprops)


    

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
            
            self.select_button['state'] = 'normal'
            self.ident_button['state'] = 'normal'
            self.import_button['state'] = 'disabled'
            self.additemscope_button['state'] = 'normal'


        # import itemtypes from list                
        os.chdir(dir_path)
        with open("typelist.txt", "r") as typelist:
            rln = typelist.readlines()

            for x in rln:
                ln = x
                tmp, lnsplit = ln.split('#')

                self.itemprops.insert(END, lnsplit)
        
        #root.after(10, gui.search_itemprops)
        
        #mark itemtypes


    def select(self):
        selection = gui.text_import.get(ACTIVE)
        gui.label['text'] = selection


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

    def passfunction(self):
        pass


root = Tk()
gui = GUI(root)
root.geometry("1000x600")
root.resizable(False, False)
root.protocol('WM_DELETE_WINDOW', gui.passfunction)





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

