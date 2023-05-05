## method overriding = is the ability to allow a child to provide a specific implementation of a method that is already provided by one of its parents

class Animal:

    def eat(self):   ## eat(self) these both are called as method signature
        print("This animal is eating")

class Rabbit(Animal):
    
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit = Rabbit()

rabbit.eat()
