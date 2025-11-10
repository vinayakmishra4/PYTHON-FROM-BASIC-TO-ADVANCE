# Mafire.py
"""
This script demonstrates the usage of the built-in Python functions map(), filter(), and reduce().
These functions are commonly used for functional programming to transform, filter, and aggregate data respectively.

1. map(): Transforms each item in a list using a specified function.
2. filter(): Selects items from a list that satisfy a given condition.
3. reduce(): Aggregates all items in a list into a single value by applying a binary function cumulatively.

Each section includes examples and explanatory comments.
"""

from functools import reduce

# -------------------------------
# Example 1: Using map()
# -------------------------------
# map() applies a function to every item of an iterable (like a list) and returns a map object (which can be converted to a list).
# Here, we will square each number in a list.

numbers = [1, 2, 3, 4, 5]

# Define a function to square a number
def square(number):
    return number * number

# Use map to apply 'square' to each number
squared_numbers = list(map(square, numbers))

print("Original numbers:", numbers)
print("Squared numbers using map():", squared_numbers)

# -------------------------------
# Example 2: Using filter()
# -------------------------------
# filter() creates a list of elements for which a function returns True.
# Here, we will filter out only even numbers from the list.

# Define a function to check if a number is even
def is_even(number):
    return number % 2 == 0

# Use filter to select even numbers
even_numbers = list(filter(is_even, numbers))

print("\nOriginal numbers:", numbers)
print("Even numbers using filter():", even_numbers)

# -------------------------------
# Example 3: Using reduce()
# -------------------------------
# reduce() applies a rolling computation to sequential pairs of values in a list.
# Here, we will compute the product of all numbers in the list.

# Define a function to multiply two numbers
def multiply(x, y):
    return x * y

# Use reduce to multiply all numbers together
product_of_numbers = reduce(multiply, numbers)

print("\nOriginal numbers:", numbers)
print("Product of numbers using reduce():", product_of_numbers)

# End of script demonstration
