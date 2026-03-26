# classes in python are blueprint of an object
# objects are real world instances of these calsses
# example car is class and any car company's actual car model is its object

# defining a class named Student
class Student:
    no_of_students = 0
    # creating constructor using __init__() 
    def __init__(self, name, age, marks): # self is the object for which constructor is called is passed as first parameter
        self.name = name
        self.age = age
        self.marks = marks
        Student.no_of_students += 1
    
    def display_info(self):
        print(f"{self.name} is {self.age} years old and has marks {self.marks}")

s1 = Student("Keshav", 11, 100) # Student() calls the constructor
s1.display_info()
print(Student.no_of_students)

s2 = Student("shivansh", 20, 96)
s2.display_info()
print(Student.no_of_students)

s2.name = "Shivansh" # updating properties
s2.display_info()

# an object has properties(variables) and behaviours(methods)
# function associated with classes are called methods
# name, age and marks are fields associated with objects
# we can create properties associated with classes only like number of students
# class properties can be called with class name or instance
