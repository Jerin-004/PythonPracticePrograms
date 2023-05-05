# list = a variable wish stores multiple values

fruits = ["apple","banana", "orange", "pineapple"]

fruits[0] = "dragon fruit"  ## replacing an element

fruits.append("grapes")
fruits.remove("pineapple")
fruits.pop()  ## it will remove the last element
fruits.insert(1,"black apple")
fruits.reverse()
fruits.sort()
fruits.clear()

for data in fruits:
    print(data)


# 2D lists

# breakfast = ["dosa", "idly", "chappati"]
# drinks  = ["soda", "coffee", "tea"]
# dessert = ["cake", "pudding", "ice creame"]

# food = [breakfast,drinks,dessert]

# try:
#     print(food[1][2])

# except IndexError:
#     print("list's index number is out of range")