# Grade Calculator

# Input marks, print grade:

# >=90: A

# 80–89: B

# 70–79: C

# 60–69: D

# <60: Fail.

marks = int(input("Enter your marks: "))

if marks >=90:
    print("A")
elif 80<= marks <=89:
    print("B")
elif 70<=marks <=79:
    print("C")
elif 60<=marks<=69:
    print("D")
elif marks < 60:
    print("FAIL")
    