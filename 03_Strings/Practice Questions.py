
# Program 1 : Reverse a String
text = "Python"

print("Program 1")
print("Original String :", text)
print("Reversed String :", text[::-1])

print()


# Program 2 : Count Vowels
text = "Artificial Intelligence"

count = 0

for letter in text.lower():
    if letter in "aeiou":
        count += 1

print("Number of Vowels :", count)
print()



# Program 3 : Check Palindrome
text = "madam"

print("Program 3")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

print()

# ==========================================
# Program 4 : Count Words
# ==========================================

sentence = "I Love Python Programming"

words = sentence.split()

print("Program 4")
print("Total Words :", len(words))

print()

# ==========================================
# Program 5 : Count Characters
# ==========================================

text = "Python"

print("Program 5")
print("Total Characters :", len(text))

print()

# ==========================================
# Program 6 : Convert Case
# ==========================================

text = "python programming"

print("Program 6")
print("Upper :", text.upper())
print("Lower :", text.lower())
print("Title :", text.title())

print()

# ==========================================
# Program 7 : Replace a Word
# ==========================================

text = "I Love Python"

print("Program 7")
print(text.replace("Python", "AI"))

print()

# ==========================================
# Program 8 : Find a Character
# ==========================================

text = "Data Science"

print("Program 8")
print("Index of 'S' :", text.find("S"))

print()

# ==========================================
# Program 9 : Check Startswith & Endswith
# ==========================================

text = "Python Programming"

print("Program 9")
print(text.startswith("Python"))
print(text.endswith("Programming"))

print()

# ==========================================
# Program 10 : Join List into String
# ==========================================

words = ["Python", "AI", "Machine Learning"]

result = " | ".join(words)

print("Program 10")
print(result)

print()

# ==========================================
# Program 11 : Print Each Character
# ==========================================

text = "Python"

print("Program 11")

for letter in text:
    print(letter)

print()

# ==========================================
# Program 12 : Print Characters at Even Index
# ==========================================

text = "Programming"

print("Program 12")

for i in range(0, len(text), 2):
    print(text[i])

print()

# ==========================================
# Program 13 : Remove Extra Spaces
# ==========================================

text = "     Hello Python     "

print("Program 13")
print(text.strip())

print()

# ==========================================
# Program 14 : Check String Type
# ==========================================

text1 = "Python"
text2 = "12345"
text3 = "Python123"

print("Program 14")

print("IsAlpha :", text1.isalpha())
print("IsDigit :", text2.isdigit())
print("IsAlnum :", text3.isalnum())

print()

# ==========================================
# Program 15 : Count Frequency of a Character
# ==========================================

text = "programming"

character = "m"

print("Program 15")
print("Frequency :", text.count(character))

print()

# ==========================================
# Program 16 : Concatenate Two Strings
# ==========================================

first_name = "Aarya"
last_name = "Pal"

print("Program 16")
print(first_name + " " + last_name)

print()

# ==========================================
# Program 17 : Repeat a String
# ==========================================

text = "Python "

print("Program 17")
print(text * 3)

print()

# ==========================================
# Program 18 : Membership Operator
# ==========================================

text = "Artificial Intelligence"

print("Program 18")

print("'AI' in text :", "AI" in text)
print("'Machine' not in text :", "Machine" not in text)

print()

# ==========================================
# Program 19 : First and Last Character
# ==========================================

text = "Python"

print("Program 19")

print("First Character :", text[0])
print("Last Character  :", text[-1])

print()

# ==========================================
# Program 20 : Mixed String Program
# ==========================================

text = "python programming"

print("Program 20")

print("Original String :", text)
print("Upper Case      :", text.upper())
print("Lower Case      :", text.lower())
print("Title Case      :", text.title())
print("Length          :", len(text))
print("Reverse         :", text[::-1])
print("Contains Python :", "python" in text)
print("Count of 'm'    :", text.count("m"))
print("Replace         :", text.replace("python", "Java"))

print()

# ==========================================
# End of Practice Programs
# ==========================================
