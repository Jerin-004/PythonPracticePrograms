## funtion to variables
# beware this some cool stuff

def hello():
    print("Hello!")


# prints the address of the function
print(hello)
hi = hello
print(hi)

# now hello function has a new clone
hello()
hi()

say = print
say("Hello world :D")