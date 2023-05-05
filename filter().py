## filter() = creates a collection of elements from an iterable for which a function returns true

## filter(function,  iterable)


people = [("Rachel", 19),
          ("Monica", 18),
          ("Phoebe", 17),
          ("Joey", 16),
          ("Chandler", 21),
          ("Ross", 20)]

age = lambda data: data[1] >= 18
names = lambda data: data[0]

Votable_people = list(filter(age, people))

sorted_people = sorted(Votable_people, key=names)

for i in Votable_people:
    print(i)
print()

for i in sorted_people:
    print(i)
