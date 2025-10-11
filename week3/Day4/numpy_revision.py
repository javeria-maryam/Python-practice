# Tasks:

# Create a 2D NumPy array with shape (4,3) filled with random integers between 10–50.

# Print:
# First row
# Last column
# Middle two rows
# Perform operations:
# Mean, median, and standard deviation of the array
# Filter elements > 25

import numpy as np
import random

arr = np.random.randint(10,50,(4,3))

print(arr)
print("\nFirst row:",arr[0])
print("\nLast Column:",arr[:,-1])
print("\nMiddle two rows:",arr[1:3])


mean = np.mean(arr)
std = np.std(arr)
filter = arr[arr > 25]

print(f"Mean: {mean:.2f}")
print(f"Standard deviation: {std:.2f}")
print("Elements > 25:",filter)

