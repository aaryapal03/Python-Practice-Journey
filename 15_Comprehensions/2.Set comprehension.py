
# Example 1 : Create a Set of Squares
numbers = [1, 2, 3, 4, 5]

squares = {num ** 2 for num in numbers}
print("Original List :", numbers)
print("Square Set    :", squares)

print()


# Example 2 : Remove Duplicate Values
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 6]

unique_numbers = {num for num in numbers}
print("Original List :", numbers)
print("Unique Set    :", unique_numbers)

print()



# Example 3 : Even Numbers
numbers = range(1, 11)

even_numbers = {num for num in numbers if num % 2 == 0}
print("Even Numbers :", even_numbers)

print()



# Example 4 : Convert to Uppercase
fruits = ["apple", "banana", "apple", "mango"]

uppercase = {fruit.upper() for fruit in fruits}
print("Original List :", fruits)
print("Uppercase Set :", uppercase)

print()

#End of Program
