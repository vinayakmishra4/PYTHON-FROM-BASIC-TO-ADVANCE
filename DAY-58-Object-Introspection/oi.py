


# 🐍 Object Introspection Examples in Python

# Example object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}!"

# Create an instance
person = Person("Alice", 30)

# 1. Type checking
print("1. Type Checking:")
print(f"Type of person: {type(person)}")
print(f"Is 'person' an instance of Person? {isinstance(person, Person)}")
print("-" * 50)

# 2. Attribute and method discovery
print("2. Attributes and Methods:")
print(f"All attributes and methods of person: {dir(person)}")
print("-" * 50)

# 3. Check for existence of attribute/method
print("3. Check Existence:")
print(f"Does person have attribute 'name'? {hasattr(person, 'name')}")
print(f"Does person have method 'greet'? {hasattr(person, 'greet')}")
print("-" * 50)

# 4. Get attribute dynamically
print("4. Get Attribute Dynamically:")
name_value = getattr(person, 'name')
print(f"Value of 'name' attribute: {name_value}")
print("-" * 50)

# 5. Dynamic method invocation
print("5. Dynamic Method Invocation:")
greet_method = getattr(person, 'greet')
print(greet_method())
print("-" * 50)

# 6. Introspecting class attributes
print("6. Class Attributes:")
print(f"Class dictionary: {Person.__dict__}")
print(f"Class name: {Person.__name__}")
print(f"Class bases: {Person.__bases__}")
print("-" * 50)

# 7. Summary
print("✅ Object introspection allows checking type, attributes, methods, and dynamic interactions at runtime.")