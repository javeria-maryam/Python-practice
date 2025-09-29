# Write a program to:

# Open a file notes.txt in append mode.

# Add one new line "Learning Python is fun!".

# Reopen the file and print its content.


with open("notes.txt","a") as f:
    f.write("\nLearning Python is fun!")

with open("notes.txt","r") as f:
    print(f.read())