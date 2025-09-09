def safe_division():
    """
    Function to safely perform division using try-except-else-finally.
    Demonstrates Python error handling with user input.
    """
    try:
        # Taking user input
        num1 = int(input("Enter the numerator: "))
        num2 = int(input("Enter the denominator: "))

        # Attempt division
        result = num1 / num2

    except ValueError:
        # Handles invalid number input
        print("❌ Invalid input! Please enter numbers only.")

    except ZeroDivisionError:
        # Handles division by zero
        print("❌ Cannot divide by zero!")

    else:
        # Executes only if no exception occurs
        print(f"✅ Division successful! Result = {result}")

    finally:
        # Always executes no matter what
        print("🔹 Program ended (finally block executed).")


# Call the function
safe_division()