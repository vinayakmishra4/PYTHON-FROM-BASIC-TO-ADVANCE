# DAY 30 - Dictionaries with Input

# 1. Create a dictionary using input
student = {}
student["name"] = input("Enter student name: ")
student["age"] = int(input("Enter student age: "))
courses = input("Enter courses (separated by commas): ")
student["courses"] = courses.split(",")   # convert string into list

print("\nStudent dictionary created:", student)

# 2. Add more information
student["grade"] = input("Enter grade: ")

print("\nUpdated dictionary:", student)

# 3. Remove a course
remove_course = input("Enter a course to remove: ")
if remove_course in student["courses"]:
    student["courses"].remove(remove_course)
    print(f"Removed course: {remove_course}")
else:
    print(f"Course '{remove_course}' not found!")

print("After course removal:", student)

# 4. Looping through dictionary
print("\nLooping through dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")

# 5. Nested dictionaries with input
classroom = {}
n = int(input("\nHow many students in classroom? "))

for i in range(1, n+1):
    name = input(f"Enter name of student {i}: ")
    age = int(input(f"Enter age of {name}: "))
    classroom[f"student{i}"] = {"name": name, "age": age}

print("\nClassroom dictionary:", classroom)

# 6. Dictionary comprehension with input
limit = int(input("\nEnter a number to generate squares dictionary: "))
squares = {x: x**2 for x in range(1, limit+1)}
print("Squares dictionary:", squares)