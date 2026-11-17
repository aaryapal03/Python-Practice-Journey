'''
Nested Try-Except means placing one try-exceptblock inside another try-except block.
It is useful when one operation depends on another and both operations can generate different exceptions.

Syntax:
try:
    try:
        # Inner try block
    except:
        # Inner except block
except:
    # Outer except block
'''


# Example 1 : Nested Try-Except
try:
    print("Outer Try Block")

    try:
        num = int(input("Enter a number: "))
        result = 100 / num
        print("Result:", result)

    except ZeroDivisionError:
        print("Cannot divide by zero.")

except ValueError:
    print("Please enter a valid number.")



# Example 2 : Nested Try with File Handling
try:
     try:
        with open("sample.txt", "r") as file:
            print(file.read())

    except FileNotFoundError:
        print("File not found.")

except Exception as e:
    print("Outer Exception:", e)

print()



# Example 3 : Nested Try with List
numbers = [10, 20, 30]
try:
    try:
        index = int(input("Enter index: "))
        print(numbers[index])

    except IndexError:
        print("Index out of range.")

except ValueError:
    print("Please enter a valid integer.")

print()


#End of Program
