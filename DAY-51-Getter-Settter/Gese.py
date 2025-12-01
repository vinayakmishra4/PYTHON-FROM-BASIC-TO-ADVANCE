class Person:
    def __init__(self, name, age):
        self.__name = name      # private attribute
        self.__age = age        # private attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        if name.strip():
            self.__name = name
        else:
            print("Name cannot be empty.")

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be a positive number.")

# ----------------------------
# Using the class
# ----------------------------
person = Person("Alice", 25)

print("Name:", person.get_name())
print("Age:", person.get_age())

person.set_name("Bob")
person.set_age(30)

print("Updated Name:", person.get_name())
print("Updated Age:", person.get_age())
