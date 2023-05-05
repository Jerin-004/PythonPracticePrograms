## Time module

## epic also known as epoch = a date and time from which a computer measures system time

import time

print(time.ctime(100000000))      ## converts a time expressed in seconds since epoch to a readable string
                          ## epoch = when your computer thinks time began (reference point)

print(time.time())     ## return current seconds since epoch

## Method 1:

print(time.ctime(time.time()))   ## current time

## Method 2:(### string format time)

time_object = time.localtime()
local_time = time.strftime("%B %d %Y %I:%M:%S",time_object)      
print(local_time)
print(time_object)

time_object = time.gmtime()    ### UTC time
UTC_time = time.strftime("%B %d %Y %I:%M:%S",time_object)
print(UTC_time)

print(time_object)


## Example 2:(## string representative time)

time_string = "07 August, 2021"
time_object = time.strptime(time_string, "%d %B, %Y")   
print(time_object)


## Example 3:(## tuple representative of a relative time)

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)

time_tuple = (2020, 9, 29, 8, 45, 0, 0, 0, 0,)
time_string = time.asctime(time_tuple)
print(time_string)

## Example 4:(## tuple representative of a relative time and converts it to seconds since the epoch)

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)

time_tuple = (2020, 9, 29, 8, 45, 0, 0, 0, 0,)
time_string = time.mktime(time_tuple)
print(time_string)
