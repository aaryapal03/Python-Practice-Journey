'''
Encapsulation is the process of combining data (variables) and methods (functions) into a single unit (class).
It also helps in protecting data from unauthorized access.

Types of Access Modifiers:
1. Public
2. Protected
3. Private
'''


# Example 1 : Public Members
class Student:

    def __init__(self):
        self.name = "Aarya"
        self.age = 18


student = Student()

print("Name :", student.name)
print("Age  :", student.age)

print()



# Example 2 : Protected Members
class Student:

    def __init__(self):
        self._course = "BCA Data Science"


student = Student()

print("Course :", student._course)

print()



# Example 3 : Private Members
class BankAccount:

    def __init__(self):
        self.__balance = 5000

    def show_balance(self):
        print("Balance :", self.__balance)


account = BankAccount()

account.show_balance()

# The following line will give an error
# print(account.__balance)

print()



# Example 4 : Getter Method
class Employee:

    def __init__(self):
        self.__salary = 50000

    def get_salary(self):
        return self.__salary


employee = Employee()

print("Salary :", employee.get_salary())

print()



# Example 5 : Setter Method
class Employee:

    def __init__(self):
        self.__salary = 50000

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be positive.")


employee = Employee()

print("Old Salary :", employee.get_salary())

employee.set_salary(60000)

print("New Salary :", employee.get_salary())

print()



# Example 6 : Complete Example
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Marks should be between 0 and 100.")


student = Student("Aarya", 90)

print("Name  :", student.name)
print("Marks :", student.get_marks())

student.set_marks(95)

print("Updated Marks :", student.get_marks())

print()

#End of Program
✔ Encapsulation combines data and methods into one class.
✔ Public members can be accessed from anywhere.
✔ Protected members use a single underscore (_).
✔ Private members use double underscores (__).
✔ Getter methods are used to access private data.
✔ Setter methods are used to modify private data safely.
