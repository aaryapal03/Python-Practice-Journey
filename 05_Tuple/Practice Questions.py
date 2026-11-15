
# Program 1: Create and Print a Tuple

fruits = ("Apple", "Banana", "Mango", "Orange")
print(fruits)

print()

# Program 2: Access Tuple Elements

numbers = (10, 20, 30, 40, 50)

print("First Element :", numbers[0])
print("Last Element :", numbers[-1])

print()

# Program 3: Tuple Slicing

colors = ("Red", "Blue", "Green", "Yellow", "Black")

print("First Three :", colors[:3])
print("Last Two :", colors[-2:])
print("Reverse :", colors[::-1])

print()

# Program 4: Tuple Methods

marks = (80, 90, 70, 90, 60)

print("Count of 90 :", marks.count(90))
print("Index of 70 :", marks.index(70))

print()

# Program 5: Built-in Functions

values = (15, 25, 35, 45, 55)

print("Length :", len(values))
print("Maximum :", max(values))
print("Minimum :", min(values))
print("Sum :", sum(values))

print()

# Program 6: Tuple Operations

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print("Concatenation :", tuple1 + tuple2)
print("Repetition :", tuple1 * 2)

print()

# Program 7: Membership Operators

subjects = ("Python", "Java", "SQL")

print("Python" in subjects)
print("C++" not in subjects)

print()

# Program 8: Tuple Packing and Unpacking

student = ("Aarya", 19, "Data Science")

name, age, course = student

print("Program 8")
print("Name :", name)
print("Age :", age)
print("Course :", course)

print()

# Program 9: Using * Operator

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("Program 9")
print("First :", first)
print("Middle :", middle)
print("Last :", last)

print()

# Program 10: Mixed Tuple Program

numbers = (25, 10, 40, 15, 30)

print("Program 10")
print("Original Tuple :", numbers)
print("Length :", len(numbers))
print("Maximum :", max(numbers))
print("Minimum :", min(numbers))
print("Sum :", sum(numbers))
print("Sorted :", sorted(numbers))
print("First Element :", numbers[0])
print("Last Element :", numbers[-1])

print()

#End of Program
