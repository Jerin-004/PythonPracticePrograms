## super() = Funtion used to give access to the method of a parent class.
##           Returns a temporary object of a parent class when used

class Rectangle:

    def __init__(self,width,lenght):
        self.width = width
        self.lenght = lenght

class Square(Rectangle):

    def __init__(self, width, lenght):
        super().__init__(width, lenght)

    def area(self):
        return self.width*self.lenght
    
class Cube(Rectangle):

    def __init__(self, width, lenght,height):
        super().__init__(width, lenght)
        self.height = height

    def volume(self):
        return self.width*self.lenght*self.height

sqaure = Square(3,3)
cube = Cube(3,3,3)


print(sqaure.area())
print(cube.volume())

# -----------------------------------------------------