# Simple Calculator

# Taking input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input('Select an operator ("+", "-", "*", "/"): ')

# Performing operations
if operator == '+':
    print(f"Sum of {num1} and {num2} is: {num1 + num2}")

elif operator == '-':
    print(f"Difference of {num1} and {num2} is: {num1 - num2}")

elif operator == '*':
    print(f"Multiplication of {num1} and {num2} is: {num1 * num2}")

elif operator == '/':
    if num2 == 0:
        print("Error: Cannot divide by zero!")
    else:
        print(f"Division of {num1} and {num2} is: {num1 / num2}")

else:
    print("Invalid operator! Please choose +, -, * or /.")
