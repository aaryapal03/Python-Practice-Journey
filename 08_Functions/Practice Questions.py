
# Program 1: Find the square of every number using map()
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, numbers))
print(result)

print()

# Program 2: Convert all names to uppercase using map()
names = ["aarya", "rahul", "priya"]
result = list(map(lambda x: x.upper(), names))
print(result)

print()

# Program 3: Add 10 to every number using map()
numbers = [5, 10, 15, 20]
result = list(map(lambda x: x + 10, numbers))
print(result)
print()

# Program 4: Display even numbers using filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

print()

# Program 5: Display odd numbers using filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(filter(lambda x: x % 2 != 0, numbers))
print(result)

print()

# Program 6: Display numbers greater than 50 using filter()
numbers = [25, 60, 40, 90, 15, 75]
result = list(filter(lambda x: x > 50, numbers))
print(result)

print()

# Program 7: Find the sum of all numbers using reduce()
from functools import reduce
numbers = [10, 20, 30, 40]
result = reduce(lambda x, y: x + y, numbers)
print(result)

print()

# Program 8: Find the product of all numbers using reduce()
from functools import reduce
numbers = [2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)
print(result)

print()

# Program 9: Find the largest number using reduce()
from functools import reduce
numbers = [12, 45, 78, 23, 90]
result = reduce(lambda x, y: x if x > y else y, numbers)
print(result)

print()

# Program 10: Find the smallest number using reduce()
from functools import reduce
numbers = [12, 45, 78, 23, 90]
result = reduce(lambda x, y: x if x < y else y, numbers)
print(result)

print()


# Program 11: Create a function to print your name.

def my_name():
    print("My name is Aarya.")
  
my_name()


# Program 12: Create a function to add two numbers.

def add(a, b):
    return a + b

print("Sum =", add(10, 20))


# Program 13: Create a function with default arguments.

def greet(name="Guest"):
    print("Hello,", name)

greet()
greet("Aarya")


# Program 14: Create a function using *args to find the sum.

def total(*numbers):
    print("Sum =", sum(numbers))

total(10, 20, 30, 40, 50)


# Program 15: Create a function using **kwargs to display student details.

def student(**details):
    for key, value in details.items():
        print(key, ":", value)

student(name="Aarya", age=19, course="BCA Data Science")


# Program 16: Find the factorial of a number using recursion.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Program 6")
print("Factorial =", factorial(5))

print()

# Program 17: Use a lambda function to find the square of a number.
square = lambda x: x ** 2
print(square(6))


# Program 18: Use map() to find the square of every number.
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, numbers))
print(result)


# Program 19: Use filter() to display even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

print()

# Program 20: Use reduce() to find the sum of all numbers.
from functools import reduce
numbers = [10, 20, 30, 40]
result = reduce(lambda x, y: x + y, numbers)
print(result)

#End of Program
