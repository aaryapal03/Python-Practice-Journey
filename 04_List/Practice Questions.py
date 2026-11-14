
# Program 1 : Create and Access a List
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("List :", fruits)
print("First Element :", fruits[0])
print("Last Element :", fruits[-1])

print()


# Program 2 : List Slicing
numbers = [10, 20, 30, 40, 50, 60]

print("Original List :", numbers)
print("First Three :", numbers[:3])
print("Last Three :", numbers[-3:])
print("Every Second Element :", numbers[::2])

print()


# Program 3 : List Methods
cities = ["Mumbai", "Delhi", "Pune"]

cities.append("Chennai")
cities.insert(1, "Hyderabad")
cities.remove("Delhi")
print(cities)

print()


# Program 4 : Built-in Functions
marks = [85, 92, 76, 88, 95]

print("Length :", len(marks))
print("Maximum :", max(marks))
print("Minimum :", min(marks))
print("Sum :", sum(marks))

print()


# Program 5 : Sorting and Reversing
values = [45, 12, 78, 34, 23]

print("Original :", values)
values.sort()
print("Sorted :", values)
values.reverse()
print("Reversed :", values)

print()


# Program 6 : Searching in List
colors = ["Red", "Blue", "Green", "Blue", "Yellow"]

print("Index of Green :", colors.index("Green"))
print("Count of Blue :", colors.count("Blue"))

print()


# Program 7 : Membership Operator
subjects = ["Python", "Java", "C++", "SQL"]

print("Python" in subjects)
print("HTML" not in subjects)

print()


# Program 8 : Copy a List
list1 = [10, 20, 30]
list2 = list1.copy()

print("Original List :", list1)
print("Copied List :", list2)

print()


# Program 9 : Nested List

students = [ ["Aarya", 19], ["Rahul", 20], ["Priya", 18] ]

for student in students:
    print("Name :", student[0])
    print("Age :", student[1])
    print()



# Program 10 : Mixed List Program
numbers = [30, 10, 50, 20, 40]

print("Original List :", numbers)
numbers.append(60)
numbers.sort()

print("Updated List :", numbers)
print("Length :", len(numbers))
print("Maximum :", max(numbers))
print("Minimum :", min(numbers))
print("Sum :", sum(numbers))
print("First Element :", numbers[0])
print("Last Element :", numbers[-1])

print()

#Program 11 :Append in list
alpha=[]
lower=[]
upper=[]
digit=[]
sc=[]
S=input('enter a message')
for i in S:
    if i.isalpha():
        alpha.append(i)
        if i.isupper():
            upper.append(i)
        else:
            lower.append(i)

    elif i.isdigit():
        digit.append(i)

    else:
        sc.append(i)


print('Alphabets are:-',alpha)
print('Uppercase are:-',upper)
print('lowercase are:-',lower)
print('digits are:-',digit)
print('sc are:-',sc)


# End of Practice Programs
