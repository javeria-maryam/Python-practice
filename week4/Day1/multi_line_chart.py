# plot marks of 2 years 2024 and 2025
# add title, legend, labels and marker

import matplotlib.pyplot as plt

students = ["Ali","Maryam","Bilal","Sara"]
marks_2024 = [89,60,79,88]
marks_2025 = [90,65,85,90]

plt.plot(students,marks_2024,label='2024',marker = 'o')
plt.plot(students,marks_2025,label='2025',marker = 's')
plt.title("Marks comparison")
plt.xlabel('students')
plt.ylabel('Marks')
plt.legend()
plt.grid(True)
plt.show()

