'''
Syntax:
try:
    # Code that may cause an exception
except ExceptionType1:
    # Handle first exception
except ExceptionType2:
    # Handle second exception
except ExceptionType3:
    # Handle third exception
'''


# Example 1 : Handling Different Exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)

except ValueError:
    print("Invalid input! Please enter a number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


# Example 2 : List Index Error
try:
    numbers = [10, 20, 30]
    index = int(input("Enter index: "))
    print(numbers[index])

except ValueError:
    print("Please enter a valid integer.")

except IndexError:
    print("Index is out of range.")


# Example 3 : Multiple Exceptions in One Block
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print(result)

except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")


# Example 4 : Generic Exception
try:
    my_dict = {"A": 10, "B": 20}
    print(my_dict["C"])

except KeyError:
    print("Key not found.")

except Exception as e:
    print("Some other error occurred:", e)

#End of Program
