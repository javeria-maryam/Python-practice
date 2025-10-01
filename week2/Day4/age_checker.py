# Age Checker with custom error.

def myage(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    else:
        print("Valid age:",age)

try:
    age = int(input("Enter your age: "))
    myage(age)

except ValueError as e:
    print(e)


    
