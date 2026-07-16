# Super Keyword: Super Keyword is used to call the parent class constructor

class Parent:
    def __init__(self):
        print("This is Parent class constructor")
    

class Child(Parent):
    def __init__(self):
        super().__init__()  # Calling the parent class constructor

# Creating an object of Child class
child_object = Child()
