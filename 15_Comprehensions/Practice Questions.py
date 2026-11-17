
# Create a list of squares from 1 to 10.
squares = [num ** 2 for num in range(1, 11)]
print("Squares:", squares)



# Create a list of even numbers from 1 to 20.
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print("Even Numbers:", even_numbers)



# Convert all names to uppercase using list comprehension.
names = ["aarya", "rahul", "priya", "amit"]
uppercase_names = [name.upper() for name in names]
print("Uppercase Names:", uppercase_names)



# Create a dictionary where number is the key and its cube is the value.
cube_dict = {num: num ** 3 for num in range(1, 6)}
print("Cube Dictionary:", cube_dict)



# Create a dictionary of word lengths.
words = ["Python", "Java", "HTML", "SQL"]
length_dict = {word: len(word) for word in words}
print("Length Dictionary:", length_dict)



# Create a dictionary for even numbers only.
even_square = {num: num ** 2 for num in range(1, 11) if num % 2 == 0}
print("Even Square Dictionary:", even_square)



# Remove duplicate values using set comprehension.
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6]
unique_numbers = {num for num in numbers}
print("Unique Numbers:", unique_numbers)



# Create a set of vowels from a string.
text = "Python Programming"
vowels = {ch.lower() for ch in text if ch.lower() in "aeiou"}
print("Vowels:", vowels)



# Create a set of squares of odd numbers.
odd_squares = {num ** 2 for num in range(1, 11) if num % 2 != 0}
print("Odd Squares:", odd_squares)



# Create a dictionary from a list of fruits where the key is the fruit name and the value is its length.
fruits = ["Apple", "Banana", "Mango", "Orange"]
fruit_length = {fruit: len(fruit) for fruit in fruits}
print("Fruit Length Dictionary:", fruit_length)


#End of Program
