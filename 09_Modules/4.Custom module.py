#1st File name:- 
my_module.py

# Function to add two numbers

def add(a, b):
    return a + b

# Function to find the square of a number

def square(num):
    return num ** 2

# Variable

college = "XYZ College"

# Constant

PI = 3.14159


#2nd  file name:- 
04_custom_module.py

# Import the custom module
import my_module

print("Addition")
print(my_module.add(15, 25))
print()


print("Square")
print(my_module.square(8))
print()


print("College Name")
print(my_module.college)
print()


print("Value of PI")
print(my_module.PI)
print()

#End of Program 
