## abstract class

## Prevents a user from creating an object of the class
## + compels a user to override abstract methods in a child class

## abstract class = a class which contains one or more abstract methods.
## abstract method = a method that has a declaration but does not have an implementation.

from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You are driving the car")

    def stop(self):
        print("You have stopped the car")

    
class Motorcycle(Vehicle):

    def go(self):
        print("You are driving the motor cycle")

    def stop(self):
        print("You have stopped your motorcycle")


# vehicle = Vehicle()
car = Car()
motor_cycle = Motorcycle()

# vehicle.go()
car.go()
motor_cycle.go()

car.stop()
motor_cycle.stop()