'''
A constructor is a special method that is automatically called when an object is created.
In Python, the constructor is written using the __init__() method.

Purpose of Constructor:
✔ Initialize object data (attributes)
✔ Assign values to object variables
✔ Automatically executes when an object is created

Syntax:
class ClassName:

    def __init__(self):
        # Initialization code
'''


# Example 1 : Default Constructor
class Student:

    def __init__(self):
        print("Constructor is called automatically.")


student1 = Student()

print()



# Example 2 : Constructor with Attributes
class Student:

    def __init__(self):
        self.name = "Aarya"
        self.age = 18
        self.course = "BCA Data Science"


student1 = Student()

print("Name   :", student1.name)
print("Age    :", student1.age)
print("Course :", student1.course)

print()



# Example 3 : Parameterized Constructor
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Aarya", 18)
student2 = Student("Rahul", 19)

print(student1.name, "-", student1.age)
print(student2.name, "-", student2.age)

print()



# Example 4 : Constructor with Default Values
class Employee:

    def __init__(self, name="Unknown", salary=0):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name   :", self.name)
        print("Salary :", self.salary)
        print("-" * 20)


employee1 = Employee("Amit", 50000)
employee2 = Employee()

employee1.display()
employee2.display()

print()



# Example 5 : Constructor with Method
class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand :", self.brand)
        print("Model :", self.model)


car1 = Car("Toyota", "Fortuner")
car1.display()

print()


#End of Program
✔ __init__() is the constructor in Python.
✔ It is called automatically when an object is created.
✔ Constructors initialize object attributes.
✔ Constructors can have parameters.
✔ Constructors can also have default values.
