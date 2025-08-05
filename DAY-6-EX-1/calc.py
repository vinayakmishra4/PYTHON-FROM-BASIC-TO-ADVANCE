# Take two integer inputs from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract b from a
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide a by b, with error handling for division by zero
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Function to find the remainder when a is divided by b
def modulus(a, b):
    return a % b

# Function to raise a to the power of b
def exponent(a, b):
    return a ** b

# Function to perform floor division (quotient without decimal)
def floor_divide(a, b):
    return a // b

# Run this block only if the script is executed directly
if __name__ == "__main__":
    print("Addition:", a, "+", b, "=", add(a, b))
    print("Subtraction:", a, "-", b, "=", subtract(a, b))
    print("Multiplication:", a, "*", b, "=", multiply(a, b))
    print("Division:", a, "/", b, "=", divide(a, b))
    print("Modulus:", a, "%", b, "=", modulus(a, b))
    print("Exponentiation:", a, "**", b, "=", exponent(a, b))
    print("Floor Division:", a, "//", b, "=", floor_divide(a, b))
