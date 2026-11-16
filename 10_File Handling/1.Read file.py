
# 1. Read Entire File
with open("sample.txt", "r") as file:
    content = file.read()

print(content)

print()

# -----------------------------------------
# 2. Read First Line
# -----------------------------------------

with open("sample.txt", "r") as file:
    first_line = file.readline()

print("Read First Line")
print(first_line)

print()

# -----------------------------------------
# 3. Read All Lines
# -----------------------------------------

with open("sample.txt", "r") as file:
    lines = file.readlines()

print("Read All Lines")
print(lines)

print()

# -----------------------------------------
# 4. Read File Line by Line
# -----------------------------------------

with open("sample.txt", "r") as file:
    print("Reading Line by Line")

    for line in file:
        print(line.strip())

print()

# -----------------------------------------
# 5. Check File is Readable
# -----------------------------------------

with open("sample.txt", "r") as file:
    print("Is File Readable?")
    print(file.readable())

print()

# -----------------------------------------
# File Information
# -----------------------------------------

with open("sample.txt", "r") as file:
    print("File Name :", file.name)
    print("File Mode :", file.mode)
    print("Is File Closed?", file.closed)

print()

