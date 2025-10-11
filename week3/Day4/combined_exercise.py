# Task:

# Use NumPy to generate a random array of 10 students’ marks (between 50–100).
# Convert it into a Pandas DataFrame with columns ["Student", "Marks"].
# Add a "Grade" column:
# "A" if marks ≥ 90
# "B" if marks between 80–89
# "C" if marks < 80
# Calculate and print:
# Class average
# Count of each grade

import numpy as np
import pandas as pd


marks = np.random.randint(50,101,10)
students = [f"Student {i}" for i in range(1,11)]

df = pd.DataFrame({
    "Students" : students,
    "Marks" : marks
})

def grade(m):
    if m >=90:
        return "A"
    elif m >=80:
        return "B"
    else:
        return "C"
    
df["Grade"] = df["Marks"].apply(grade)

print(df)

average = round(df["Marks"].mean(),2)
count = df["Grade"].value_counts()

print("\nClass average:",average)
print("\nGrade count:\n",count)

