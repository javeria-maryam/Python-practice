# File reader with exception handling

file = input("Enter the file name: ")

try:
    with open(file,"r") as f:
        content = f.read()
        print("\n",content)

except FileNotFoundError:
    print("Error! File does not exist")

finally:
    print("Task Completed")

    