# Slicing Practice

# Create an array of numbers 1–20.

# Print:

# First 5 numbers

# Last 5 numbers

# Only even numbers

import numpy as np

arr = np.arange(1,21)


print("First 5 numbers:",arr[:5])
print("Last 5 numbers:",arr[-5:])
print("Even numbers are:",arr[arr % 2 ==0])
