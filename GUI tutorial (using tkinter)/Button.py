## button = you click it, then it does stuff

from tkinter import *

count = 0
def click():
    global count
    count += 1
    print(count)

windows = Tk()


photo = PhotoImage(file="J.png")

button = Button(windows,
                text="Click Me!",
                font=("Comic sans",20),
                foreground="red",
                bg="black",
                command=click,
                activeforeground="red",
                activebackground="red",
                relief=RAISED,
                bd=15,
                image=photo,
                compound="bottom",
                state=ACTIVE,
                )

button.pack()


windows.mainloop()