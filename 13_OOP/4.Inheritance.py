'''
Inheritance is the process by which one class (child class) acquires the properties and methods of another class (parent class).

Benefits of Inheritance:
✔ Code Reusability
✔ Easy Maintenance
✔ Reduces Code Duplication

Syntax:
class Parent:
    pass
class Child(Parent):
    pass
'''


# Example 1 : Single Inheritance
class Animal:

    def sound(self):
        print("Animals make different sounds.")


class Dog(Animal):

    def bark(self):
        print("Dog barks.")


dog = Dog()

dog.sound()
dog.bark()

print()



# Example 2 : Multilevel Inheritance
class Grandparent:

    def grandparent_property(self):
        print("Grandparent's Property")


class Parent(Grandparent):

    def parent_property(self):
        print("Parent's Property")


class Child(Parent):

    def child_property(self):
        print("Child's Property")


child = Child()

child.grandparent_property()
child.parent_property()
child.child_property()

print()



# Example 3 : Multiple Inheritance
class Father:

    def skills(self):
        print("Father: Driving")


class Mother:

    def hobby(self):
        print("Mother: Cooking")


class Son(Father, Mother):

    def own_skill(self):
        print("Son: Coding")


son = Son()

son.skills()
son.hobby()
son.own_skill()

print()



# Example 4 : Hierarchical Inheritance
class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):

    def car_type(self):
        print("This is a Car")


class Bike(Vehicle):

    def bike_type(self):
        print("This is a Bike")


car = Car()
bike = Bike()

car.start()
car.car_type()

print()

bike.start()
bike.bike_type()

print()



# Example 5 : Hybrid Inheritance
class A:

    def display_a(self):
        print("Class A")


class B(A):

    def display_b(self):
        print("Class B")


class C(A):

    def display_c(self):
        print("Class C")


class D(B, C):

    def display_d(self):
        print("Class D")


obj = D()

obj.display_a()
obj.display_b()
obj.display_c()
obj.display_d()

print()


✔ Inheritance allows one class to inherit another class.
✔ Parent class is also called Base Class.
✔ Child class is also called Derived Class.

Types of Inheritance:
1. Single Inheritance
2. Multilevel Inheritance
3. Multiple Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance

Main Benefit:
Code Reusability
