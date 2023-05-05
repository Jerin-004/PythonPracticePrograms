## logical operators (and,or,not)

temp = int(input("What is the temperature outside?:"))

if temp >= 0 and temp <= 30:    ## both condition must be true
    print("the temperature is good today!")
    print("go explore!")

if (temp < 0 or temp > 30):   ## if any one is true the entire statemont will be true
    print("the temperature is bad dont go outside!!")

# not function flips it from being false to true and true to false


name = None

while not name:
    name = input("Enter your name:")

print("hello",name)