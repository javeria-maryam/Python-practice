import numpy as np

# Dictionary of students and their marks
students = {
    "Ali": 85,
    "Sara": 92,
    "Omar": 78,
    "Hina": 88,
    "Usman": 95
}

# Extract all marks into a list
marks = list(students.values())

# Calculate mean and standard deviation
mean_marks = np.mean(marks)
std_marks = np.std(marks)

# Print results rounded to 1 decimal place
print(f"Average Marks: {mean_marks:.1f}")
print(f"Standard Deviation: {std_marks:.1f}")
