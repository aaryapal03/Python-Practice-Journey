
# Example 1 : Create a List of Squares
numbers = [1, 2, 3, 4, 5]

squares = [num ** 2 for num in numbers]
print("Original List :", numbers)
print("Squared List  :", squares)


# Example 2 : Even Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [num for num in numbers if num % 2 == 0]
print("Original List :", numbers)
print("Even Numbers  :", even_numbers)

print()


# Example 3 : Convert to Uppercase
fruits = ["apple", "banana", "mango", "grapes"]

uppercase = [fruit.upper() for fruit in fruits]
print("Original List :", fruits)
print("Uppercase List:", uppercase)

print()



# Example 4 : Numbers Greater Than 50
marks = [35, 80, 45, 92, 60, 28]

passed = [mark for mark in marks if mark >= 50]
print("Marks       :", marks)
print("Passed Marks:", passed)

print()


#End of Program
