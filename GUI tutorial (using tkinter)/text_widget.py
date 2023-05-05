## text widget = functions like a text are, you can enter multiple lines of text

from tkinter import *


def submit():
    input_text = text.get(0.0,END)
    print(input_text)

def delete():
    text.delete(0.0,END)


windows = Tk()

text = Text(windows,
            bg="light yellow",
            font=("Ink free",25),
            fg="black",
            height=8,
            width=20,
            padx=20,
            pady=20)

text.pack()


submitButton = Button(windows, text="submit",command=submit)

submitButton.pack()

deleteButton = Button(windows, text="delete",command=delete)

deleteButton.pack()

windows.mainloop()