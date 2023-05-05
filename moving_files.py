## moving files

import os 

source = "test.txt"
destination = "E:\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)  ## must type the both source and destination
        print(source,"was moved")

except FileNotFoundError:
    print(source,"not found!")