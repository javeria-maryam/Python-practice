#Function for each operation: add, subtract, multiply, divide.

#Ask the user which operation they want and two numbers.


def addition(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    if num2==0:
       print("Error: cannot divide by zero!")
    else:
       return num1/num2

num1= int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose any operator: '+, - , * , /': ")


if operator == "+":
 print("Result:",addition(num1,num2))

elif operator == "-":
   print("Result:",subtract(num1,num2))

elif operator == "*":
   print("Result:",multiply(num1,num2))

elif operator == "/":
   print("Result:", divide(num1,num2))

else:
   print("Invalid Operator!")



