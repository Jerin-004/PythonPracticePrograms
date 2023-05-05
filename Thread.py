## thread = a flow of execution. Like a separate order of instructions.
##          However each thread takes a turn runnning to achieve concurrency (continuously)
##          GIL = (global interpreter lock), is the thing which that limits us from accesing one thread at a time
##          allows only one thread to hold the control of the Python interpreter at any one time

## CPU bound = program/task spends most of its time waiting for internal events (CPU intensive)
##             it is better to use multiprocessing

## io bound = program/task spends most of its time waiting for external events (user input, web scraping)
##            its better to use mutlithreading 


import threading
import time 


def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")

def drink_milk():
    time.sleep(4)
    print("You drank your milk")

def study():
    time.sleep(5)
    print("You finished studying")



x = threading.Thread(target=eat_breakfast)
x.start()

y = threading.Thread(target=drink_milk)
y.start()

z = threading.Thread(target=study)
z.start()


x.join()
y.join()
z.join()


# eat_breakfast()
# drink_milk()
# study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())