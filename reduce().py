## reduce() = apply a funtion to a iterable and reduce it a single cumulative value.
##            perfoms funtion on first two elements and repeats process until 1 value remains

## reduce(function, iterable)

import functools

letters = ("H","E","L","L","O")
func = lambda x,y : x+y

words = functools.reduce(func,letters)
print(words)


mutiplication = [5,4,3,2,1]
func2 = lambda x,y : x*y
result = functools.reduce(func2,mutiplication)
print(result)