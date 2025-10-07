import numpy as np

# Creating 1D and 2D numpy arrays

arr1 = np.array([10,20,30,40,50])

arr2 = np.array([[10,20,30],
                 [40,50,60],
                 [70,80,90]])

print("1D Array:",arr1)
print("2D Array:\n",arr2)

# Accessing specific elements.
# 1D Example

print("First element:",arr1[0])    # First element
print("Last element:",arr1[-1])    # Last element

#2D Example

print(arr2[0,1])                  # Element form row 0, column 1
print(arr2[1,0])                  # Element from row 1, column 0

#Slicing in Numpy

#1D Example

print(arr1[:3])                  # First 3 elements
print(arr1[1:4])                 # Elements from index 1 to 3

#2D Example

print(arr2[0:2, 1:3])           # First 2 rows, columns 1 & 2

# Modifying Values

arr1[0] = 100
print("Updated array:",arr1)

arr2[1,2] = 99
print("Updated array:",arr2)