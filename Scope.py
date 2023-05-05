## scope = the region tath a variable is recognized
##         A verticle is only available from inside the region it is created.
##         A global and locally scoped version of a variable can be created


name = "Jerin"  ## Global scope (available only inside this funtion)

def full_name():
    name = "Chijith" ## Local scope (available only inside this function)
    print(name)

full_name()
print(name)
