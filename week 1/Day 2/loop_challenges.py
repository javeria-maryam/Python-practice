# 1. Print numbers from 1 to 50.

for i in range (1,51):
    print(i)

# 2. Print only even numbers between 1–100.

for i in range (1,101):
    if i%2==0:
        print(i)
    
# 3. Print the factorial of a number (e.g., 5! = 120).

num = 5
fact = 1

for i in range(1, num + 1):   # loop from 1 → num
    fact *= i

print("Factorial of", num, "is:", fact)



