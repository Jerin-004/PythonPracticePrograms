## daemon thread = a thread that runs in the background, not important for program to run
##                 your program will not wait for daemon to complete before exiting
##                 non-daemon thread cannot normally be killed, stay alive task is complete

##                 ex. background tasks, garbage collection, waiting for input, long running process             

import threading
import time

def timer():
    print()
    count = 0 
    
    while True:
        time.sleep(1)
        count += 1
        print()
        print("logged in for: ",count)

# x.setDaemon(True)
x = threading.Thread(target=timer,daemon=True)
x.start()


print(x.isDaemon())

user_input = input("Do you wish to exit: ")