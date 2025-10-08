# Save the dataframe to a csv file without index.

import pandas as pd

data = {
    "Name" : ["Ali","Sara","Usman"],
    "Age"  : [23,24,25],
    "City" : ["Lahore","Islamabad","Quetta"],
    "Score": [67,58,88]
}

df = pd.DataFrame(data)

df.to_csv("Students.csv", index=False)

print("Data saved successfully to students.csv")



