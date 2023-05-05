## checkbox

from tkinter import *


def display():
    if (x.get()) == 1:
        print("You agreed to our terms")

    else:
        print("You don't agree our terms :(")


windows = Tk()

x = IntVar()

photo = PhotoImage(file="J.png")

check_button = Checkbutton(windows,
                           text="I agree this terms and condition",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=("Arial", 20),
                           fg="red",
                           bg="black",
                           activeforeground="red",
                           activebackground="black",
                           padx=25,
                           pady=25,
                           image=photo,
                           compound=LEFT)

check_button.pack()

windows.mainloop()
