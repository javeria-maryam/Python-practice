# Create two lists: months = ["Jan", "Feb", "Mar", "Apr", "May"] and sales = [200, 300, 250, 400, 350]

# Plot a bar chart showing sales per month

# Add colors and labels

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"] 
sales = [200, 300, 250, 400, 350]

plt.bar(months,sales,color='black')
plt.title("Sales per month")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
