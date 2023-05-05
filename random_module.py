## random module

import random

x = random.randint(1,10)   ## for int
y = random.random()        ## for float

game = ["rock", "paper", "scissors"]
z = random.choice(game)     ## both choice and shuffle are the same

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)        ## shuffle method can be done like this only



print(x)
print(y)
print(z)
print(cards)
