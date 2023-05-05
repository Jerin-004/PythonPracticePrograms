## str.format() = optional method that gives user 
##                more control  when dispplaying output

animal = "cow"
item = "moon"

print("The",animal,"jumped over the",item)
print("The {} jumped over the {}".format(animal,item))
print("The {1} jumped over the {1}".format(animal,item))  ## positional argument
print("The {animal} jumped over the {animal}".format(animal="cow",item="moon"))  ## keyword argument

poem = "The {} jumped over the {}"
print(poem.format(animal,item))

# paddling in str.format()

name = "Jerin"

print("Hello my name is {}".format(name))
print("Hello my name is {0:20}.Nice to meet you".format(name))
print("Hello my name is {:<20}.Nice to meet you".format(name))
print("Hello my name is {:>20}.Nice to meet you".format(name))
print("Hello my name is {:^20}.Nice to meet you".format(name))