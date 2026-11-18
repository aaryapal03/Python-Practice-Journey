'''
Special methods are predefined methods in Python that start and end with double underscores (__).
They are also called:
✔ Magic Methods
✔ Dunder Methods

Some Common Special Methods:
__init__()
__str__()
__repr__()
__len__()
__add__()
'''


# Example 1 : __init__()
class Student:

    def __init__(self, name):
        self.name = name


student = Student("Aarya")

print(student.name)

print()



# Example 2 : __str__()
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student Name: {self.name}"


student = Student("Rahul")

print(student)

print()


# Example 3 : __repr__()
class Student:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student('{self.name}')"


student = Student("Priya")

print(repr(student))

print()



# Example 4 : __len__()
class Book:

    def __init__(self, title):
        self.title = title

    def __len__(self):
        return len(self.title)


book = Book("Python")

print("Length:", len(book))

print()



# Example 5 : __add__()
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


num1 = Number(10)
num2 = Number(20)

print("Addition:", num1 + num2)

print()



# Example 6 : Complete Example
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ₹{self.price}"

    def __len__(self):
        return len(self.name)


product = Product("Laptop", 50000)

print(product)
print("Name Length:", len(product))

print()

#End of Program
✔ Special methods are predefined methods.
✔ __init__() initializes an object.
✔ __str__() returns a user-friendly string.
✔ __repr__() returns an official object representation.
✔ __len__() defines the behavior of len().
✔ __add__() defines the behavior of + operator.
