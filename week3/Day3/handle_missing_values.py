# Add a missing value manually

# Use .fillna() to replace it with the average

import pandas as pd
import numpy as np

df = pd.read_csv("students.csv")

df.loc[2,"Score"] = np.nan
print("Before handling missing values")

print(df)

df["Score"].fillna(df["Score"].mean(), inplace=True)

print("\n After handling missing values:")

print(df)

