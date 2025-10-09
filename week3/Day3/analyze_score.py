# Find and print:

# Average score

# Highest and lowest score

# Total students who passed

import pandas as pd

df = pd.read_csv("students.csv")

print("Average score:",df["Score"].mean())
print("Higest score:",df["Score"].max())
print("Lowest score:",df["Score"].min())
print("Total students who have passed:",(df["Status"]=="Pass").sum())







