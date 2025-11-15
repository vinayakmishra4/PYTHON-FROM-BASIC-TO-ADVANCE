# Constructor Example in Python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Creating an object of Person
p1 = Person("Alice", 30)
p1.display()
