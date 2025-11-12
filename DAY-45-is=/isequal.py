# Python program to demonstrate =, ==, and is

# Assignment operator '='
x = [1, 2, 3]       # x is assigned a list
y = x               # y now refers to the same object as x
z = [1, 2, 3]       # z is a new list with the same content as x

print("Values of lists:")
print("x:", x)
print("y:", y)
print("z:", z)
print()

# Equality comparison '=='
print("Checking value equality with '==':")
print("x == y:", x == y)  # True, same values
print("x == z:", x == z)  # True, same values
print()

# Identity comparison 'is'
print("Checking object identity with 'is':")
print("x is y:", x is y)  # True, same object
print("x is z:", x is z)  # False, different objects
print()

# Modify one list to show the effect
y.append(4)
print("After modifying y:")
print("x:", x)
print("y:", y)
print("z:", z)
print()

print("Checking identity and equality again:")
print("x == y:", x == y)  # True, values now different? Actually, x=y points to same list, so True
print("x is y:", x is y)  # True, still the same object
print("x == z:", x == z)  # False, values different now
print("x is z:", x is z)  # False, different objects
