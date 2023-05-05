## list comprehension = a way to create a new list with less syntax
##                      can mimic certain lambda funtion,easier to read
##                      list = [expression for item in iterable]
##                      list = [expression for item in iterable if conditional]
##                      list = [expression if/else for item in iterable]

## Example 1:

sqaures = []
for i in range(1,11):
    sqaures.append(i * i)
print(sqaures)

sqaures = [i * i for i in range(1,11)]
print(sqaures)


## Example 2:

students_marks = [100,90,80,70,60,50,40,30,0]
pass_mark = lambda x : x >= 60

passed_marks = list(filter(pass_mark,students_marks))
print(passed_marks)

passed_students = [i for i in students_marks if i >= 60]
print(passed_students)


## Example 3:

passed_students = [i if i >= 60 else "FAILED" for i in students_marks]
print(passed_students)