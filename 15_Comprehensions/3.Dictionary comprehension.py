
# Example 1 : Number and Square
numbers = [1, 2, 3, 4, 5]

square_dict = {num: num ** 2 for num in numbers}
print("Original List      :", numbers)
print("Square Dictionary  :", square_dict)

print()


# Example 2 : Convert Values to Uppercase
fruits = ["apple", "banana", "mango"]

fruit_dict = {fruit: fruit.upper() for fruit in fruits}
print("Original List :", fruits)
print("Dictionary    :", fruit_dict)

print()



# Example 3 : Even Numbers Only
numbers = range(1, 11)

even_dict = {num: num ** 2 for num in numbers if num % 2 == 0}
print("Even Number Dictionary :", even_dict)

print()



# Example 4 : Word Length
words = ["Python", "Java", "C", "HTML"]

length_dict = {word: len(word) for word in words}
 print("Words              :", words)
print("Length Dictionary  :", length_dict)

print()


#End of Program
