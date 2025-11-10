# 🐍 Lambda Function Examples in Python
# ------------------------------------

# Example 1: Simple arithmetic lambda function
add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b if b != 0 else "Division by zero not allowed"

print("🔹 Basic Arithmetic using Lambda Functions:")
print(f"Addition: 10 + 5 = {add(10, 5)}")
print(f"Subtraction: 10 - 5 = {subtract(10, 5)}")
print(f"Multiplication: 10 * 5 = {multiply(10, 5)}")
print(f"Division: 10 / 5 = {divide(10, 5)}")
print()

# Example 2: Using lambda with map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print("🔹 Squares of numbers using map():", squares)
print()

# Example 3: Using lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("🔹 Even numbers using filter():", even_numbers)
print("🔹 Odd numbers using filter():", odd_numbers)
print()

# Example 4: Using lambda with sorted()
students = [
    {"name": "Alice", "age": 22, "score": 88},
    {"name": "Bob", "age": 20, "score": 95},
    {"name": "Charlie", "age": 23, "score": 70}
]
# Sort by score (descending)
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)
print("🔹 Students sorted by score (highest first):")
for s in sorted_students:
    print(f"{s['name']} - Score: {s['score']}")
print()

# Example 5: Using lambda with reduce()
from functools import reduce

product = reduce(lambda x, y: x * y, numbers)
print("🔹 Product of all numbers using reduce():", product)
print()

# Example 6: Conditional lambda
check_age = lambda age: "Adult" if age >= 18 else "Minor"
ages = [15, 18, 25]
status = list(map(check_age, ages))
print("🔹 Age classification using lambda:", status)
print()

# Example 7: Nested lambda (Advanced use)
power_function = lambda n: (lambda x: x ** n)
square = power_function(2)
cube = power_function(3)
print("🔹 Using nested lambda for power calculation:")
print("Square of 5:", square(5))
print("Cube of 3:", cube(3))

# ------------------------------------
# End of Program
# ------------------------------------
