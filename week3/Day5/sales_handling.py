# Load the CSV and show first 10 rows.
# Print total rows and columns.
# Check for missing values and fill them.
# Drop duplicate rows.
# Rename one column.
# Add a new column — for example, Bonus = Sales * 0.1.
# Save your cleaned file as cleaned_sales.csv.

import pandas as pd

df = pd.read_csv("sales.csv")

print("First 10 rows:\n",df.head(10))

print("\nTotal rows and columns:\n",df.shape)

print("\nMissing values:\n",df.isnull().sum())        # total missing values

df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())  # filling missing values

df.drop_duplicates(inplace = True)                               # droping duplicates

df.rename(columns= {"Reigon":"City"}, inplace = True)            # renaming column "Reigon" to "City"

df["Total sale"] = df["Price"] * df["Quantity"]

df.to_csv("cleaned_sales.csv", index = False)