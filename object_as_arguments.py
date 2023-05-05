## objects as arguments

class Car:

    color = None

class Motorcycle:

    color = None

def change_color(vehicle,color):
    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

change_color(car_1,"red")
change_color(car_2,"green")
change_color(car_3,"yellow")

change_color(bike_1,"Black")

print("The color of car_1 is",car_1.color)
print("The color of car_2 is",car_2.color)
print("The color of car_3 is",car_3.color)
print("The color of the bike is",bike_1.color)