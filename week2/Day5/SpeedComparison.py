# Speed Comparison

# Compare sum of 1 million numbers using Python list vs NumPy array.

import numpy as np
import time

lst = list(range(1_00_001))
arr = np.array(lst)

start = time.time()
total_list = sum(lst)
end = time.time()

print("Sum of list:",total_list)
print("Time taken by list:",end - start)

start = time.time()
total_arr = np.sum(arr)
end = time.time()

print("Sum of array:",total_arr)
print("Time taken by array:",end - start)