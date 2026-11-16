
# Positional Arguments
def student(name, age):
    print("Name :", name)
    print("Age :", age)

student("Aarya", 19)


# Keyword Arguments

def employee(name, salary):
    print("Name :", name)
    print("Salary :", salary)

employee(salary=50000, name="Rahul")


# Default Arguments
def greet(name="Guest"):
     print("Hello,", name)

greet()
greet("Aarya")


# Positional Variable-Length Arguments (*args)
def add_numbers(a,*b,c):
    total=a+c
    print("addition of 2 no. are",total)
    total=a+sum(b)+c
    print("whole addition:-",total)
  
add_numbers(10, 20, 30, 40,50,60,70,c=80)


# Keyword Variable-Length Arguments (**kwargs)
def details(a,*b,**c):
    
    total=a+sum(b)
    print("sum of first and last no are:-",total)

    total=total +sum(c.values())
    print("whole addition:-",total)
    
  
details(2,5,6,7,8,i=9,k=10,u=3)


# Combining Different Types of Arguments
def introduction(name, age=18, *skills):
    print("Combining Arguments")
    print("Name :", name)
    print("Age :", age)
    print("Skills :", skills)

introduction("Aarya", 19, "Python", "SQL", "Git")

#End of Program
