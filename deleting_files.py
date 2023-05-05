## Deleting files 

import os
import shutil 

path = "folder"


try:
    os.remove(path)    ## deleting a file
    os.rmdir(path)       ## deleting a empty folder
########      shutil.rmtree(path)   ## deleting a forlder containg files it can bee very dangerous which can even delete a whole drive and its files                   

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("You don't have the permission to delete that")


else:
    print(path,"was deleted")