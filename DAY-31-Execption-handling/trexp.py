try:
    # Take input from the user
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    
    # Convert inputs to integers
    num1 = int(num1)
    num2 = int(num2)
    
    # Perform division
    result = num1 / num2
    
    print(f"The result of {num1} divided by {num2} is {result}")

except ValueError:
    # This block runs if input conversion to int fails
    print("Error: Please enter valid integers.")

except ZeroDivisionError:
    # This block runs if division by zero occurs
    print("Error: Cannot divide by zero.")

except Exception as e:
    # This block catches any other unexpected errors
    print(f"An unexpected error occurred: {e}")
