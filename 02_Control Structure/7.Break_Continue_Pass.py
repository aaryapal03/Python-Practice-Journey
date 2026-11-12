
# Example 1 : break Statement
print("Break Statement")

for i in range(1, 11):
    if i == 6:
        break
    print(i)

print()


# Example 2 : continue Statement
print("Continue Statement")

for i in range(1, 11):
    if i == 6:
        continue
    print(i)

print()


# Example 3 : pass Statement
print("Pass Statement")

for i in range(1, 6):
    if i == 3:
        pass
     print('aarya')
   print(i, end=' ')

  

# Example 4 : break with while Loop
print("Break with While Loop")

count = 1

while count<=10:
    print(count)

    if count == 5:
        break

    count += 1

print()


# Example 5 : continue with while Loop
print("Continue with While Loop")

number = 0

while number < 5:
    number += 1

    if number == 3:
        continue

    print(number)


# End of Program
