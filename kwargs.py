## **kwargs = parameter that will pick all arguments into a dictionary
##            useful so that a function can accept a varying amount of keyboard arguments

def welcome_screen(**names):  ## ypu can change it to any name from kwargs
    print("Hello",names["first"],names["last"])
    print("Hello", end =" ")
    
    for key,values in names.items():
        print(values, end= " ")


welcome_screen(Title="Mr.",first="Chijith",last="Jerin")