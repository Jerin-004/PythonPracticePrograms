## Keyword arguments = arguments preceded by an identifier when we pass them to a funtion
##                     The order of the arguments doesn't matter, unlike position aarguments
##                     Python knows the names of the arguments that our function recoives

def hello(first,last,last_character):
    print("Hello",first,last,last_character)

hello(last_character="!",last="Jerin",first="Chijith")