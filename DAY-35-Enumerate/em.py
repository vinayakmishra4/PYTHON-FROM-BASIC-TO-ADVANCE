# Day 35: Python program to demonstrate enumerate() with user input

# 🔹 Step 1: Take input from the user
# The user enters comma-separated items (e.g., apple,banana,cherry)
user_input = input("Enter a list of items separated by commas: ")

# 🔹 Step 2: Convert the input string into a list
items = [item.strip() for item in user_input.split(',')]

# 🔹 Step 3: Basic usage of enumerate()
print("\n🔹 Basic enumeration (index starts from 0):")
for index, item in enumerate(items):
    print(f"Index: {index} -> Item: {item}")

# 🔹 Step 4: Use custom start index
print("\n🔹 Enumeration starting from index 1:")
for index, item in enumerate(items, start=1):
    print(f"Item {index}: {item}")

# 🔹 Step 5: Convert enumerate to a list of tuples
print("\n🔹 Enumerate object as list of tuples:")
enumerated_list = list(enumerate(items))
print(enumerated_list)

# 🔹 Step 6: Use enumerate to modify the list (e.g., make uppercase)
print("\n🔹 Modifying items using index (e.g., converting to uppercase):")
for index, item in enumerate(items):
    items[index] = item.upper()

print("Modified list:", items)
