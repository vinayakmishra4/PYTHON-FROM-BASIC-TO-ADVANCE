class Student:
    def __init__(self, name, marks, roll):
        # Public member
        self.name = name
        
        # Protected member
        self._marks = marks
        
        # Private member
        self.__roll = roll

    # Public method to show all details
    def show_details(self):
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("Marks (Protected):", self._marks)
        print("Roll Number (Private):", self.__roll)


# Taking input from the user
name_input = input("Enter student name: ")
marks_input = input("Enter marks: ")
roll_input = input("Enter roll number: ")

# Creating object with user input
s = Student(name_input, marks_input, roll_input)

# Accessing public member
print("\nAccessing Public Member:")
print("Name =", s.name)

# Accessing protected member
print("\nAccessing Protected Member (Allowed but not recommended):")
print("Marks =", s._marks)

# Accessing private member using name mangling
print("\nAccessing Private Member (Using name mangling):")
print("Roll Number =", s._Student__roll)

# Showing all details
s.show_details()
