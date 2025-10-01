# Division Calculator with Exception Handling

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    result = a/b
    print(f"Result: {result}")

except ValueError:
    print("Error! Pleasa enter a number: ")

except ZeroDivisionError:
    print("Error! Cant divide by zero")

finally:
    print("Calculation complete")