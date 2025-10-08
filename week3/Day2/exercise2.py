# Display
# First 2 rows
# Only the "Name" column
# Shapes and column names

import pandas as pd

data = {
    "Name" : ["Ali","Sara","Usman"],
    "Age"  : [23,24,25],
    "City" : ["Lahore","Islamabad","Quetta"],
    "Score": [67,58,88]
}

df = pd.DataFrame(data)
print(df.head(2))
print(df["Name"])
print(df.shape)
print(df.columns)

# Add a new column that says "pass" if score >= 60 else says "fail"

df["Status"] = ["Pass" if score >=60 else "Fail"
for score in df["Score"]]

print(df)