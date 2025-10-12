import pandas as pd

df = pd.read_csv("students.csv")
 
# Exploring the Dataset.

print(df.head(),"\n")                       # gives first 5 rows.      
print(df.info(),"\n")                       # gives column names, data types, and missing values count.
print(df.describe(),"\n")                   # gives stats (mean, min, max, etc.) for numeric columns.
print(df.shape,"\n")                        # returns (rows, columns)
print(df.columns,"\n")                      # lists all column names.

# Handling missing values.

print(df.isnull().sum())

# Option 1: Fill missing values
df["Score"].fillna(df["Score"].mean(), inplace=True)

# Option 2: Drop rows with missing values
# df.dropna(inplace=True)

# Removing duplictes
df.drop_duplicates(inplace=True)

# Renaming columns
df.rename(columns={"Score" : "Marks"}, inplace = True)

# Changing Datatypes
df["Age"] = df["Age"].astype(int)

# Saving cleaned dataset
df.to_csv("cleaned_students.csv", index = False)

