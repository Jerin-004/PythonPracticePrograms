
## file detection

import os

location = "E:\\【JERIN】\\Jerin_Online Class\\1 Computer Fundamentals test.pdf"

if os.path.exists(location):
    print("That location exists!")
    if os.path.isfile(location):
        print("It is a file!")
    elif os.path.isdir(location):
        print("That is a directory!")

else:
    print("That location does't exist!")