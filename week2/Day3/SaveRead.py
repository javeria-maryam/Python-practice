#Write a program to:

# Ask the user to enter 5 student names.

# Save them in a file students.txt.

# Read the file and print all names.


with open ("students.txt","w") as f:
    for i in range(5):
     name = input(f"Enter the name of student {i+1}: ")
     f.write(name+"\n")

with open("students.txt","r") as f:
   content = f.read()
   print(content)
