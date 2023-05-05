##  exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter the numerator number to divide: "))
    denominator = int(input("Enter the denominator to divide by: "))
    answer = numerator/denominator

except ZeroDivisionError as e:
    print("\n")
    print(e)
    print("you can't divide by zero!")

except ValueError as e:
    print("\n")
    print(e)
    print("Plz Enter numbers only")

except Exception as e:
    print("\n")
    print(e)
    print("Something went wrong :(")

else:
    print(answer)

finally:
    print("\nThank you!")