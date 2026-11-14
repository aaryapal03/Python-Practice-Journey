
# Creating a Nested List
students = [ ["Aarya", 19, "Data Science"], ["Rahul", 20, "Computer Science"], ["Priya", 18, "Artificial Intelligence"] ]
print("Nested List:")
print(students)

print()


# Accessing Complete Inner Lists
print("First Student :", students[0])
print("Second Student:", students[1])
print("Third Student :", students[2])

print()


# Accessing Individual Elements
print("First Student Name   :", students[0][0])
print("First Student Age    :", students[0][1])
print("First Student Course :", students[0][2])

print()

print("Second Student Name   :", students[1][0])
print("Second Student Age    :", students[1][1])
print("Second Student Course :", students[1][2])

print()


# Updating an Element
students[2][1] = 19
print("Updated Third Student Details:")
print(students[2])

print()


# Iterating Through a Nested List
print("Student Details:")

for student in students:
    print(student)

print()


# Iterating Through Each Element
print("Student Information:")

for student in students:
    print("Name   :", student[0])
    print("Age    :", student[1])
    print("Course :", student[2])
    print()


# End of Program
