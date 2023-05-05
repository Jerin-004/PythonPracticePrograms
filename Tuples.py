# tuple = collection which is ordered and unchangeable used to group together related data

student_data = ("Ramesh", "14", "male")

print(student_data.count("male"))  ## it counts how many times the value appears
print(student_data.index("Ramesh"))

for data in student_data:
    print(data)

if "14" in student_data:
    print("his age is 14")
