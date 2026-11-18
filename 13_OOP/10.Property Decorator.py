'''
@property is a built-in decorator in Python that allows a method to be accessed like an attribute.
It provides a clean and Pythonic way to implement getters, setters, and deleters.

Decorators Used:
@property
@property_name.setter
@property_name.deleter
'''


# Example 1 : Getter using @property
class Student:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name


student = Student("Aarya")
print(student.name)
print()


# Example 2 : Setter using @property
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
        else:
            print("Salary must be positive.")


employee = Employee(50000)
print("Old Salary:", employee.salary)
employee.salary = 60000
print("New Salary:", employee.salary)
print()



# Example 3 : Deleter using @property
class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        print("Name Deleted")
        del self._name


student = Student("Rahul")
print(student.name)
del student.name
print()


# Example 4 : Complete Example
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Balance cannot be negative.")

    def display(self):
        print("Balance:", self.balance)


account = BankAccount(10000)
account.display()
account.balance = 15000
account.display()
account.balance = -500
print()



# Example 5 : Read-Only Property
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius * self.radius


circle = Circle(5)

print("Radius:", circle.radius)
print("Area:", circle.area)
print()

#End of Program
✔ @property creates a getter.
✔ @property_name.setter creates a setter.
✔ @property_name.deleter creates a deleter.
✔ Properties allow methods to be accessed like attributes.
✔ They make code cleaner and more Pythonic.
