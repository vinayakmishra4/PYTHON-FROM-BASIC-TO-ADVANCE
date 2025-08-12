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

# 4. Adding items
new_fruit = input("\nEnter a fruit to append to the list: ")
fruits.append(new_fruit)
print("After append:", fruits)

insert_fruit = input("Enter a fruit to insert: ")
insert_index = int(input(f"At which index to insert (0 to {len(fruits)}): "))
fruits.insert(insert_index, insert_fruit)
print("After insert:", fruits)

# 5. Removing items
remove_fruit = input("\nEnter a fruit to remove from the list: ")
if remove_fruit in fruits:
    fruits.remove(remove_fruit)
    print("After removal:", fruits)
else:
    print(f"{remove_fruit} not found in the list.")

# 6. Popping item
do_pop = input("\nDo you want to pop the last item? (yes/no): ").lower()
if do_pop == "yes":
    popped = fruits.pop()
    print("Popped item:", popped)
    print("After pop:", fruits)

# 7. Slicing example
print("\nSlicing (first 3 fruits):", fruits[:3])

# 8. Modify an item
change_index = int(input(f"\nEnter index to change (0 to {len(fruits)-1}): "))
new_value = input("Enter new fruit name: ")
fruits[change_index] = new_value
print("After changing item:", fruits)

# 9. Check for a fruit
check_fruit = input("\nEnter fruit to check: ")
if check_fruit in fruits:
    print(f"{check_fruit} is in the list.")
else:
    print(f"{check_fruit} is not in the list.")

# 10. Show length
print("\nNumber of fruits in list:", len(fruits))

# 11. Sort and reverse
sort_choice = input("Do you want to sort the list? (yes/no): ").lower()
if sort_choice == "yes":
    fruits.sort()
    print("Sorted list:", fruits)

reverse_choice = input("Do you want to reverse the list? (yes/no): ").lower()
if reverse_choice == "yes":
    fruits.reverse()
    print("Reversed list:", fruits)

# 12. Count and find index
count_item = input("\nEnter fruit to count: ")
print(f"Count of '{count_item}':", fruits.count(count_item))

index_item = input("Enter fruit to find index: ")
if index_item in fruits:
    print(f"Index of '{index_item}':", fruits.index(index_item))
else:
    print(f"'{index_item}' not found in the list.")

# 13. Clear list
clear_choice = input("\nDo you want to clear the list? (yes/no): ").lower()
if clear_choice == "yes":
    fruits.clear()
    print("List cleared:", fruits)
else:
    print("Final list:", fruits)
