## ASCII - America standard code for imformation interchange

from os import system

def ASCII():
    value = input("Enter any thing to convert it to an ASCII value:")
    print("The ASCII value of",value,"is:",ord(value))

ASCII()
again= input("Enter 'r' to do it again:").lower()


if again == "r":
    system('cls')
    ASCII()