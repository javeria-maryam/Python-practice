# Tasks:

# Create a DataFrame manually using a dictionary:
# Convert to DataFrame, then:
# Display first 3 rows
# Sort by score (descending)
# Filter students with score > 80
# Calculate mean and max score
# Add a new column "Status": "Pass" if score ≥ 80 else "Fail"

import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Usman", "Ayesha", "Bilal"],
    "Score": [85, 92, 78, 90, 88],
    "Age": [20, 22, 21, 23, 20]
}

df = pd.DataFrame(data)
print("Original dataframe:\n",df)
print("\nFirst 3 rows:\n",df.head(3))

sort = df.sort_values('Score', ascending=False)
print("\nSorted by score:\n",sort)

print("\nMean:",df['Score'].mean())
print("\nMax score:",df['Score'].max())

df["Status"] = df["Score"].apply(lambda x: "pass" if x>=80 else "fail")

print("Udpated df:\n",df)
