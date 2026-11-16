
# Example 1: Print Numbers from 1 to 5
def print_numbers(n):
    if n > 5:
        return

    print(n)
    print_numbers(n + 1)

print("Example 1")
print_numbers(1)

print()

# Example 2: Factorial Using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print("Example 2")
print("Factorial of 5 =", factorial(5))

print()

# Example 3: Sum of First N Natural Numbers
def natural_sum(n):
    if n == 1:
        return 1

    return n + natural_sum(n - 1)

print("Example 3")
print("Sum =", natural_sum(5))

print()

# Example 4: Power of a Number

def power(base, exponent):
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)

print("Example 4")
print("2^5 =", power(2, 5))

print()

# Example 5: Countdown
def countdown(n):
    if n == 0:
        print("Done!")
        return

    print(n)
    countdown(n - 1)

print("Example 5")
countdown(5)

print()

#End of Program
