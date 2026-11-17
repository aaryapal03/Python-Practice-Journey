
# 1. Write Data to a New File
with open("student.txt", "w") as file:
    file.write("Name : Aarya Pal\n")
    file.write("Course : FY BCA Data Science\n")
    file.write("College : Pillai College\n")

print()


# 2. Overwrite Existing File
with open("student.txt", "w") as file:
    file.write("This is new data.\n")
    file.write("Previous data has been replaced.\n")


print()


# 3. Write Multiple Lines
lines = ["Python\n", "Java\n", "C++\n", "SQL\n"]

with open("languages.txt", "w") as file:
    file.writelines(lines)

print()


# 4. Write User Input to a File
name = input("Enter your name: ")

with open("user.txt", "w") as file:
    file.write("User Name : " + name)

print()


# 5. Check Whether File is Writable
with open("student.txt", "w") as file:
    print(file.writable())

print()



# File Information
with open("student.txt", "w") as file:
    print("File Name :", file.name)
    print("File Mode :", file.mode)
    print("Is File Closed?", file.closed)

print()


#End of Program
