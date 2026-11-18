'''
1. Instance Variables 2. Class Variables

Methods in Python OOP:
1. Instance Methods
2. Class Methods
3. Static Methods
'''


# Example 1 : Instance Variables
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Aarya", 18)
student2 = Student("Rahul", 19)

print(student1.name, "-", student1.age)
print(student2.name, "-", student2.age)

print()



# Example 2 : Class Variables
class Student:

    college = "Pillai University"

    def __init__(self, name):
        self.name = name


student1 = Student("Aarya")
student2 = Student("Rahul")

print(student1.name, "-", Student.college)
print(student2.name, "-", Student.college)

print()


# Example 3 : Instance Method
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)


student1 = Student("Aarya")

student1.display()

print()



# Example 4 : Class Method
class Student:

    college = "Pillai University"

    @classmethod
    def show_college(cls):
        print("College:", cls.college)


Student.show_college()

print()



# Example 5 : Static Method
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


result = Calculator.add(10, 20)

print("Addition:", result)

print()



# Example 6 : Variables and Methods Together
class Employee:

    company = "ABC Technologies"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name    :", self.name)
        print("Salary  :", self.salary)

    @classmethod
    def company_name(cls):
        print("Company :", cls.company)

    @staticmethod
    def greet():
        print("Welcome to the Company!")

employee1 = Employee("Aarya", 50000)

employee1.display()

Employee.company_name()

Employee.greet()

print()


#End of Program
✔ Instance Variables belong to an object.
✔ Class Variables belong to the class.
✔ Instance Methods work with object data.
✔ Class Methods work with class variables.
✔ Static Methods do not use object or class data.
