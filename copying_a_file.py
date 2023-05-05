
## copying a file

# copyfile() = copies contents of a file 
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metaata (file's creation and modification times)

import shutil 

shutil.copyfile("test.txt","copy.txt")  ## source,destination
# shutil.copy("test.txt","copy.txt")  ## all works the same
# shutil.copy2("test.txt","copy.txt")  ## the same

with open("copy.txt","a") as file:
    file.write("\nYo fools this a copy!!")
