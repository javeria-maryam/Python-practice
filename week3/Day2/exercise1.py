# Create a dictionary of your own data (Name, Age, City, Score).
# Convert it into a DataFrame and print it.

import pandas as pd

data = {
    "Name" : ["Ali","Sara","Usman"],
    "Age" : [23,24,25],
    "City": ["Lahore","Islamabad","Quetta"],
    "Score" : [67,66,88]
}

s = pd.DataFrame(data)

print(s)