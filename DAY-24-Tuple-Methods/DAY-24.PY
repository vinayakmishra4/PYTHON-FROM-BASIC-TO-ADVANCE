# Day 24: Tuple Methods & Operations with User Input

# 1️⃣ Create a tuple from user input
user_input = input("Enter elements of a tuple separated by commas: ")
# Split input string and convert to tuple
user_tuple = tuple(user_input.split(','))

print("\nYour tuple:", user_tuple)
print("-" * 50)

# 2️⃣ Using tuple methods

# count() - ask user which element to count
element_to_count = input("Enter an element to count in the tuple: ")
count_result = user_tuple.count(element_to_count)
print(f"'{element_to_count}' occurs {count_result} times in your tuple")

# index() - ask user which element to find
element_to_index = input("Enter an element to find its first index: ")
if element_to_index in user_tuple:
    index_result = user_tuple.index(element_to_index)
    print(f"First occurrence of '{element_to_index}' is at index {index_result}")
else:
    print(f"'{element_to_index}' is not in the tuple")
print("-" * 50)

# 3️⃣ Tuple operations

# Concatenation - add more elements via input
additional_input = input("Enter additional elements to concatenate (comma separated): ")
additional_tuple = tuple(additional_input.split(','))
concatenated = user_tuple + additional_tuple
print("Concatenated tuple:", concatenated)

# Repetition - ask how many times to repeat
repeat_count = int(input("How many times do you want to repeat your tuple? "))
repeated_tuple = user_tuple * repeat_count
print("Repeated tuple:", repeated_tuple)

# Membership check
check_element = input("Enter an element to check if it's in the tuple: ")
print(f"Is '{check_element}' in the tuple?", check_element in user_tuple)

# Slicing - ask start and end indices
start_index = int(input("Enter start index for slicing: "))
end_index = int(input("Enter end index for slicing: "))
sliced_tuple = user_tuple[start_index:end_index]
print(f"Sliced tuple ({start_index}:{end_index}):", sliced_tuple)

# Length
print("Length of your tuple:", len(user_tuple))

# Conversion to list
tuple_as_list = list(user_tuple)
print("Tuple converted to list:", tuple_as_list)

# Conversion to set
tuple_as_set = set(user_tuple)
print("Tuple converted to set (unique elements):", tuple_as_set)