# Exercise 1:

# Create an array of 10 random numbers between 10–100 using:

# arr = np.random.randint(10, 101, 10)


# Tasks:

# Print the array.

# Print the first 5 elements.

# Print the last 3 elements.

# Print all elements greater than 50.

import numpy as np
import random

arr = np.random.randint(10,101,10)

print(arr)

print("First 5 elements:",arr[:5])
print("Last 3 elements:",arr[-3:])
print("Elements greater than 50:",arr[arr > 50])


# Exercise 2:


# Create a 3x3 array:

# arr = np.array([[3, 6, 9],
#                 [12, 15, 18],
#                 [21, 24, 27]])


# ✅ Tasks:

# Extract the first column.

# Extract last two columns.

# Extract middle row.

# Extract middle column

# Extract all values greater than 10 and less than 25.

import numpy as np

arr = np.array([[3, 6, 9],
                [12, 15, 18],
                [21, 24, 27]])

print("First column:",arr[:,0])
print("Last two columns:\n",arr[:,-2:])    # from the 2nd last column to the end
print("Middle row:",arr[1,:])
print("Middle column:",arr[:,1])
print("Values greater than 10 and less than 25:",arr[(arr>10) & (arr<25)])



# Exercise 3:

# You’re given:

# temps = np.array([25, 32, 28, 35, 30, 40, 42])

# Tasks:

# Print temps above average temperature.

# Replace all temps > 40 with 40 (limit the max temperature).

import numpy as np

temps = np.array([25, 32, 28, 35, 30, 40, 42])

average = np.mean(temps)

print(f"Average temprature: {average:.2f}")

print("Temps above average:",temps[temps > average])

temps[temps > 40] = 40
print("Limited tempratures:",temps)
