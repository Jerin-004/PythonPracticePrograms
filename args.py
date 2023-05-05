# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

def add(*data):  # you can change it to any name from args
    sum1 = 0
    data = list(data)
    data[0] = 3
    for values in data:
        sum1 += values
    return sum1


print(add(2, 2, 2))
