#Function that takes a number and returns whether it’s even or odd.

def myfunc(num1):
    
    if num1%2==0:
        return "Even"
    else:
        return "Odd"
    
    
num1 = int(input("Enter a number: "))
print("The number is",myfunc(num1))
