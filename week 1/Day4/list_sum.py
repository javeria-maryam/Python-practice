#Write a program that finds the sum of all elements in a list.

mylist = list(map(int,input("Enter a list of numbers: ").split()))

total = sum(mylist)

print("Sum is:",total)