
# Program 1: Create and Print a Set
fruits = {"Apple", "Banana", "Mango", "Orange"}
print(fruits)

print()

# Program 2: Add and Update Elements
numbers = {10, 20, 30}

numbers.add(40)
numbers.update([50, 60])
print(numbers)

print()

# Program 3: Remove Elements
numbers = {10, 20, 30, 40, 50}

numbers.remove(20)
numbers.discard(100)
print(numbers)

print()

# Program 4: Set Methods
numbers = {10, 20, 30, 40}

copied_set = numbers.copy()


print("Original Set :", numbers)
print("Copied Set :", copied_set)
numbers.clear()

print("After clear() :", numbers)

print()

# Program 5: Built-in Functions

values = {15, 25, 35, 45, 55}

print("Length :", len(values))
print("Maximum :", max(values))
print("Minimum :", min(values))
print("Sum :", sum(values))
print("Sorted :", sorted(values))

print()

# Program 6: Set Operations

A = {10, 20, 30, 40}
B = {30, 40, 50, 60}

print("Union :", A | B)
print("Intersection :", A & B)
print("Difference :", A - B)
print("Symmetric Difference :", A ^ B)

print()

# Program 7: Subset, Superset and Disjoint

A = {10, 20}
B = {10, 20, 30, 40}
C = {50, 60}

print("Subset :", A.issubset(B))
print("Superset :", B.issuperset(A))
print("Disjoint :", A.isdisjoint(C))

print()

# Program 8: Membership Operators

subjects = {"Python", "SQL", "DBMS"}

print("Python" in subjects)
print("Java" not in subjects)

print()


# Program 10: Mixed Set Program

numbers = {5, 10, 15, 20, 25}

numbers.add(30)

print("Program 10")
print("Updated Set :", numbers)
print("Length :", len(numbers))
print("Maximum :", max(numbers))
print("Minimum :", min(numbers))
print("Sum :", sum(numbers))
print("Sorted :", sorted(numbers))

print()

#End of Program
