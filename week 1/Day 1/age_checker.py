# Age Checker

# Input age → if age < 13 → child, 13–19 → teenager, 20+ → adult.

age = int(input("Enter age: "))

if age < 13:
    print("CHILD")
elif 13 <= age <=19:
    print("TEENAGER")
else:
    print("ADULT")