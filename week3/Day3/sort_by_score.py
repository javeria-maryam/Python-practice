# Sort students by score (highest to lowest)
# Print their names and score

import pandas as pd

df = pd.read_csv("students.csv")

sorted_df = df.sort_values(by = "Score", ascending=False)

print("Sorted by score")
print(sorted_df[["Name" , "Score"]])