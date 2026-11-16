
# Basic Lambda Function
square = lambda x: x * x
print("Square of 5 =", square(5))


# Lambda Function with Two Arguments

add = lambda a, b: a + b
print("Addition =", add(10, 20))


# Lambda Function with Three Arguments

multiply = lambda a, b, c: a * b * c
print("Multiplication =", multiply(2, 3, 4))


# Lambda Function with Conditional Expression
largest = lambda a, b: a if a > b else b
print("Largest Number =", largest(25, 40))


# Using Lambda with sorted()

students = [("Rahul", 85), ("Priya", 92), ("Aarya", 88)]

sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)

#End of Program
