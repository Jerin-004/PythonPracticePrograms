## method chaining  = calling multiple methods sequentialy
##                    each call performs an action on the same object and returns self

class Car:

    def start(self):
        print("You started the engine")
        return self

    def drive(self):
        print("You are driving the car")
        return self

    def brake(self):
        print("You stepped on the brakes")
        return self

    def stop(self):
        print("You stop the car")
        return self

car = Car()

# car.start().drive()
# car.brake().stop()

car.start()\
.drive()\
.brake()\
.stop()