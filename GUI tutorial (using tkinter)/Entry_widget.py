## Entry widget = textbox  that accepts a simple line of user input

from tkinter import *

def submit():
    user_name = entry.get()
    print("Hello",user_name)
    # entry.config(state=DISABLED)


def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

windows = Tk()

entry = Entry(windows,
            # show="*",
            font=("Comic sans",50),
            fg="red",
            bg="black",)

entry.insert(0,"Enter your user name")
entry.pack(side=LEFT)

submit_button = Button(windows,
                       text="submit",
                       fg="red",
                       bg="black",
                       relief=RAISED,
                       bd=5,
                       command=submit)

submit_button.pack(side=RIGHT)

delete_button = Button(windows,
                       text="delete",
                       fg="red",
                       bg="black",
                       relief=RAISED,
                       bd=5,
                       command=delete)

delete_button.pack(side=RIGHT)

backsapce_botton = Button(windows,
                          text="backspace",
                          fg="red",
                          bg="black",
                          relief=RAISED,
                          bd=5,
                          command=backspace)

backsapce_botton.pack(side=RIGHT)


windows.mainloop()