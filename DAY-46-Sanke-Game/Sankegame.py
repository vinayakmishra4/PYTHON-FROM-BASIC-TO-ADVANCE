# SANKE WATER GUN GAME

# This is a simple Python implementation of the classic "Snake, Water, Gun" game.
# The rules are:
# - Snake drinks Water → Snake wins
# - Gun shoots Snake → Gun wins
# - Water damages Gun → Water wins
# If both the user and the computer choose the same option, it's a tie.
#
# The program randomly selects a choice for the computer and asks the user to enter their choice.
# It then compares the two choices and determines the winner based on the rules above.
#
# Example:
# Enter your choice (snake, water, gun): snake
# Computer chose: water
# Output: You win! Snake drinks water.

import random
# Importing the random module to allow the computer to make a random choice

choices = ['snake', 'water', 'gun']
# Defining the possible options the player and computer can choose from

computer_choice = random.choice(choices)
# Computer randomly selects one of the options from the list

user_choice = input("Enter your choice (snake, water, gun): ").lower()
# Taking the user's choice and converting it to lowercase to avoid case mismatches

# Defining a function to compare the choices and decide the winner
def snake_water_gun(user_choice, computer_choice):
    # If both choices are the same, it's a tie
    if user_choice == computer_choice:
        return "It's a tie!"
    
    # Logic for when the user selects 'snake'
    if user_choice == 'snake':
        if computer_choice == 'water':
            return "You win! Snake drinks water."
        else:
            return "You lose! Gun shoots snake."
    
    # Logic for when the user selects 'water'
    if user_choice == 'water':
        if computer_choice == 'gun':
            return "You win! Water damages gun."
        else:
            return "You lose! Snake drinks water."
    
    # Logic for when the user selects 'gun'
    if user_choice == 'gun':
        if computer_choice == 'snake':
            return "You win! Gun shoots snake."
        else:
            return "You lose! Water damages gun."
        

# Calling the function and storing the result in a variable
result = snake_water_gun(user_choice, computer_choice)

# Displaying what the computer chose
print(f"Computer chose: {computer_choice}")

# Displaying the result of the game (win/lose/tie)
print(result)