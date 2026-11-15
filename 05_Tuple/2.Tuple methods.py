
# Original Tuple
numbers = (10, 20, 30, 20, 40, 50)
print(numbers)

print()


# count()
print("count()")
print(numbers.count(20))

print()

# index()

print("index()")
print(numbers.index(30))

print()

# Built-in Functions
print("Built-in Functions")

print("Length  :", len(numbers))
print("Minimum :", min(numbers))
print("Maximum :", max(numbers))
print("Sum     :", sum(numbers))
print("Sorted  :", sorted(numbers))

print()

# Tuple Concatenation (+)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print("Concatenation")
print(tuple1 + tuple2)

print()

# Tuple Repetition (*)
print("Repetition")
print(tuple1 * 3)

print()

# Membership Operators
print("Membership Operators")

print(20 in numbers)
print(100 not in numbers)

print()

# Accessing Elements
print("First Element :", numbers[0])
print("Last Element  :", numbers[-1])

print()

# Slicing
print("First Three Elements :", numbers[:3])
print("Last Three Elements  :", numbers[-3:])
print("Reverse Tuple        :", numbers[::-1])

print()

#End of Program
