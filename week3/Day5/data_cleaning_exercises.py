# Tasks:

# Find how many missing values each column has.

# Fill missing values in “Age” with the average age.

# Fill missing “Score” values with the median score.

# Display the cleaned DataFrame.


import pandas as pd
data = {
    "Name": ["Ali", "Sara", "Hassan", "Ayesha", "Usman"],
    "Age": [22, None, 24, None, 21],
    "Score": [85, 90, None, 75, 88]
}
df = pd.DataFrame(data)

print("Missing values:\n",df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())

df["Score"] = df["Score"].fillna(df["Age"].mean())

print("\nCleaned DataFrame:\n",df)



# Tasks:

# Check for duplicate rows.

# Remove duplicate rows.

# Print the new DataFrame shape and data.

data = {
    "ID": [101, 102, 103, 101, 104],
    "Name": ["Ali", "Sara", "Hassan", "Ali", "Usman"],
    "Score": [85, 90, 88, 85, 92]
}
df = pd.DataFrame(data)

df.drop_duplicates(inplace=True)

print(df.shape)
print("\n",df)
