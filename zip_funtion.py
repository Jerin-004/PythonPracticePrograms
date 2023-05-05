## zip(*iterables) = combining elements from two or more iterables (lists, tuples, sets, etc....)
##                   creates a zip object with paired elements stored in tuples for each elements 

## Example 1:

username = ["Chijith", "Jerin", "Messi"]
password = ("jerin1234", "abc123", "messi123")

# users = list(zip(username,password))

users = dict(zip(username,password))

print(type(users))

# for i in users:
#     print(i)

for key,value in users.items():
    print(key+" : "+value)


## Exapmle 2:

username = ["Chijith", "Jerin", "Messi"]
password = ("jerin1234", "abc123", "messi123")
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = zip(username,password,login_date)

print(type(users))

for i in users:
    print(i)