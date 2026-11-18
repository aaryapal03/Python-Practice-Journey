'''
The word "Polymorphism" means "Many Forms".
In Python, polymorphism allows the same method function, or operator to perform different tasks depending on the object or data type.

Types of Polymorphism:
1. Method Overriding
2. Duck Typing
3. Built-in Polymorphism
4. Operator Polymorphism
'''


# Example 1 : Method Overriding
class Animal:

    def sound(self):
        print("Animals make different sounds.")

class Dog(Animal):

    def sound(self):
        print("Dog barks.")

class Cat(Animal):

    def sound(self):
        print("Cat meows.")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

print()



# Example 2 : Duck Typing
class Bird:

    def speak(self):
        print("Bird is chirping.")

class Person:

    def speak(self):
        print("Person is speaking.")


def display_sound(obj):
    obj.speak()


bird = Bird()
person = Person()

display_sound(bird)
display_sound(person)

print()



# Example 3 : Built-in Polymorphism
print("Length of String :", len("Python"))
print("Length of List   :", len([10, 20, 30, 40]))
print("Length of Tuple  :", len((1, 2, 3)))

print()



# Example 4 : Operator Polymorphism
print("10 + 20 =", 10 + 20)

print("'Hello' + ' Python' =", "Hello" + " Python")
print([1, 2] + [3, 4])

print()



# Example 5 : Same Function, Different Objects
class Car:

    def move(self):
        print("Car is moving on the road.")

class Airplane:

    def move(self):
        print("Airplane is flying in the sky.")

def start(vehicle):
    vehicle.move()


car = Car()
plane = Airplane()

start(car)
start(plane)

print()


#End of Program
✔ Polymorphism means one interface, many forms.
✔ Method Overriding changes the parent's method.
✔ Duck Typing depends on the object's behavior.
✔ Built-in functions like len() are polymorphic.
✔ Operators like + behave differently for different data types.
