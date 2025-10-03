# From the array [12, 5, 7, 18, 25, 40, 3, 11],

# Print all numbers between 10 and 30.

# Find their sum and mean.

import numpy as np

arr = np.array( [12, 5, 7, 18, 25, 40, 3, 11])

print("Numbers between 10 and 30",arr[(arr<30) & (arr>10)])
print("Sum:",np.sum(arr))
print("Mean:",np.mean(arr))
