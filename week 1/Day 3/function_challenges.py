# 1. Write a function that returns the factorial of a number.

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
    
num = int(input("Enter a number: "))

print("Factorial of",num,'is',factorial(num))


# 2. Write a function that checks if a string is a palindrome (e.g., “madam”).

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]


word = input("Enter a word: ")

if is_palindrome(word):
 print(word, "is palindrome")

else:
 print(word, "is not palindrome")


# 3.Write a function that calculates the area of a circle given its radius.

import math

def cal_area(rad):
 return math.pi*rad*rad

r = float(input("Enter the radius of the circle: "))
print("The area of circle is", round(cal_area(r),2)) #rounded to 2 decimal places

