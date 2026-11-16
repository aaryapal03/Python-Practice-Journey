
# Import the random module
import random

# random()
print(random.random())

# randint()
print(random.randint(1, 10))

# randrange()
print(random.randrange(1, 20, 2))

# uniform()
print(random.uniform(1, 10))

# choice()

fruits = ["Apple", "Banana", "Mango", "Orange"]
print(random.choice(fruits))

print()

# choices()

colors = ["Red", "Blue", "Green", "Yellow"]
print(random.choices(colors, k=3))

print()

# sample()

numbers = [10, 20, 30, 40, 50]
print(random.sample(numbers, 3))

print()

# shuffle()
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print(cards)

print()

# seed()
random.seed(10)
print(random.randint(1, 100))
print(random.randint(1, 100))

print()

# getrandbits()
print(random.getrandbits(8))

print()

#End of Program
