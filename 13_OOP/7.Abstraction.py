'''
Abstraction is the process of hiding the implementation details and showing only the essential features to the user.
In Python, abstraction is achieved using:
1. ABC (Abstract Base Class)
2. @abstractmethod decorator
'''

# Example 1 : Simple Abstract Class
class Animal(ABC):

    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Dog barks.")


dog = Dog()
dog.sound()

print()



# Example 2 : Multiple Child Classes
class Shape(ABC):
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Area of Square:", self.side * self.side)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of Rectangle:", self.length * self.width)


square = Square(4)
rectangle = Rectangle(6, 3)

square.area()
rectangle.area()

print()



# Example 3 : Vehicle Example
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car starts using a key.")


class Bike(Vehicle):

    def start(self):
        print("Bike starts using a self-start button.")


car = Car()
bike = Bike()

car.start()
bike.start()

print()


# Example 4 : Employee Example
class Employee(ABC):

    @abstractmethod
    def work(self):
        pass


class Developer(Employee):

    def work(self):
        print("Developer writes code.")


class Designer(Employee):

    def work(self):
        print("Designer creates UI designs.")


developer = Developer()
designer = Designer()

developer.work()
designer.work()

print()



# Example 5 : What Happens if Method
# is Not Implemented?

class Animal(ABC):
    def sound(self):
        pass

class Cat(Animal):
    pass


print("Cannot create an object of Cat because")
print("the abstract method 'sound()' is not implemented.")

# Cat()  # Uncommenting this line will raise an error.

print()


#End of Program
✔ Abstraction hides implementation details.
✔ Abstract classes are created using ABC.
✔ Abstract methods use @abstractmethod.
✔ Child classes must implement all abstract methods.
✔ Abstract classes cannot be instantiated directly.
