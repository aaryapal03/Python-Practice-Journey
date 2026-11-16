
# 1. Import Entire Module
import math
print("Square Root of 25 =", math.sqrt(25))
print()


# 2. Import Specific Function
from math import factorial
print("Factorial of 5 =", factorial(5))
print()


# 3. Import Multiple Functions
from math import sqrt, pow
print("Square Root of 64 =", sqrt(64))
print("2 Raised to Power 5 =", pow(2, 5))
print()


# 4. Import Module with Alias
import math as m
print("Value of PI =", m.pi)
print("Ceiling Value =", m.ceil(5.2))
print()


# 5. Import Specific Function with Alias
from math import factorial as fact

print("5. Import Function with Alias")
print("Factorial of 6 =", fact(6))
print()


# 6. Import All Functions
from math import *
print("Floor Value =", floor(7.9))
print("Value of e =", e)
print()


# 7. Import Custom Module
import my_module

print("Addition =", my_module.add(70, 30))
print()


#End of Program
