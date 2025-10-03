# Create a list of 10 numbers
# Find mean and std uisng numpy
# Round upto 2 decimal places

import numpy as np

arr = np.arange(1,11)

mean = np.mean(arr)
std = np.std(arr)

print(f"Mean: {mean:.2f}")
print(f"Standard Deviation: {std:.2f}")