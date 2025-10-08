# Add a new column that says "pass" if score >= 60 else says "fail"


import pandas as pd

data = {
    "Name" : ["Ali","Sara","Usman"],
    "Age"  : [23,24,25],
    "City" : ["Lahore","Islamabad","Quetta"],
    "Score": [67,58,88]
}

df = pd.DataFrame(data)

df["Status"] = ["Pass" if score >= 60 else "Fail" for score in df["Score"] ]

print(df)