# Create a class Student.
# Attributes: name, marks (list).
# Method: average() → returns average of marks.
# Method: grade() →
# If avg ≥ 80 → "A"
# If avg ≥ 60 → "B"
# Else → "C"
# Create at least 2 student objects and print their details.


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks)/len(self.marks)
    
    def grade(self):
        avg = self.average()
        if avg >= 80 :
            return "A"
        elif avg >= 60:
            return "B"
        else:
            return "C"
        
Student1 = Student("Ali",[50,40,60,80])
Student2 = Student("Emily",[40,80,60,70])

print("My name is",Student1.name,",my grade is",Student1.grade())
print("My name is",Student2.name,",my grade is",Student2.grade())

