#INDEXING OF A LIST:-
# Creating a List
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print("Original List:")
print(fruits)

print()


# Positive Indexing
print("Positive Indexing")
print("Index 0 :", fruits[0])
print("Index 1 :", fruits[1])
print("Index 2 :", fruits[2])
print("Index 3 :", fruits[3])
print("Index 4 :", fruits[4])

print()


# Negative Indexing
print("Negative Indexing")
print("Index -1 :", fruits[-1])
print("Index -2 :", fruits[-2])
print("Index -3 :", fruits[-3])
print("Index -4 :", fruits[-4])
print("Index -5 :", fruits[-5])

print()


# Accessing First and Last Element
print("First Element :", fruits[0])
print("Last Element  :", fruits[-1])

print()


# Accessing Middle Element
print("Middle Element :", fruits[2])

#SLICING OF A LIST:- 
# List Slicing
numbers = [10, 20, 30, 40, 50, 60]

print("Original List:")
print(numbers)

print("Slicing Examples:")

print("First Three Elements      :", numbers[:3])
print("Last Three Elements       :", numbers[-3:])
print("Elements from Index 2 to 4:", numbers[2:5])
print("Elements from Index 1 to End:", numbers[1:])
print("Elements from Start to Index 4:", numbers[:5])
print("Every Second Element      :", numbers[::2])
print("Reverse List              :", numbers[::-1])

# End of Program
