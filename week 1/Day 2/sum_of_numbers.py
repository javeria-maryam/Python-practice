# Ask user for a number n.

# Use a while loop to calculate the sum of numbers from 1 → n.

#Example: n=5 → 1+2+3+4+5 = 15

n = int(input("Enter a number: "))

i = 1

total =0

while i <=n:
    total+=i
    i+=1
print(total)




