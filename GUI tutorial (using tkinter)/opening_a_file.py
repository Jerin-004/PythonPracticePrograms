## open a file (file dialog)

from tkinter import *
from tkinter import filedialog

def browse_file():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\STALIN\\Desktop",
                                          title="Open file",
                                          filetypes=(("text files","*.txt"),
                                          ("all files","*.*")))
    file = open(filepath,"r")
    print(file.read())
    file.close()

windows = Tk()

button = Button(windows, text="Browse", command=browse_file)
button.pack()

windows.mainloop()