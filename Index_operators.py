# Index operators [] = gives acces to a sequence's element (str, lists, tuples)

place = "chennai London!"

if place[0].islower():
    place = place.capitalize()

print(place)

first_place = place[:7].upper()
last_place = place[8:-1].lower()
last_character = place[-1]


print(first_place)
print(last_place)
print(last_character)