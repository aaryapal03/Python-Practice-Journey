
#using with statment
with open("sample.txt", "r") as file:
    data = file.read()
    print(data)

print()


with open("output.txt", "w") as file:
    file.write("Hello Aarya!\n")
    file.write("Learning Python File Handling.")


print()



#without using with statement:- 
file = open("sample.txt", "r")
print(file.read())

# We must close the file manually
file.close()
print()


WITHOUT WITH STATEMENT
1. Need to call file.close() manually.
2. If you forget close(), the file remains open.
3. More chances of errors.
4. Code is longer.


WITH STATEMENT
1. Automatically closes the file.
2. No need to call file.close().
3. Safer and cleaner code.
4. Recommended way to work with files.
