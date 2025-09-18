# Write a Python program that asks the user to enter a year, and then checks whether the year is a leap year or not.

#  A year is a leap year if:

# It is divisible by 4 and not divisible by 100, OR

# It is divisible by 400.

year = int(input("Enter a year: " ))

if (year%4==0 and year%100!=0) or (year%400==0):
 print(f"{year} is a Leap year")

else:
 print(f"{year} is not leap year")

