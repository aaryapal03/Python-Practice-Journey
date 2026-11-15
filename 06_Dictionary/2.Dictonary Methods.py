
# Original Dictionary

student = {"name": "Aarya", "age": 19, "course": "Data Science"}
print(student)

print()

# update()
student.update({"city": "Mumbai"})

print("update()")
print(student)

print()

# get()

print("get()")
print(student.get("course"))

print()

# keys()

print("keys()")
print(student.keys())

print()

# values()

print("values()")
print(student.values())

print()

# items()

print("items()")
print(student.items())

print()

# pop()

student.pop("age")

print("pop()")
print(student)

print()

# popitem()

student.popitem()

print("popitem()")
print(student)

print()

# setdefault()

student.setdefault("country", "India")

print("setdefault()")
print(student)

print()

# copy()

new_student = student.copy()

print("copy()")
print(new_student)

print()

# clear()

sample = {"A": 1, "B": 2}

sample.clear()

print("clear()")
print(sample)

print()

#del()
sample = {"A": 1, "B": 2}

del sample
print(sample)

print()

# fromkeys()

keys = ("name", "age", "course")

new_dict = dict.fromkeys(keys, "Not Available")

print("fromkeys()")
print(new_dict)

print()

# Built-in Functions

marks = {"Math": 95, "Python": 90, "DBMS": 88}

print("Built-in Functions")

print("Length :", len(marks))
print("Minimum Key :", min(marks))
print("Maximum Key :", max(marks))
print("Sorted Keys :", sorted(marks))

print()

# Dictionary Operations

print("Dictionary Operations")

print("Name Exists :", "name" in student)
print("Salary Exists :", "salary" not in student)

print()

# Accessing Values

print("Accessing Values")

print(student["name"])
print(student.get("country"))

print()

#End of Program
