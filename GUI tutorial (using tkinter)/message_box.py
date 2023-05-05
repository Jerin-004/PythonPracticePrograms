## message box

from tkinter import *
from tkinter import font
from tkinter.font import BOLD
from tkinter import messagebox
import time
import os

def message():
    time.sleep(4)

    messagebox.showinfo(title="System info",message="Installing Malware in 5 sec",icon="warning")

    time.sleep(5)

    messagebox.showwarning(title="K7 Anti-virus",message="Virus detected")

    if messagebox.askyesnocancel(title="K7 Anti-virus",message="Suspecious Malware activity detected. Wanna delete?"):
        time.sleep(3)
        if messagebox.askretrycancel(title="ERROR",message="Failed to delete virus"):

            while messagebox.askretrycancel(title="ERROR",message="Failed to delete virus"):
                messagebox.askretrycancel(title="ERROR",message="Failed to delete virus")

            if not messagebox.askretrycancel(title="ERROR",message="Failed to delete virus"):
                messagebox.showwarning(title="WARNING",message="System breakdown in few sec")
                # os.system("shutdown /s /t 10")
        else:
            messagebox.showwarning(title="WARNING",message="System breakdown in few sec")
            # os.system("shutdown /s /t 10")

    else:
        messagebox.showwarning(title="WARNING",message="System breakdown in few sec")
        # os.system("shutdown /s /t 10")

    # answer = messagebox.askquestion(title="ask question", message="Do you like pie?")

    # if answer == "yes":
    #     print("I like pie too")

    # else:
    #     print("But whyyy")


windows = Tk()

icon = PhotoImage(file="windows.png")
windows.iconphoto(True,icon)

windows.title("Warning")


danger_image = PhotoImage(file="poison.png")

warning_sign = Label(windows,
                    text="WARNING!! DO NOT PRESS THIS BUTTON",
                    font=('Arial',10,BOLD),
                    fg="red")

warning_sign.pack()

button = Button(windows,
                image=danger_image,
                bg="red",
                command=message)

button.pack()


windows.mainloop()