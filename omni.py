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
from tkinter import messagebox
import ctypes
from colorama import Back, Fore, Style, init


#Global Definitions
dir_path = os.path.dirname(os.path.realpath(__file__))
rel_path = '\import'      
import_path = dir_path + rel_path
rel_error_path = '\error_log'
abs_error_path = dir_path + rel_error_path
selection = ""
tmpvr = ""
newstr = ""
index = ""  
value1 = ""
value = ""
counter = 0
imported = False
searchterm = ""
props = []
infotext = ""



#Init
class GUI:
    def __init__(self,master):
        self.master = master
        master.title("Omnibot")
        
        #Widgets
        self.search_var = StringVar()
        self.search_var.trace("w", self.update_list)


        self.label = Label(master, text=infotext)
        self.import_button = Button(master, text = "Import File", command=self.imp, state = NORMAL)
        self.log = Listbox(master, height = 4, width = 43)
        #self.close_button = Button(master, text = "Exit", command=self.quit)
        self.text_import = Listbox(master, selectmode = SINGLE, height = 30, width = 100, exportselection = 0)
        #self.select_button = Button(master,text = "Select", command = self.select, state = DISABLED)
        self.text_import_scroll = Scrollbar(master,command = self.text_import.yview)
        self.additemscope_button = Button(master, text = "Add Itemtype", command = self.additemtype, state = DISABLED)
        self.logscroll = Scrollbar(master,command = self.log.yview)
        self.itemprops = Listbox(master, selectmode = SINGLE, height = 10, width = 50, exportselection = 0)
        self.itemscroll = Scrollbar(master,command = self.itemprops.yview)
        #self.ident_button = Button(master, text = "Identify <div> elements", command = self.ident, state = DISABLED)
        self.searchbar = Entry(master,textvariable = self.search_var, width = 50)
        self.searchresults = Listbox(master, selectmode = SINGLE, height = 5, width = 50)
        self.searchresults_scroll = Scrollbar(master, command = self.searchresults.yview) 
        self.remove_button = Button(master, text = "Remove markup", command = self.removemarkup, state = DISABLED)

        # Widget Placement
        self.itemprops.place(x = 650, y = 155)
        self.label.place(x = 10,y = 500)
        self.import_button.place(x = 10, y = 570)
        #self.select_button.place(x = 85, y = 570)
        #self.close_button.place(x = 960, y = 570)
        self.text_import.place(x = 10, y = 10)
        self.additemscope_button.place(x = 650, y = 10)
        self.log.place(x = 10 , y = 500)
        #self.ident_button.place(x = 85, y = 570)
        self.logscroll.place(in_ = self.log, relx = 1.0, relheight = 1.0, bordermod = "outside")
        self.itemscroll.place(in_ = self.itemprops, relx = 1.0, relheight = 1.0, bordermod = "outside")
        self.text_import_scroll.place(in_= self.text_import, relx = 1.0, relheight = 1.0, bordermod = "outside")
        self.searchbar.place(x = 650, y = 45)
        self.text_import.configure(yscrollcommand= self.text_import_scroll.set)
        self.log.configure(yscrollcommand = self.logscroll.set )
        self.itemprops.configure(yscrollcommand = self.itemscroll.set)
        self.searchresults.place(x = 650, y = 70)
        self.remove_button.place(x = 740, y = 10)

        self.searchresults_scroll.place(in_ = self.searchresults, relx = 1.0, relheight = 1.0, bordermod = "outside")
        self.searchresults.configure(yscrollcommand = self.searchresults_scroll.set)

        #Bindings
        self.text_import.bind("<<ListboxSelect>>", self.selectLine)
        self.itemprops.bind("<<ListboxSelect>>", self.selectProp)
        self.searchresults.bind("<<ListboxSelect>>", self.selectPropSearch)
        self.searchbar.bind("<Double-Button-1>", self.clearSearch)

        #Init

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
        self.searchresults.search_clear(0, END)
    
    def selectPropSearch(self, event):
        widget = event.widget
        selection=widget.curselection()
        global value
        value = widget.get(selection[0])
        return value
        print ("selection: " + value.replace("\n", "") + " at index " + str(selection[0]))
        self.log.insert(END, "selection: " + value.replace("\n", "") + " at index " + str(selection[0]))
        self.log.itemconfig(END, {'fg': '#17d637'})
        self.itemprops.search_clear(0, END)

    def removemarkup(self):                                                                                                
        #beep boop this does not work yet
        
        if value1 != "":
        
            if "itemscope itemtype=" in value1:
                #what the actual fuck is wrong here
                counter = 0
                delindex = 0
                string = value1
                stringparts = string.split()

                filtered_string =""
                for part in stringparts:
                    if part.startswith("itemtype=\"") or part == "itemscope":
                        pass
                    else:
                        filtered_string = filtered_string +" "+part

                index = gui.text_import.get(0,"end").index(value1)

                for each in value1:
                    if each == " ":
                        counter +=1
                    elif each == "<":
                        break
                    
                filtered_string = " "*counter + filtered_string

                gui.text_import.delete(index, index)
                gui.text_import.insert(index, filtered_string)

                #highlight div elements
                x = 0
                
                selection = gui.text_import.get(x)
                index = gui.text_import.get(0, "end").index(selection)
                while x <= gui.text_import.size():
                    if "<div " in selection:
                        gui.text_import.itemconfig(index - 1, {'bg': '#eaab70'}) 
                    selection = gui.text_import.get(x) 
                    index += 1    
                    x+= 1

        else:
            self.log.insert(END, "No selection.")
            self.log.itemconfig(END, {'fg': '#ff0000'})      

        
        
    def additemtype(self): 
        counter = 0
        if value1 != "":
            if value != "":
                if not "itemscope itemtype=" in value1:
                    #print("stuff goes here")
                    if "<div " not in value1:
                        self.log.insert(END, "<div> element not recognized.") 
                        self.log.itemconfig(END, {'fg': '#ff0000'})
                        
                    else:
                        tmpvr = value1
                        #print(tmpvr)
                        tmpvr, newstr = tmpvr.split('<div ')
                        #print(newstr)
                        index = gui.text_import.get(0,"end").index(value1)
                        #print(index)
                        tmpvar = value
                        
                        for each in value1:
                            if each == " ":
                                counter +=1
                            elif each == "<":
                                break

                        newstr = " "*counter + '<div itemscope itemtype="https://schema.org/' + tmpvar + '" ' + newstr
 
                        #print(counter)
                        #newstr = newstr.replace("\n", "")
                        #print(newstr)
                        #print(index)
                        gui.text_import.delete(index, index)
                        gui.text_import.insert(index, newstr)
                    
                else:
                    self.log.insert(END, "Already added itemtype to selection.") 
                    self.log.itemconfig(END, {'fg': '#ff0000'})
                    
        else:
            self.log.insert(END, "Nothing to insert.") 
            self.log.itemconfig(END, {'fg': '#ff0000'})

        #highlight div elements
        x = 0
        
        selection = gui.text_import.get(x)
        index = gui.text_import.get(0, "end").index(selection)
        while x <= gui.text_import.size():
            if "<div " in selection:
                gui.text_import.itemconfig(index - 1, {'bg': '#eaab70'}) 
            selection = gui.text_import.get(x) 
            index += 1    
            x+= 1
        # gui.log.insert(END, "Highlighted all <div> elements")
        # gui.log.itemconfig(END, {'fg': '#d4ff00'})

    def quit(self):
        sys.exit()

    def clearSearch(event):
        gui.searchbar.delete(0,END)
        return None

    
    def update_list(self, *args):
        search_term = self.search_var.get()

        self.searchresults.delete(0, END)

        i = 0
        temp = ""
        if search_term != "":
            while i < gui.itemprops.size():
                i+=1
                temp = gui.itemprops.get(i)
                temp2 = temp.lower()
                #print(temp)
                if search_term.lower() in temp2:
                    gui.searchresults.insert(END, temp)
            
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
                for x in i:
                    self.text_import.insert(END, x)

            #self.select_button['state'] = 'normal'
            #self.ident_button['state'] = 'normal'
            self.import_button['state'] = 'disabled'
            self.additemscope_button['state'] = 'normal'
            self.remove_button['state'] = 'normal'

        # import itemtypes from list                
        os.chdir(dir_path)
        with open("typelist.txt", "r") as typelist:
            rln = typelist.readlines()

            for x in rln:
                ln = x
                tmp, lnsplit = ln.split('#')
                lnsplit = lnsplit.replace("\n", "")

                self.itemprops.insert(END, lnsplit)
        
        props = self.itemprops.get(0, END)
        #print(props)

        self.searchbar.insert(0, "Search. . .")
        #highlight div elements
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

    def close(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

root = Tk()
gui = GUI(root)
root.geometry("1000x600")
root.resizable(False, False)
#root.withdraw()
root.protocol('WM_DELETE_WINDOW', gui.close)
#root.configure(background = 'white')

root.mainloop() 

init(convert=True)

abort = 0

count = 0

#     # Export file

# os.system('cls')
# print(Fore.GREEN + 'Writing File. . .')
# time.sleep(3)

# os.system('python clean.py')
# exportfile = rel_path + '\export.html'
# print(Fore.WHITE + "Copied " + Fore.GREEN + str(count) + Fore.WHITE +
#       " lines to" + Fore.GREEN + " export.html" + Fore.WHITE + ".")
# print("\n")

