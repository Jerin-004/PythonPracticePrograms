##  multiple inheritance = when a child class is derived from more than one parent class

class Prey:

    def escape(self):
        print("This animal is escaping")

class Predator:

    def hunt(self):
        print("This animal is hunting")

class Deer(Prey):
    pass

class Lion(Predator):
    pass

class Fish(Prey,Predator):
    pass

deer = Deer()
lion = Lion()
fish = Fish()

deer.escape()
lion.hunt()
fish.hunt()
fish.escape()