'''
An iterator accesses elements one by one.
iter() creates an iterator from an iterable and next() returns the next element.
When elements are finished, StopIteration occurs.

Syntax:
iterator = iter(iterable)
next(iterator)
'''

# Example 1 : Iterator with List

numbers = [10, 20, 30, 40]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

print()



# Example 2 : Iterator with String
text = "Python"

iterator = iter(text)

print(next(iterator))
print(next(iterator))
print(next(iterator))

print()



# Example 3 : Using for Loop
fruits = ["Apple", "Banana", "Mango"]

iterator = iter(fruits)
for i in iterator:
    print(i)

print()


# Example 4 : StopIteration
colors = ["Red", "Green"]

iterator = iter(colors)
try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))      # No more elements

except StopIteration:
    print("No more elements in the iterator.")

print()


#End of Program
