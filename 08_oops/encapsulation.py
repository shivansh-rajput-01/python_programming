# it is another pillar of oops
# it is the process of wrapping properties and behaviour of real world entity together

class Employee:
    def __init__(self, name, dept, sal):
        self.name = name
        self.dept = dept
        self.sal = sal
    
    def __str__(self): # this is python Dunder method that tells what to print when object is written in print
        return f"Name: {self.name}\nDepartment: {self.dept}\nSalary: {self.sal}"
    

e1 = Employee("Rakesh", "CSE", 100000)

print(e1)
