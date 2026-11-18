'''
Composition is an OOP concept where one class contains an object of another class.
It represents a HAS-A relationship.
'''


# Example 1 : Car HAS AN Engine
class Engine:
    def start(self):
        print("Engine Started.")

class Car:
    def __init__(self):
        self.engine = Engine()   # Composition

    def drive(self):
        print("Car is Ready to Drive.")
        self.engine.start()


car = Car()

car.drive()
print()


# Example 2 : Student HAS AN Address
class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state

    def display(self):
        print("City :", self.city)
        print("State:", self.state)


class Student:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display(self):
        print("Name :", self.name)
        self.address.display()


address = Address("Mumbai", "Maharashtra")

student = Student("Aarya", address)

student.display()
print()



# Example 3 : Computer HAS A CPU
class CPU:
    def process(self):
        print("CPU is Processing Data.")

class Computer:
    def __init__(self):
        self.cpu = CPU()

    def start(self):
        print("Computer Started.")
        self.cpu.process()


computer = Computer()
computer.start()
print()



# Example 4 : Library HAS Books
class Book:
   def __init__(self, title):
        self.title = title

    def display(self):
        print("Book :", self.title)


class Library:
    def __init__(self):
        self.book1 = Book("Python Programming")
        self.book2 = Book("Data Science Basics")

    def show_books(self):
        self.book1.display()
        self.book2.display()


library = Library()
library.show_books()
print()



# Example 5 : Mobile HAS Battery
class Battery:
    def charge(self):
        print("Battery is Charging.")


class Mobile:
    def __init__(self):
        self.battery = Battery()

    def power_on(self):
        print("Mobile is Powering On.")
        self.battery.charge()


mobile = Mobile()
mobile.power_on()
print()


✔ Composition represents a HAS-A relationship.
✔ One class contains an object of another class.
✔ Composition improves code reusability.
✔ It helps create flexible and maintainable programs.
✔ Real-life examples include:
   - Car HAS AN Engine
   - Student HAS AN Address
   - Computer HAS A CPU
