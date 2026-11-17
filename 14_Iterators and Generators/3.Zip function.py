
"The zip() function combines two or more iterables (list, tuple, string, etc.) into a single iterator of tuples."


# Example 1 : Zip Two Lists
names = ["Aarya", "Rahul", "Priya"]
marks = [90, 85, 95]

result = zip(names, marks)
print(list(result))

print()



# Example 2 : Iterate Using for Loop
subjects = ["Python", "Java", "SQL"]
scores = [88, 92, 85]

for subject, score in zip(subjects, scores):
    print(subject, ":", score)

print()



# Example 3 : Zip Three Lists
names = ["Aarya", "Rahul", "Priya"]
ages = [18, 19, 18]
cities = ["Mumbai", "Delhi", "Pune"]

for name, age, city in zip(names, ages, cities):
    print(name, "-", age, "-", city)

print()



# Example 4 : Different Length Lists
list1 = [1, 2, 3, 4]
list2 = ["A", "B"]

result = list(zip(list1, list2))
print(result)

print()


#End of Program
