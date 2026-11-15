
# Tuple Packing
student = ("Aarya", 19, "Data Science")
print(student)

print()

# Tuple Unpacking
name, age, course = student

print("Name   :", name)
print("Age    :", age)
print("Course :", course)

print()

# Packing Different Data Types
details = ("Rahul", 20, 89.5, True)
print(details)

print()

# Unpacking Another Tuple

student_name, student_age, marks, passed = details

print("Name   :", student_name)
print("Age    :", student_age)
print("Marks  :", marks)
print("Passed :", passed)

print()

# Using * Operator
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("Using * Operator:")
print("First  :", first)
print("Middle :", middle)
print("Last   :", last)

print()

# Ignoring Values During Unpacking

colors = ("Red", "Green", "Blue")

first_color, _, third_color = colors

print("Ignoring Values:")
print("First Color :", first_color)
print("Third Color :", third_color)

print()

# Swapping Two Variables

a = 10
b = 20

print("Before Swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print()

print("After Swapping:")
print("a =", a)
print("b =", b)

print()

#End of program
