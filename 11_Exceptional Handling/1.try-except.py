'''
Syntax:
try:
    # Code that may cause an error
except:
    # Code that runs if an error occurs
'''

# Example 1 : ZeroDivisionError
try:
    num = 10
    result = num / 0
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero.")



# Example 2 : ValueError
try:
    age = int(input("Enter your age: "))
    print("Age:", age)

except ValueError:
    print("Please enter a valid integer.")



# Example 3 : FileNotFoundError
try:
    with open("sample.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist.")


# Example 4 : Generic Exception
try:
    numbers = [10, 20, 30]
    print(numbers[5])

except Exception as e:
    print("An error occurred:", e)

print()


#End of Program
