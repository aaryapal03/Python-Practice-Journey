'''
The raise keyword is used to manually generate an exception.
It allows us to stop the program and display a custom error message when a condition is not met.

Syntax:
raise ExceptionType("Error Message")
''' 

# Example 1 : Raise ValueError
age = -5
try:
    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Age:", age)

except ValueError as e:
    print(e)


# Example 2 : Raise ZeroDivisionError
try:
    if number == 0:
        raise ZeroDivisionError("Number cannot be zero.")

    print("Number:", number)

except ZeroDivisionError as e:
    print(e)


# Example 3 : Raise TypeError
  try:
    if not isinstance(name, str):
        raise TypeError("Name must be a string.")

    print(name)

except TypeError as e:
    print(e)

#End of Program
