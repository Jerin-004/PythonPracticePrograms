## Radio button = similar to checkbox, but you can only select one option from a group

from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def display():
    if (x.get() == 0):
        print("You have ordered a pizza!")

    elif (x.get() == 1):
        print("You have ordered a hamburger!")
    
    elif (x.get() == 2):
        print("You have ordered a hotdog!")

    else:
        print("huh?")


windows = Tk()

pizza_image = PhotoImage(file="pizza.png")
burger_image = PhotoImage(file="hamburger.png")
hotdog_image = PhotoImage(file="Hotdog.png")
food_image = [pizza_image,burger_image,hotdog_image]

x = IntVar()

for index in range(len(food)):

    radio_button = Radiobutton(windows,
                               text=food[index],
                               variable=x,  
                               value=index,
                               padx=25,
                               font=("Impact",40),
                               indicatoron=0,  ## elimininates circle indicators
                               width=320,
                               relief=RAISED,
                               bd=5,
                               image=food_image[index],
                               compound=LEFT,
                               command=display)

    radio_button.pack(anchor=W)


windows.mainloop()