##  Basics of class

from car2 import Car

car_1 = Car("Ford","Figo","2012","Orange")
car_2 = Car("Tata","Scorpio","2014","White")

car_1.Wheels = 2
Car.Wheels = 2   ## affects all instances of this class

print(car_1.Wheels)
print(car_2.Wheels)

print(Car.Wheels)