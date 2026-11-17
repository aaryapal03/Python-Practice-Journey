'''
A generator is a special type of function that returns values one at a time using the 'yield' keyword instead of 'return'.
Generators are memory-efficient because they generate values only when needed.

Syntax:
def function_name():
    yield value
'''

# Example 1 : Simple Generator
def numbers():
    yield 1
    yield 2
    yield 3

gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))

print()


# Example 2 : Generator with Loop
def count_numbers(n):
    for i in range(1, n + 1):
        yield i

gen = count_numbers(5)

for num in gen:
    print(num)

print()


# Example 3 : Generator for Squares

def square_numbers(n):
    for i in range(1, n + 1):
        yield i ** 2

gen = square_numbers(5)

for square in gen:
    print(square)

print()



# Example 4 : Generator Expression

numbers = (num ** 2 for num in range(1, 6))

for value in numbers:
    print(value)

print()

#End of Program
