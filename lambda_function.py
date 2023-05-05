# ## lambda function = function written in 1 line using lambda keyword
#                     accepts any number of arguments, but only has one expression.
#                     (think of it as a shortcut)
#                     (useful if needed for a short period of time, throw-away)

## lamba parameters:expression

double = lambda x : x*2
print(double(5))

multiply = lambda a,b : a*b
print(multiply(6,5))

add = lambda w,e,r : w + e + r
print(add(3,3,3))

full_name = lambda first_name,last_name : first_name+" "+last_name
print(full_name("Chijith","Jerin"))

age = lambda age : True if age >= 18 else False
print(age(90))