## Labels = an area widget that holds text and/or an image within a window

from tkinter import *


windows = Tk()

photo = PhotoImage(file='D:\\【JERIN】\\Python\\Python_basics\\J.png')

label = Label(windows,
              text="Chijith Jerin",
              font=("Arial", 50, "italic"),
              foreground="red",
              bg="black",
              relief=RAISED,
              bd=10,
              padx=30,
              pady=30,
              image=photo,
              compound="bottom")

label.pack()
# label.place(x=100,y=100)

windows.mainloop()
