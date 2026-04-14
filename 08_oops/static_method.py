# we have different decorators in python
# @staticmethod decorator makes a method static i.e. that does not get self as parameter and can be called with class
# like for a system Student class will have same college

class Student:
    def __init__(self, name, marks, age):
        self.name = name
        self.marks = marks
        self.age = age

    @staticmethod
    def college_name():
        print("IIT")

s = Student("st1", 91, 21)
s.college_name()
