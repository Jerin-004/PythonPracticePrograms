import time

## while loop = unlimited
## for loop = limited

for i in range(50):
    print(i+1)

for i in range(50,100+1,2): # count up by two
    print(i)

for i in "Jerin":
    print(i)
                       # starting
for seconds in range(10,0,-1): ## -1 = reverse order
    print(seconds)      ## ending
    time.sleep(1)

print("Happy New year") 

rows = int(input("Enter the number of rows:"))
columns = int(input("Enter the number of column:"))
symbol = input("Enter the symbol:")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()    ## enters into a new line