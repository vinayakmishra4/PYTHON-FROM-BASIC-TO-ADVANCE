# WAP to sum of n natural numbers

# Take input from the user and convert it to an integer
number = int(input("Enter the number: "))

# Initialize total sum to 0
total = 0

# Initialize counter i to 1, since natural numbers start from 1
i = 1

# Loop from 1 to number (inclusive)
while i <= number:
    total += i    # Add current number i to total sum
    i += 1        # Increment i by 1 to move to the next natural number

# After the loop finishes, print the result
print("Sum of", number, "natural numbers is", total)
