import random  # Importing the random module to generate random numbers

# Function to generate a random number between n and m
def number_guess(n, m):
    guess = random.randint(n, m)  # Generate a random integer between n and m (inclusive)
    return guess

# ---- Driver code starts here ----

# Ask the user for the lower bound of the guessing range
n = int(input("Enter the lower bound: "))

# Ask the user for the upper bound of the guessing range
m = int(input("Enter the upper bound: "))

# Ask the user for the maximum number of attempts allowed
max_attempts = int(input("Enter the maximum number of attempts: "))

# Generate the secret number using the function
number = number_guess(n, m)

# Start the guessing loop
while max_attempts > 0:
    # Prompt the user to enter their guess
    user_guess = int(input("Enter your guess: "))
    
    # Check if the user's guess is correct
    if user_guess == number:
        print("🎉 Congratulations! You guessed the number.")
        break  # Exit the loop if guessed correctly

    # Provide feedback if the guess is too low
    elif user_guess < number:
        print("📉 Your guess is too low.")
    
    # Provide feedback if the guess is too high
    else:
        print("📈 Your guess is too high.")
    
    # Decrease the number of remaining attempts
    max_attempts -= 1

    # Show the number of attempts left
    print(f"🕒 You have {max_attempts} attempts left.")

# This else block executes if the loop ends without a correct guess
else:
    print(f"❌ You've used all your attempts. The number was {number}. Better luck next time!")
