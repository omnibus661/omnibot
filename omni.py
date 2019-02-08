from tkinter import filedialog
from tkinter import *
from shutil import copy2
from shutil import move
import time
import os
import string
import re
import subprocess
from colorama import init, Fore, Back, Style

init(convert=True)

# Select Source file
root = Tk()
root.withdraw()
print(Fore.GREEN + "Select HTML file to use")
root.source = filedialog.askopenfilename(
    initialdir="/", title="Select source file", filetypes=(("html files", ".html"), ("all files", ".*")))

if root.source == "":

    print(Fore.RED + "No file selected. Aborting...")
else:
    print(Fore.GREEN + "Selected file " + root.source)
    time.sleep(1)

    # Get absolute path to import directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    rel_path = '\import'
    import_path = dir_path + rel_path

    # Copy file to import directory
    copy2(root.source, import_path, follow_symlinks=True)
    print(Fore.GREEN + "Copied file to directory.")

    time.sleep(1)

    with open("typelist.txt") as types:

        # Rename file

        os.chdir(import_path)
        os.system('rename * import.html')
        print(Fore.GREEN + "Renamed File")

        importfile = rel_path + '\import.html'

        # Read import file and copy to export file
        print("Reading...")

        count = 0

        # Write to file
        with open("import.html") as i:
            with open("export.html", "w") as o:
                for x in i:
                    if "<div " in x:
                        #line = x.split()
                        valid = False
                        validid = False
                        validsel = False
                        validconfirm = False
                        selectedType = 0

                        while valid != True:
                            print("\n \n")
                            # Ask if add itemscope
                            confirmadd = input(Fore.WHITE + "Add " + Fore.CYAN + "itemscope " + Fore.WHITE +
                                            "to " + Fore.GREEN + x.replace("\n", "") + Fore.WHITE + " ? (y/n) ")
                            if confirmadd.lower() == "y" or confirmadd.lower() == "n":
                                valid = True

                                if confirmadd.lower() == "y":
                                    print("\n")
                                    # Specify which itemscope
                                    while validid != True:
                                        print("\n")

                                        idselect = input(
                                            Fore.WHITE + "Which " + Fore.CYAN + "itemscope" + Fore.WHITE + "? (n to abort) ")

                                        if idselect.isdigit():

                                            selectedType = idselect

                                            validid = True

                                            # # Ask if add specified itemscope 1
                                            # if selectedType == "1":
                                            #     while validsel != True:
                                            #         print("\n")
                                            #         confirsel = input(
                                            #             Fore.WHITE + "Add " + Fore.CYAN + "CreativeWork" + Fore.WHITE + "? (y/n) ")

                                            #         if confirsel.lower() == "y" or confirsel.lower() == "n":
                                            #             print("\n")
                                            #             if confirsel == "y":

                                            #                 # Add itemscope
                                            #                 x = x.replace(
                                            #                     '<div ', '<div itemscope itemtype="http://schema.org/CreativeWork" ')
                                            #                 print(x)
                                            #                 print(
                                            #                     Fore.WHITE + "Added " + Fore.CYAN + "CreativeWork" + Fore.WHITE + ".")

                                            #             elif confirsel == "n":

                                            #                 validid = False
                                            #                 validsel = False
                                            #                 validconfirm = False

                                            #             validsel = True
                                            #         else:
                                            #             print(
                                            #                 Fore.RED + "Invalid input.")
                                            #             validsel = False

                                            else:
                                                pass

                                            

                                        else:
                                            if idselect.lower() == "n":
                                                valid = False
                                                validid = False
                                                validsel = False
                                                validconfirm = False
                                                break
                                            else:
                                                print(
                                                    Fore.RED + "Invalid input.")
                                                validid = False
                                else:
                                    pass
                            else:
                                print(Fore.RED + "Invalid input.")
                                valid = False

                    count += 1
                    with open("export.html", "a") as export:
                        export.write(x)

        # Export file

        with open("export.html") as e:
            for x in e:
                print(x)

    exportfile = rel_path + '\export.html'
    print(Fore.WHITE + "Copied " + Fore.GREEN + str(count) + Fore.WHITE +
          " lines to" + Fore.GREEN + " export.html" + Fore.WHITE + ".")
