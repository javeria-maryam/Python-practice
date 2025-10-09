# Load the students.csv file
# Print only the names of students who have passed

import pandas as pd

df = pd.read_csv("students.csv")

passed = df[df["Status"] == 'Pass']

print("Passed Students")
print(passed['Name'])