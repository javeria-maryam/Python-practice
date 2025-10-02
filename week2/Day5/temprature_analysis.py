# You have daily temperatures (°C) recorded for a week:

# temps = np.array([28, 30, 27, 26, 29, 31, 32])


# 👉 Your tasks:

# Find the average temperature of the week.

# Find the hottest day (maximum temperature).

# Find the coldest day (minimum temperature).

# Print only the days where temperature was above 29°C.

import numpy as np

temps = np.array([28, 30, 27, 26, 29, 31, 32])

print("Average temprature of the week is:",np.mean(temps))
print("Hottest dat temprature is:",np.max(temps))
print("Coldest day temprature is:",np.min(temps))
print("Days above 29°C:",temps[temps > 29])