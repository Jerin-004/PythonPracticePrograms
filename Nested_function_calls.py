## nested function calls = function calls inside other function calls
##                         innermost function calls are resolved first
##                         returned value is used as arguments for the next outer function

value = input("Enter a number:")
value = float(value)
value = abs(value)
value = round(value)
print(value)

print(round(abs(float(input("Enter a number:")))))