# Create a tuple of 5 colors, access elements by index.

mytuple = tuple(input("Enter 5 colors separated by space: ").split())


for i in range(len(mytuple)):
    print("Index", i, "→", mytuple[i])


