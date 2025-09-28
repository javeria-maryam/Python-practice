# Employees with Overriding 👩‍💼👨‍💼
# Create a parent class Employee with:
# Attributes: name, salary.
# Method get_details().
# Create child class Manager:
# Extra attribute: department.
# Override get_details() to include department.
# Create objects and print details


class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: {self.salary}"
    
class Manager(Employee):
    def __init__(self,name,salary,department):
      super().__init__(name,salary)
      self.department = department

    def get_details(self):
       return f"Employee: {self.name}, Salary: {self.salary}, Department: {self.department}"
    
employee = Employee("Ali",40000)
m1 = Manager("Umar",80000,"HR")
m2 = Manager("Alisha",50000,"Tech")

print(employee.get_details())
print(m1.get_details())
print(m2.get_details())