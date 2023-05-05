## Python Object Oriented programming (POOP)

from car import Car

car_1 = Car("Ford","Figo","2012","Orange")
car_2 = Car("Tata","Scorpio","2014","White")

print(car_1.company)
print(car_1.model)
print(car_1.year)
print(car_1.color)

print(car_2.company)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_1.drive()
car_2.stop()