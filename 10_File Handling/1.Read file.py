
# 1. Read Entire File
with open("sample.txt", "r") as file:
    content = file.read()

print(content)


# 2. Read First Line
with open("sample.txt", "r") as file:
    first_line = file.readline()

print("Read First Line")
print(first_line)



# 3. Read All Lines
with open("sample.txt", "r") as file:
    lines = file.readlines()

print("Read All Lines")
print(lines)



# 4. Read File Line by Line
with open("sample.txt", "r") as file:
    for i in file:
        print(i.strip())

print()


# 5. Check File is Readable
with open("sample.txt", "r") as file:
    print(file.readable())

print()

# File Information
with open("sample.txt", "r") as file:
    print("File Name :", file.name)
    print("File Mode :", file.mode)
    print("Is File Closed?", file.closed)

print()

