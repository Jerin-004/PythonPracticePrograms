## sliding scale

from tkinter import * 

def submit():
    print("Your experience level is: ",scale.get(),"XP")


windows = Tk()


pro_image = PhotoImage(file="professionals.png")


pro_label = Label(windows,
                  image=pro_image,)
pro_label.pack()


scale = Scale(windows,
              from_=100,
              to=0,
              length=600,
              tickinterval=10,      ## adds numeric indicators for value
              orient=VERTICAL,      ## orientation of scale
              font=("Consolas",20),
              #showvalue= 0,     ## hide current value
              #resolution=5,       ## increment of the slider
              troughcolor="#69eaff",     ## sets color of the scrool bar
              fg="gold",        
              background="black")

scale.set(0)
scale.pack()


noob_image = PhotoImage(file="noob.png")


noob_label = Label(windows,
                  image=noob_image,)
noob_label.pack()



submit_button = Button(windows,
                       text="SUBMIT",
                       font=("Impact",10),
                       relief=RAISED,
                       borderwidth=5,
                       command=submit)

submit_button.pack()

windows.mainloop()