"The seek() method moves the file pointer to a specified position."

#Example no. 1 :- 
with open("sample.txt", "r") as file:
    file.seek(6)          # Move pointer to 6th character
    print(file.read())

print()


"Returns the current position of the file pointer."

#Example no. 2 :-
with open("sample.txt", "r") as file:
    print("Starting Position:", file.tell())

    file.read(10)
    print("After reading 10 characters:", file.tell())

    file.seek(0)
    print("After seek(0):", file.tell())

print()

#End of Program
