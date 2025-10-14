#cleaning and analyzing data

import pandas as pd

df = pd.read_csv("sales.csv")

print("Original Data:\n",df.head())
print(df.isnull().sum())

df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())
df["Price"] = df["Price"].fillna(df["Price"].mean())


df["total_sale"] = df["Price"] * df["Quantity"] * (1 - df["Discount"]/100)

df.columns = df.columns.str.lower().str.replace(' ','_')

df.drop_duplicates(inplace=True)

print("\nCleaned Data:\n",df.head())

print("\n------Basic Statistics------")
print(df.describe())

city_sale = df.groupby("city")["total_sale"].sum()
print("\nTotal sale by city:\n",city_sale)

product_avg_price = df.groupby("product")["price"].mean()
print("\nProduct wise average price:\n",product_avg_price)

best_selling =df.groupby("product")["total_sale"].sum().idxmax()
print("\nBest selling product is:",best_selling)

import matplotlib.pyplot as plt 

city_sale.plot(kind = "bar" , title = "Total sales by city")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.show()

df.to_csv("cleaned_sales_data.csv", index = False)
print("\n✅ Cleaned data saved to 'cleaned_sales_data.csv'")