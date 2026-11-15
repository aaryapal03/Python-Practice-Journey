
# Original Sets
set1 = {10, 20, 30, 40, 50}
set2 = {40, 50, 60, 70, 80}
print(set1)
print()

print(set2)
print()

# Union
print(set1.union(set2))
print()

print("Union using |")
print(set1 | set2)
print()

# Intersection
print(set1.intersection(set2))
print()

print("Intersection using &")
print(set1 & set2)

print()

# Difference
print(set1.difference(set2))
print()

print("Difference using -")
print(set1 - set2)
print()

# Symmetric Difference
print(set1.symmetric_difference(set2))
print()

print("Symmetric Difference using ^")
print(set1 ^ set2)
print()

# issubset()
A = {10, 20}
B = {10, 20, 30, 40}

print(A.issubset(B))

print()

# issuperset()
print(B.issuperset(A))

print()

# isdisjoint()
X = {1, 2}
Y = {3, 4}

print(X.isdisjoint(Y))

print()

# Membership Operators

print("Membership Operators")

print("20 in set1 :", 20 in set1)
print("100 not in set1 :", 100 not in set1)

print()

#End of Program
