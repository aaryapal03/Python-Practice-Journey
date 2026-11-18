
# Create a Student class with name and age.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name :", self.name)
        print("Age  :", self.age)


student = Student("Aarya", 18)
student.display()


# Create a Rectangle class and calculate area.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area:", self.length * self.width)


rectangle = Rectangle(10, 5)
rectangle.area()


# Demonstrate Single Inheritance.
class Animal:
    def sound(self):
        print("Animals make sounds.")


class Dog(Animal):
    def bark(self):
        print("Dog barks.")


dog = Dog()

dog.sound()
dog.bark()


# Demonstrate Method Overriding.
class Bird:
    def fly(self):
        print("Bird is flying.")


class Eagle(Bird):
    def fly(self):
        print("Eagle flies very high.")


eagle = Eagle()
eagle.fly()


# Demonstrate Encapsulation.
class BankAccount:
    def __init__(self):
        self.__balance = 10000

    def get_balance(self):
        return self.__balance


account = BankAccount()
print("Balance:", account.get_balance())


# Demonstrate Abstraction.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Area:", self.side * self.side)


square = Square(4)
square.area()


# Demonstrate Composition.
class Engine:
    def start(self):
        print("Engine Started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is Moving")


car = Car()
car.drive()


# Create a Property using @property.
class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self._salary = value


employee = Employee(40000)
print("Salary:", employee.salary)
employee.salary = 50000
print("Updated Salary:", employee.salary)



# Create a Static Method.
class Calculator:
    @staticmethod
    def multiply(a, b):
        return a * b


print("Multiplication:", Calculator.multiply(10, 5))


# Create a Class Method.
class College:

    college_name = "Pillai University"

    @classmethod
    def show_college(cls):
        print("College:", cls.college_name)


College.show_college()


# Create a Special Method (__str__).
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title


book = Book("Python Programming")
print(book)


# Create multiple objects of the same class.
class Mobile:

    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)


mobile1 = Mobile("Samsung")
mobile2 = Mobile("Apple")
mobile3 = Mobile("OnePlus")

mobile1.display()
mobile2.display()
mobile3.display()

#End of Program
