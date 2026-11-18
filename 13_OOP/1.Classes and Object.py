'''
A class is a blueprint (template) used to create objects. It defines the attributes (data) and methods (functions) that an object will have.
An object is an instance of a class. One class can create multiple objects.

Syntax:
class ClassName:
    pass

object_name = ClassName()
'''


# Example 1 : Creating a Simple Class
class Student:
    pass

student1 = Student()
print()


# Example 2 : Class with Attributes
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


# Example 3 : Class with Method
class Student:

    def __init__(self):
        self.name = "Rahul"

    def display(self):
        print("Student Name:", self.name)


student1 = Student()

student1.display()
print()



# Example 4 : Creating Multiple Objects
class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("-" * 20)


car1 = Car("Toyota", "Fortuner")
car2 = Car("Honda", "City")
car3 = Car("Hyundai", "Creta")

car1.display()
car2.display()
car3.display()

print()



# Example 5 : Different Objects of Same Class
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduction(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


student1 = Student("Aarya", 18)
student2 = Student("Rahul", 19)
student3 = Student("Priya", 18)

student1.introduction()
student2.introduction()
student3.introduction()

print()

#End of Program
