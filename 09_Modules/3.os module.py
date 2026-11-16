
# Import the os module
import os

# getcwd()
print(os.getcwd())

print()

# listdir()
print(os.listdir())

print()

# mkdir()
folder_name = "Demo_Folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder Created Successfully!")
else:
    print("Folder Already Exists!")

print()

# exists()
print(os.path.exists(folder_name))

print()

# rename()
new_folder_name = "Python_Demo"

if os.path.exists(folder_name):
    os.rename(folder_name, new_folder_name)
    print("Folder Renamed Successfully!")
else:
    print("Folder Not Found!")

print()

# getlogin()
try:
    print(os.getlogin())
except OSError:
    print("User name could not be determined.")

print()

# cpu_count()
print(os.cpu_count())

print()

# name
print(os.name)

print()

# environ
print("PATH =", os.environ.get("PATH"))

print()

# path.basename()
file_path = "C:/Users/Aarya/Documents/Python/file.txt"
print(os.path.basename(file_path))

print()

# path.dirname()
file_path = "C:/Users/Aarya/Documents/Python/file.txt"
print(os.path.dirname(file_path))

print()

# path.join()
new_path = os.path.join("Python", "Modules", "program.py")
print(new_path)

print()

# path.abspath()
print(os.path.abspath("03_os_module.py"))

print()

# Safe Information
print(os.getpid())

print()

# Examples (Not Executed)

os.remove("file.txt")     == Deletes a file ,  os.rmdir("Folder")       == Deletes an empty folder


#End of Program
