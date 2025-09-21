# DAY-36 Example: Using if __name__ == "__main__"

# A simple function that can be reused when this file is imported
def greet(name):
    return f"Hello, {name}! Welcome to Python."

# Another function for demonstration
def add(a, b):
    return a + b

# The main entry point of this script
# This block will only run when the file is executed directly
if __name__ == "__main__":
    # Code here runs ONLY when you run: python Main.py
    print("Running Main.py directly...")
    
    # Ask user for their name and two numbers
    user_name = input("Enter your name: ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Call the functions defined above with user inputs
    print(greet(user_name))
    print(f"Sum of {num1} + {num2} =", add(num1, num2))

    # Extra note
    print("This block did not run because of import, but because the file was executed directly.")