# Input initial list
items = input("Enter items separated by spaces: ").split()
print("Initial list:", items)

# append()
item_to_append = input("Enter an item to append: ")
items.append(item_to_append)
print("After append:", items)

# extend()
items_to_extend = input("Enter multiple items to extend (space separated): ").split()
items.extend(items_to_extend)
print("After extend:", items)

# insert()
index = int(input("Enter index to insert at: "))
item_to_insert = input("Enter item to insert: ")
items.insert(index, item_to_insert)
print("After insert:", items)

# remove()
item_to_remove = input("Enter item to remove: ")
if item_to_remove in items:
    items.remove(item_to_remove)
    print("After remove:", items)
else:
    print(f"'{item_to_remove}' not found in the list.")

# pop()
if items:
    index_to_pop = int(input("Enter index to pop (or -1 for last): "))
    popped = items.pop(index_to_pop if index_to_pop != -1 else -1)
    print(f"Popped item: {popped}")
    print("After pop:", items)
else:
    print("List is empty, cannot pop.")

# index()
item_for_index = input("Enter item to find index: ")
if item_for_index in items:
    print(f"Index of '{item_for_index}':", items.index(item_for_index))
else:
    print(f"'{item_for_index}' not found in list.")

# count()
item_to_count = input("Enter item to count: ")
print(f"Count of '{item_to_count}':", items.count(item_to_count))

# sort()
items.sort()
print("After sort:", items)

# reverse()
items.reverse()
print("After reverse:", items)

# copy()
copied_list = items.copy()
print("Copied list:", copied_list)

# clear()
items.clear()
print("After clear:", items)
