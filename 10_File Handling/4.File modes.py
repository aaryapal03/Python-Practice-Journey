
# Create a Sample File
with open("sample.txt", "w") as file:
    file.write("Python File Handling\n")
    file.write("Learning Different File Modes\n")

print()


# 1. Read Mode (r)
with open("sample.txt", "r") as file:
    print(file.read())

print()


# 2. Write Mode (w)
with open("sample.txt", "w") as file:
    file.write("This file is overwritten.\n")

print()

# 3. Append Mode (a)
with open("sample.txt", "a") as file:
    file.write("This line is appended.\n")

print()


# 4. Exclusive Create Mode (x)
try:
    with open("new_file.txt", "x") as file:
        file.write("New File Created Successfully!")
    print("File Created!")
except FileExistsError:
    print("File Already Exists!")

print()


# 5. Read and Write Mode (r+)
with open("sample.txt", "r+") as file:
    print(file.read())

print()


# 6. Write and Read Mode (w+)
with open("sample.txt", "w+") as file:
    file.write("Using w+ Mode")

    file.seek(0)

    print(file.read())

print()


# 7. Append and Read Mode (a+)
with open("sample.txt", "a+") as file:
    file.write("\nLearning Python")

    file.seek(0)

    print(file.read())

print()


# File Information
with open("sample.txt", "r") as file:
    print("File Name :", file.name)
    print("File Mode :", file.mode)
    print("Readable :", file.readable())
    print("Writable :", file.writable())

print()

#End of Program
