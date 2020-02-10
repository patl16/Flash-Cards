import os
import tkinter
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import *

root = Tk()

class Main_Frame1(tkinter.Frame):
    def __init__(self, parent, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.But1 = Button(self, text="Open File With Questions", command=self.File_Save, width=50)
        self.But1.grid(row=1, column=1, sticky=NW, pady=0, padx=0, ipady=72)

        self.But1 = Button(self, text="Start Flash Cards ", command=self.File_Open, width=20)
        self.But1.grid(row=1, column=2, sticky=NW, pady=0, padx=0, ipady=72)

        self.e1 = Entry(self, width=59)
        self.e1.grid(row=2, column=1, sticky=NW, pady=0, padx=0, ipady=4)

    def File_Save(self):
        file = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        self.e1.insert(10, str(file))
        file1 = open("Quest.txt", "w")  # write mode
        file1.write(file)
        file1.close()

    def File_Open(self):
        root.destroy()
        os.system("Flash.py")


def Run_Main():
    global Main_Frame1
    Main_Frame1 = Main_Frame1(root)
    Main_Frame1.pack(expand='true', fill='both')
    Main_Frame1.configure(background="#3f49e5")
    root.geometry("498x200")
    file1 = open("Quest.txt", "w")  # write mode
    file1.write("")
    file1.close()


Run_Main()
root.mainloop()