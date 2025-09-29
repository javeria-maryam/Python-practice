# Word frequency counter from a file story.txt


with open("story.txt","w") as f:
    f.write("I am learning Python, Python is very powerful and simple.")

with open("story.txt","r") as f:
    content = f.read()
    
words = content.lower().split()

cleaned_words = [word.strip(".,?") for word in words]

counter = {}

for word in cleaned_words:
    counter[word] = counter.get(word,0)+1
    
print("World Frequencies:")

for word, count in counter.items():
    print(word,":",count)