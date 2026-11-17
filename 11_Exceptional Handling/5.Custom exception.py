'''
A custom exception is a user-defined exception. Python allows us to create our own exception by inheriting from the Exception class.
Syntax:
class MyException(Exception):
    pass
'''

# Example 1 : Invalid Age Exception
class InvalidAgeError(Exception):
    pass

age = -5

try:
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")

    print("Age:", age)

except InvalidAgeError as e:
    print(e)

print()



# Example 2 : Invalid Marks Exception
class InvalidMarksError(Exception):
    pass

marks = 120

try:
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks should be between 0 and 100.")

    print("Marks:", marks)

except InvalidMarksError as e:
    print(e)

print()



# Example 3 : Invalid Password Exception
class InvalidPasswordError(Exception):
    pass

password = "abc123"

try:
    if len(password) < 8:
        raise InvalidPasswordError("Password must contain at least 8 characters.")

    print("Password Accepted")

except InvalidPasswordError as e:
    print(e)

print()


#End of Program
