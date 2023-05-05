## walrus operator :=

# new to Python 3.8
# assignment expression also known as walrus operator
# assigns values to variables as part of a larger expression 

happy = True
print(happy)

print(happy := True)

foods = list()
while True:
    food = input("Enter the food that you like: ")
    if food == "q":
        break
    foods.append(food)

foods = list()
while food := input("Enter the food that you like: ") != "q":
    foods.append(food)