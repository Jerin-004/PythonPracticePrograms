## reading a file 

file = input("Enter the file name or file's directory name:")

try:
    with open(file) as data:
        print(data.read())

except FileNotFoundError:
    print("File not found :(")