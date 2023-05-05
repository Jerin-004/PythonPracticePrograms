## slicing
a = "Chennai"

first_name = a [0:3]
last_name = a [4:]
print(first_name,last_name)
joke_name = a [0:7:2] # start:stop:step which means the last thing prints only the 2nd str
joke_name = a [::2]# you can also write this way
print(joke_name)

reversed_a = a [::-1]  ## the third value decides in which order the value should be printed
print(reversed_a)

website = "http://google.com"
website_2 = "http://wikipedia.com"
slice = slice(7,-4)      ## a slice function will be separated by comma not collen
print(website[slice])
print(website_2[slice])