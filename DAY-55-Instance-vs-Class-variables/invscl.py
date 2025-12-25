class Student:
    # Class variable (shared by all objects)
    school_name = "Greenwood High"

    def __init__(self, name, age):
        # Instance variables (unique to each object)
        self.name = name
        self.age = age

    def display_info(self):
        print("\nStudent Details")
        print("Name   :", self.name)
        print("Age    :", self.age)
        print("School :", Student.school_name)

# Input for first student
name1 = input("Enter name of first student: ")
age1 = int(input("Enter age of first student: "))

student1 = Student(name1, age1)

# Input for second student
name2 = input("\nEnter name of second student: ")
age2 = int(input("Enter age of second student: "))

student2 = Student(name2, age2)

