## listbox = A listing of selectables text items within it's own container

from tkinter import *

def submit():

    food = []
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    
    print("You have ordered:")

    for index in food:
        print(index)
    

def enter():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())

def delete():

    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())


windows = Tk()


listbox = Listbox(windows,
                  width=9,
                  font=("Constantia", 40),
                  bg="#f7ffde",
                  selectmode=MULTIPLE)

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"salad")
listbox.insert(4,"burger")
listbox.insert(5,"showerma")

listbox.config(height=listbox.size())
listbox.pack()


entrybox = Entry(windows,
                 relief=RAISED,
                 borderwidth=5)

entrybox.pack()

submitButton = Button(windows,
                      text="SUBMIT",
                      relief=RAISED,
                      borderwidth=5,
                      command=submit)

submitButton.pack()

enterButton = Button(windows,
                     text="ENTER",
                     relief=RAISED,
                     borderwidth=5,
                     command=enter)

enterButton.pack()

deleteButton = Button(windows,
                     text="DELETE",
                     relief=RAISED,
                     borderwidth=5,
                     command=delete)

deleteButton.pack()


windows.mainloop()