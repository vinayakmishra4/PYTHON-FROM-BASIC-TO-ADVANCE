"""
Simple Calculator Program
Author: VINAYAK
Date: 2025-09-01

This program performs basic arithmetic operations (add, subtract, multiply, divide)
on two numbers entered by the user. It follows PEP 8 styling and uses docstrings.
"""

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a divided by b. Raises error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def main():
    """Main function to run the calculator."""
    print("Welcome to the Calculator Program!\n")

    # Printing all docstrings
    print("Program Docstring:")
    print(__doc__)  # Module docstring

    print("\nFunction Docstrings:")
    print("add():", add.__doc__)
    print("subtract():", subtract.__doc__)
    print("multiply():", multiply.__doc__)
    print("divide():", divide.__doc__)
    print("main():", main.__doc__)

    # Taking user input
    num1 = float(input("\nEnter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Choose an operation: +, -, *, /")
    operator = input("Enter operator: ")

    # Performing the operation
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        try:
            result = divide(num1, num2)
        except ValueError as e:
            print(e)
            return
    else:
        print("Invalid operator.")
        return

    # Display result
    print(f"The result is: {result}")

# This ensures the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()
