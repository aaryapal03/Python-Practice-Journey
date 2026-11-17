
# Practice Question 1
# Divide two numbers safely using try-except.
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid integers.")


# Practice Question 2
# Handle FileNotFoundError while opening a file.
try:
    with open("sample.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")


# Practice Question 3
# Handle IndexError.
numbers = [10, 20, 30]

try:
    index = int(input("Enter index: "))
    print(numbers[index])

except IndexError:
    print("Index out of range.")

except ValueError:
    print("Please enter a valid integer.")


# Practice Question 4
# Demonstrate else block.
try:
    number = int(input("Enter a number: "))
    print("Square:", number ** 2)

except ValueError:
    print("Invalid Input.")

else:
    print("Program executed successfully.")


# Practice Question 5
# Demonstrate finally block.
try:
    num = int(input("Enter a number: "))
    print(100 / num)

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Finally block always executes.")


# Practice Question 6
# Use raise keyword.
age = -10

try:
    if age < 0:
        raise ValueError("Age cannot be negative.")

    print(age)

except ValueError as e:
    print(e)


# Practice Question 7
# Create and use a custom exception.
class InvalidMarksError(Exception):
    pass

marks = 120

try:
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks should be between 0 and 100.")

    print(marks)

except InvalidMarksError as e:
    print(e)


# Practice Question 8
# Nested Try-Except
try:

    try:
        number = int(input("Enter a number: "))
        print(50 / number)

    except ZeroDivisionError:
        print("Cannot divide by zero.")

except ValueError:
    print("Please enter a valid integer.")


# Practice Question 9
# Handle multiple exceptions in one except block.
try:
    num = int(input("Enter a number: "))
    print(100 / num)

except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")


# Practice Question 10
# Generic Exception

try:
    data = {"Python": 100}
    print(data["Java"])

except Exception as e:
    print("Error:", e)

#End of Program
