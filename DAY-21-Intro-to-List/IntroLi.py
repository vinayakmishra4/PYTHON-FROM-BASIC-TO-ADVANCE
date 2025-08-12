# 1. Creating a list using input
fruits = input("Enter fruits separated by commas: ").split(",")
fruits = [fruit.strip() for fruit in fruits]  # Remove extra spaces
print("\nYour fruit list:", fruits)

# 2. Accessing list items
print("First fruit:", fruits[0] if fruits else "List is empty")
print("Last fruit:", fruits[-1] if fruits else "List is empty")

# 3. Looping through the list
print("\nLooping through your fruits:")
for fruit in fruits:
    print(fruit)
