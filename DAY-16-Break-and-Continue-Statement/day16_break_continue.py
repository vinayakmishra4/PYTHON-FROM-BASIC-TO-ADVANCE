# ---------------------------------------
# DAY 16: Break and Continue Statements
# ---------------------------------------

# Example 1: Using `break` in a loop
print("Example 1: break statement")
for i in range(1, 11):
    if i == 6:
        print("Breaking the loop at i =", i)
        break
    print("i =", i)

print("-" * 40)

# Example 2: Using `continue` in a loop
print("Example 2: continue statement")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print("Odd number:", i)

print("-" * 40)

# Example 3: `break` when searching in a list
print("Example 3: Searching in a list with break")
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
target = "Charlie"
for name in names:
    print("Checking:", name)
    if name == target:
        print("Found", target)
        break

print("-" * 40)

# Example 4: `continue` to skip invalid values
print("Example 4: Skipping empty values with continue")
inputs = ["John", "", "Jane", None, "Mike", " "]
for item in inputs:
    if not item or item.strip() == "":
        continue  # Skip empty or whitespace-only strings
    print("Valid input:", item)

print("-" * 40)

# Example 5: Nested loop with break
print("Example 5: Nested loops with break")
for i in range(3):
    for j in range(5):
        if j == 3:
            break  # Breaks the inner loop
        print(f"i = {i}, j = {j}")

print("-" * 40)

# Example 6: Nested loop with continue
print("Example 6: Nested loops with continue")
for i in range(3):
    for j in range(5):
        if j == 2:
            continue  # Skips j = 2
        print(f"i = {i}, j = {j}")
