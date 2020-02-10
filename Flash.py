import os
import tkinter
from tkinter import *
from tkinter.ttk import *
root = tkinter.Tk()

with open("Quest.txt") as f0:
    lines0 = f0.readlines()
count0 = len(open("Quest.txt").readlines())

with open(lines0[0]) as f1:
    lines1 = f1.readlines()
count1 = len(open(lines0[0]).readlines())

a = 0
b = 1
c = str(os.path.basename(lines0[0]))


class Main_Frame(tkinter.Frame):
    def __init__(self, parent, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)

        self.Txt = Text(self, width=8, height=1)
        self.Txt.insert('1.0', 'Card:' + str(b))
        self.Txt.grid(row=0, column=0, sticky=NW, pady=0, padx=0)

        self.Txt2 = Text(self, width=44, height=1)
        self.Txt2.insert('1.0', 'Document: ' + str(c))
        self.Txt2.grid(row=0, column=1, sticky=NW, pady=0, padx=0)

        self.ButL = Button(self, text="Back", command=self.Down, width=10)
        self.ButL.grid(row=1, column=0, sticky=NW, pady=0, padx=0, ipady=79)

        self.But1 = Button(self, text=lines1[a], command=self.flip, width=58)
        self.But1.grid(row=1, column=1, sticky=NW, pady=0, padx=0, ipady=72)

        self.ButR = Button(self, text="Next", command=self.Up, width=10)
        self.ButR.grid(row=1, column=2, sticky=NW, pady=0, padx=0, ipady=79)

    def flip(self):
        global a
        if (a % 2) == 0:
            a = a + 1
            self.But1.config(text=str(lines1[a]))
        else:
            a = a - 1
            self.But1.config(text=str(lines1[a]))
        print(a)

    def Up(self):
        global b, a
        b = b + 1
        self.Txt.delete('1.0', END)
        self.Txt.insert('1.0', 'Card:' + str(b))
        if (a % 2) == 0:
            a = a + 2
            self.But1.config(text=str(lines1[a]))
        else:
            a = a + 1
            self.But1.config(text=str(lines1[a]))

    def Down(self):
        global b, a
        if a > 1:
            b = b - 1
            if (a % 2) == 0:
                a = a - 2
                self.But1.config(text=str(lines1[a]))
            else:
                a = a - 1
                self.But1.config(text=str(lines1[a]))
        self.Txt.delete('1.0', END)
        self.Txt.insert('1.0', 'Card:' + str(b))

def Run_Main():
    global Main_Frame
    Main_Frame = Main_Frame(root)
    Main_Frame.pack(expand='true', fill='both')
    Main_Frame.configure(background="#3f49e5")
    root.geometry("498x200")

Run_Main()
root.mainloop()