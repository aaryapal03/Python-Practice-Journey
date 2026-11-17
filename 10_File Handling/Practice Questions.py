
# Create a file and write your details.
with open("student.txt", "w") as file:
    file.write("Name : Aarya\n")
    file.write("Age : 18\n")
    file.write("Course : BCA Data Science")

print("Data written successfully.")


# Read the complete file.
with open("student.txt", "r") as file:
    print(file.read())


# Append one line to the file.
with open("student.txt", "a") as file:
    file.write("\nCollege : Pillai University")

print("Line appended successfully.")


# Count the total characters.
with open("student.txt", "r") as file:
    data = file.read()

print("Total Characters :", len(data))

# Count total words.
with open("student.txt", "r") as file:
    data = file.read()

print("Total Words :", len(data.split()))


# Count total lines.
with open("student.txt", "r") as file:
    lines = file.readlines()

print("Total Lines :", len(lines))


# Read first 10 characters and display pointer position.
with open("student.txt", "r") as file:
    print(file.read(10))
    print("Current Position :", file.tell())


# Move pointer to beginning and read again.
with open("student.txt", "r") as file:
    file.read(15)

    file.seek(0)

    print(file.read())


# Copy contents of one file into another.
with open("student.txt", "r") as source:
    data = source.read()

with open("copy.txt", "w") as destination:
    destination.write(data)

print("File copied successfully.")


# Binary File
with open("message.bin", "wb") as file:
    file.write(b"Welcome to Python")

with open("message.bin", "rb") as file:
    print(file.read())


# Store a list using Pickle.
numbers = [10, 20, 30, 40, 50]

with open("numbers.dat", "wb") as file:
    pickle.dump(numbers, file)

with open("numbers.dat", "rb") as file:
    print(pickle.load(file))


# Store a dictionary using Pickle.
student = {"Name": "Aarya",  "Age": 18, "Course": "BCA DS"}

with open("student.dat", "wb") as file:
    pickle.dump(student, file)

with open("student.dat", "rb") as file:
    print(pickle.load(file))


#End of Program
