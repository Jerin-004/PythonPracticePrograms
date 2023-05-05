## color chooser

from tkinter import *
from tkinter import colorchooser


def click():
    color = colorchooser.askcolor()
    windows.config(bg=color[1])



windows = Tk()
windows.geometry("420x420")

button = Button(windows, text="CLICK ME!", command=click, )
button.place(x=185,y=185)

windows.mainloop()