# Dictionary = a changable, unordered collection of unique key:values pairs
#              Fast because they are hashing, allow us to access a value quickly


capitals = {"India":"New Delhi",
            "USA":"Washington DC",
            "China":"Benjing",
            "Russia":"Moscow"}

capitals.update({"Germany":"Berlin"})
capitals.update({"India":"Chennai"})
capitals.pop("China")    ## it used to remove a value
capitals.clear()

print(capitals["Germany"])
print(capitals.get("Germany"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for Keys,values in capitals.items():
    print(Keys, values)