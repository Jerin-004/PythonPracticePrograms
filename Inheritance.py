## Inheritance

class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")
    
    def sleep(self):
        print("This animal is sleeping")

class Dog(Animal):

    def run(self):
        print("This dog is running")

class Fish(Animal):

    def swim(self):
        print("This fish is swimming")

class Eagle(Animal):

    def fly(self):
        print("This eagle is flying")

dog = Dog()
fish = Fish()
eagle = Eagle()

## inherited values
print(dog.alive)
fish.eat()
eagle.sleep()

## unique value
dog.run()
fish.swim()
eagle.fly()