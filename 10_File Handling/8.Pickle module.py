
'''
The pickle module is used to store Python objects into a binary file and read them back.

Common Functions:
pickle.dump()  -> Write object to a binary file
pickle.load()  -> Read object from a binary file
'''

#Example no. 1-
import pickle

students = ["Aarya", "Rahul", "Priya", "Aman"]

with open("students.dat", "wb") as file:
    pickle.dump(students, file)

print()


with open("students.dat", "rb") as file:
    data = pickle.load(file)

print(data)

print()


#Example no. 2-
student = {"Name": "Aarya", "Age": 18, "Course": "BCA Data Science"}

with open("student.dat", "wb") as file:
    pickle.dump(student, file)

with open("student.dat", "rb") as file:
    info = pickle.load(file)

print(info)

print()

#End of Program
