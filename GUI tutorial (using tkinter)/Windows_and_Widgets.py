## Widgets = GUI elements: buttons, textboxes, labels, images
## Windows = servers as a container to hold or contain these widgets

from tkinter import *

windows = Tk()     ## instantiate an instance of a window 
windows.geometry("500x500")
windows.title("Chijith Jerin")
icon = PhotoImage(file="D:\\【JERIN】\\Python\\Python_basics\\J.png")
windows.iconphoto(True,icon)
windows.config(background="#5cfcff")


windows.mainloop()     ### place window on computer screen, listens for events
