# Create a 2D array of shape (3, 3) with numbers from 1–9.

# Print the second row.

# Print the third column.

# Reshape it into (1, 9).

import numpy as np

arr = np.arange(1,10).reshape(3,3)


print("Second row:",arr[1])
print("Third Column:",arr[:,2])

reshaped = arr.reshape(1,9)
print(reshaped)

