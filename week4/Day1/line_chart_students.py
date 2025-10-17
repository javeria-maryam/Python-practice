# Plot marks of 5 students

# Add title, labels, grid

# Save the chart as an image

import matplotlib.pyplot as plt

marks = [67,87,59,80,78]
students = ["Ali","Maryam","Bilal","Yousaf","Hina"]

plt.plot(students,marks,color = 'green',marker = 's')
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)
plt.show()


plt.savefig("StudentMarks.png")
print("Saved successfully")