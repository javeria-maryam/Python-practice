# Create a file called story.txt.

# Write a short paragraph (3–4 sentences) into it.

# Write a Python program that:

# Opens story.txt

# Reads the content

# Counts how many words are in the file

# Prints the word count

with open("story.txt","w") as f:
    f.write("I am a student. I am learning Python. I am 23 years old")

with open("story.txt","r") as f:
    content = f.read()

words = content.split()

print("Total number of words are:",len(words))

