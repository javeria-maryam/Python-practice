# Find the total and average sales.

# How many days had sales below 250?

# Print all the sales that were between 300 and 500 (inclusive).

# What is the index (day number) of the highest sales day?
# (hint: np.argmax)

# On how many days did sales increase compared to the previous day?

import numpy as np

sales = np.array([250, 300, 200, 400, 150, 500, 350, 100, 450, 600])

total = np.sum(sales)
average = np.mean(sales)
below = sales[sales < 250]
between = sales[(sales <= 500) & (sales >= 300) ]
daynum = np.argmax(sales)
increases = (sales[1:] > sales[:9]).sum()


print("total sales:",total)
print("Average sales:",average)
print("Sales below 250:",below)
print("Sales between 300 and 500:",between)
print("Index number of higest sales day:",daynum)
print("Number of days sales increased:", increases)



