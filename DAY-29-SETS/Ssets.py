# Day 29 - Sets in Python (with user input)

# A Set in Python is an unordered collection of unique elements.
# It does not allow duplicates and is written inside curly braces {}.

# -----------------------------
# Creating Sets with user input
# -----------------------------
# Taking input as comma-separated values and converting into a set
fruits = set(input("Enter some fruits (comma separated): ").split(","))
print("Fruits Set (duplicates removed):", fruits)

# Creating two sets of numbers from user input
A = set(map(int, input("Enter numbers for Set A (space separated): ").split()))
B = set(map(int, input("Enter numbers for Set B (space separated): ").split()))

print("\nSet A:", A)
print("Set B:", B)

# -----------------------------
# Adding Elements
# -----------------------------
new_fruit = input("\nEnter a fruit to add: ")
fruits.add(new_fruit)
print("After adding:", fruits)

# -----------------------------
# Removing Elements
# -----------------------------
remove_fruit = input("Enter a fruit to remove: ")
if remove_fruit in fruits:
    fruits.remove(remove_fruit)
    print("After removing:", fruits)
else:
    print(f"{remove_fruit} not found in set")

# -----------------------------
# Set Operations
# -----------------------------
print("\nUnion (A | B):", A | B)
print("Intersection (A & B):", A & B)
print("Difference (A - B):", A - B)
print("Symmetric Difference (A ^ B):", A ^ B)

# -----------------------------
# Set Methods
# -----------------------------
print("\nLength of set A:", len(A))
print("Is A subset of B?", A.issubset(B))
print("Is A superset of B?", A.issuperset(B))
print("Are A and B disjoint?", A.isdisjoint(B))

# -----------------------------
# Looping through a set
# -----------------------------
print("\nLooping through fruits set:")
for fruit in fruits:
    print(fruit)

# -----------------------------
# Converting between set and list
# -----------------------------
numbers_list = list(map(int, input("\nEnter some numbers with duplicates (space separated): ").split()))
numbers_set = set(numbers_list)  # removes duplicates
print("Original list:", numbers_list)
print("Unique values (set):", numbers_set)

# Converting back to list
unique_numbers = list(numbers_set)
print("Converted back to list:", unique_numbers)

# -----------------------------
# Frozen Set (Immutable Set)
# -----------------------------
frozen = frozenset(A)
print("\nFrozen Set created from Set A:", frozen)
# frozen.add(10)  # ❌ Not allowed (will cause error)