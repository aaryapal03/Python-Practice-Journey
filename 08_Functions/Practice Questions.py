
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

#End of Program
