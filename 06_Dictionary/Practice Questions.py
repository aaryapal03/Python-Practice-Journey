
# Program 1: Create and Access a Dictionary

student = {"name": "Aarya", "age": 19, "course": "Data Science"}

print(student)
print("Name :", student["name"])

print()

# Program 2: Add and Update Elements

student["city"] = "Mumbai"
student["age"] = 20
print(student)

print()

# Program 3: Dictionary Methods
employee = {"id": 101, "name": "Rahul", "salary": 50000}

print("Keys :", employee.keys())
print("Values :", employee.values())
print("Items :", employee.items())

print()

# Program 4: Remove Elements
employee.pop("salary")
print(employee)

print()

# Program 5: Built-in Functions

marks = {"Python": 95,"SQL": 90,"DBMS": 88}

print("Program 5")
print("Length :", len(marks))
print("Minimum Key :", min(marks))
print("Maximum Key :", max(marks))
print("Sorted Keys :", sorted(marks))

print()

# Program 6: Dictionary Operations

print("Python" in marks)
print("Java" not in marks)

print()


# Program 10: Mixed Dictionary Program

product = {"name": "Laptop", "price": 50000,"brand": "Dell"}

product["color"] = "Black"

print("Program 10")
print(product)
print("Keys :", product.keys())
print("Values :", product.values())
print("Length :", len(product))

print()

#End of Program
