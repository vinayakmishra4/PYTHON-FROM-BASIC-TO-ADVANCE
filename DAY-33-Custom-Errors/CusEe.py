# Example: Custom Errors in Python

# Step 1: Define Custom Error Classes
class NegativeNumberError(Exception):
    """Raised when a number is negative"""
    pass

class TooLargeNumberError(Exception):
    """Raised when a number is too large"""
    pass

# Step 2: Function to check the number
def check_number(num):
    if num < 0:
        raise NegativeNumberError("❌ The number cannot be negative!")
    elif num > 100:
        raise TooLargeNumberError("❌ The number is too large! Please enter below 100.")
    else:
        print(f"✅ The number {num} is valid!")

# Step 3: Main program with input
try:
    user_input = int(input("Enter a number between 0 and 100: "))  # Taking input from user
    check_number(user_input)
except ValueError:
    print("❌ Invalid input! Please enter a valid integer.")
except NegativeNumberError as e:
    print(e)
except TooLargeNumberError as e:
    print(e)
finally:
    print("👉 Program finished.")