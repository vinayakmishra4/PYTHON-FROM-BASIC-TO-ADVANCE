# Method Overriding in Python Using User Input

class Person:
    def introduce(self, name):
        print(f"\nHello {name}!")
        print("Welcome to our application.")

class Student(Person):
    def introduce(self, name):
        print(f"\nHello {name}!")
        print("Welcome to the Python Course.")
        print("You are accessing the Student Portal.")

# Taking user input
name = input("Enter your name: ")

# Creating object of Child class
obj = Student()

# Calling overridden method
obj.introduce(name)