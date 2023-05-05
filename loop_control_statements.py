## break = used to terminate the loop entirely
## continue = skips to next iteration of the loop
## pass = does nothing,acts as a placeholder

## loop control statements = changes the loops

while True :
    name = input("Enter your name:")
    if name != "":
        break

phone_number = "123-456-789"

for i in phone_number:
    if i == "-":
        continue
    print(i, end ="")

for i in range(1,10):
    if i == 2:
        pass
    else:
        print(i)