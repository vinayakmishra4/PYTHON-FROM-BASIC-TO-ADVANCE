# Day 23 - Tuples Introduction with User Input

# Asking user for tuple elements
# Prompting the user to enter elements separated by commas to create a tuple.
# We use commas as a simple way to input multiple values in one line.
print("Enter elements for the tuple separated by commas:")
user_input = input("Elements: ")

# Creating tuple from input
# We split the input string by commas to get individual elements.
# Using tuple() to convert the list of elements into an immutable tuple.
# Stripping spaces to clean up any extra whitespace around elements.
elements = tuple(item.strip() for item in user_input.split(","))

# Display the tuple
# Showing the user the tuple they have created.
print("\nYour tuple is:", elements)

# Accessing elements
# Demonstrating how to access elements by index in a tuple.
# Index 0 is the first element, and -1 is the last element.
print("\nAccessing elements in the tuple:")
print("First element:", elements[0])
print("Last element:", elements[-1])

# Nested tuple example
# Creating a tuple that contains another tuple inside it.
# This shows how tuples can be nested to form complex data structures.
print("\nCreating a nested tuple...")
nested_tuple = (elements, ("Python", "Tuples"))
print("Nested tuple:", nested_tuple)

# Tuple unpacking
# Unpacking allows us to assign tuple elements to individual variables in one step.
# Useful when you know the number of elements and want to work with them separately.
if len(elements) >= 3:
    print("\nTuple unpacking (first three elements):")
    a, b, c = elements[:3]  # Taking first three elements and unpacking
    print("a:", a)
    print("b:", b)
    print("c:", c)
else:
    print("\nNot enough elements for unpacking example (need at least 3).")

# Usage example: Returning multiple values from a function
# Defining a function that returns two values: minimum and maximum of a tuple.
# Demonstrates how tuples can be used to return multiple values from functions.
def min_max(values):
    return min(values), max(values)

# Convert to integers if possible
# Attempting to convert tuple elements to integers to perform numeric operations.
# Using try-except to handle the case where conversion fails (non-numeric input).
try:
    num_elements = tuple(int(item) for item in elements)
    minimum, maximum = min_max(num_elements)
    print("\nMinimum value:", minimum)
    print("Maximum value:", maximum)
except ValueError:
    # If conversion fails, we inform the user that min/max calculation is skipped.
    print("\nTuple contains non-numeric values, skipping min/max example.")

# Demonstrating immutability
# Tuples are immutable, meaning their elements cannot be changed after creation.
# Trying to modify an element will raise a TypeError.
# This property makes tuples useful for fixed collections of data.
print("\nTrying to modify the tuple (this will raise an error):")
try:
    elements[0] = "Changed"
except TypeError as e:
    print("Error:", e)