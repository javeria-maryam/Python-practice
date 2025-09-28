# Shapes with Overriding 🎨

# Create a parent class Shape with a method area() that just prints "Area formula not defined".
# Create child classes:
# Circle → override area() to calculate πr².
# Rectangle → override area() to calculate length × width.
# Create objects and call area() for each.

import math

class Shape:
    def area(self):
        print("Area formula not defined")
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)
    
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

       
shape = Shape()        
c1 = Circle(5)
r1 = Rectangle(4,6)

shape.area()  
print(f"Area of circle is {c1.area():.2f}")        #area upto 2 decimal
print(f"Area of rectangle is {r1.area()}")






















        