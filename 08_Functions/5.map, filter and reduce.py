
# Original List
numbers = [1, 2, 3, 4, 5]
print(numbers)

print()

# map()
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)

print()

# filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

print()

# reduce()
from functools import reduce
total = reduce(lambda x, y: x + y, numbers)
print("Sum of Numbers:", total)

print()

# Another Example of map()
names = ["aarya", "rahul", "priya"]
capital_names = list(map(lambda name: name.capitalize(), names))
print(capital_names)

print()

# Another Example of filter()
marks = [35, 80, 25, 90, 65, 40]
passed_students = list(filter(lambda mark: mark >= 40, marks))
print(passed_students)

print()

# Another Example of reduce()
from functools import reduce
numbers = [2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

print()

#End of Program
