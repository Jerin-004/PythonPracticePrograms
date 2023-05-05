## sort() method = used with lists
## sort() funtion = used with iterables

# Example 1:

students = ("Balaji", "David", "Chijith", "Ajay")

students.sort(reverse=True)   ### arrnges the list in a alabetical order but only works in lists
sorted_students = sorted(students,reverse=True)      ### sorted funtion can be used within any iterables

for i in sorted_students:
    print(i)

# Example 2:

# students = [("Balaji","C",12),
#             ("David","A",17),
#             ("Chijith","B",23),
#             ("Ajay","F",34)]

students = (("Balaji","C",12),
            ("David","A",17),
            ("Chijith","B",23),
            ("Ajay","F",34))

# def grade(grades):
#     return grades [1]
grade = lambda grades:grades[1]
# students.sort(key=grade,reverse=True)

age = lambda age:age[2]
# students.sort(key=age)

sorted_students = sorted(students,key=grade)

for i in sorted_students:
    print(i)