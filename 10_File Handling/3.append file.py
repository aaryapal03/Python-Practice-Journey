
# Create a Sample File
with open("student.txt", "w") as file:
    file.write("Name : Aarya Pal\n")
    file.write("Course : FY BCA Data Science\n")

print()


# 1. Append Data to a File
with open("student.txt", "a") as file:
    file.write("College : Pillai College\n")

print()


# 2. Append Multiple Lines
lines = ["Python\n", "SQL\n", "Machine Learning\n"]
with open("student.txt", "a") as file:
    file.writelines(lines)

print()


# 3. Append User Input
city = input("Enter Your City: ")

with open("student.txt", "a") as file:
    file.write("City : " + city + "\n")

print()


# 4. Display Updated File Content
with open("student.txt", "r") as file:
    print(file.read())

print()


# 5. Check Whether File is Writable
with open("student.txt", "a") as file:
    print(file.writable())

print()


# File Information
with open("student.txt", "a") as file:
    print("File Name :", file.name)
    print("File Mode :", file.mode)
    print("Is File Closed?", file.closed)

print()

#End of Program
