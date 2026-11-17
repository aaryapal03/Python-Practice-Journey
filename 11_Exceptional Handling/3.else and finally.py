'''
Syntax:
try:
    # Code that may cause an exception
except:
    # Handle exception
else:
    # Executes if no exception occurs
finally:
    # Always executes
'''

# Example 1 : else Block
try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter a valid number.")

else:
    print("Result:", result)
    print("No exception occurred.")



# Example 2 : finally Block
try:
    file = open("sample.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("Finally block executed.")


# Example 3 : else + finally
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")

else:
    print("Division Result:", result)

finally:
    print("Program execution completed.")

print()

#End of Program
