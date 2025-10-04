import numpy as np


# Example students
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

students = [Student("Ali",67), Student("Sara",89), Student("John",65)]

# Save to file
with open("students.txt","w") as f:
    for s in students:
        f.write(f"{s.name}:{s.marks}\n")

# NumPy stats
marks = [s.marks for s in students]

print(f"Average: {np.mean(marks):.2f}")
print("Highest:",np.max(marks))
print("Lowest:",np.min(marks))