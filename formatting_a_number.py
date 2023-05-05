# formatting a number

pi = 3.14159
value = int(input("Enter any decimal value:"))
number = value

print("The value of pi is {:.2f}".format(pi))
print("The number is {:.2f}".format(number))
print("The number is {:,}".format(number))
print("The binary value of",number,"is {:b}".format(number))
print("The octal value of",number,"is {:o}".format(number))
print("The hexadecimal value of",number,"is {:X}".format(number))
print("The scientific notation of",number,"is {:E}".format(number))