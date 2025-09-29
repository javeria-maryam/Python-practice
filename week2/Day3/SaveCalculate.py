# Write a program to:

# Save 3 numbers into a file numbers.txt.

# Read them back.

# Calculate their sum and average.

with open("numbers.txt","w") as f:
    f.write("\n10")
    f.write("\n20")
    f.write("\n30")

with open("numbers.txt","r") as f:
    numbers = f.readlines()

numbers=[int(num.strip()) for num in numbers]

total = sum(numbers)
average = total/len(numbers)

print("Numbers:",numbers)
print("Sum:",total)
print("Average:",average)
