# Python Program to Demonstrate Different Types of Inheritance with User Input

# --------------------------
# 1. Single Inheritance
# --------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


# --------------------------
# 2. Multiple Inheritance
# --------------------------
class Flyer:
    def fly(self):
        return "I can fly!"


class Swimmer:
    def swim(self):
        return "I can swim!"


class Duck(Flyer, Swimmer):
    def __init__(self, name):
        self.name = name

    def abilities(self):
        return f"{self.name}: {self.fly()} and {self.swim()}"


# --------------------------
# 3. Multilevel Inheritance
# --------------------------
class Vehicle:
    def vehicle_type(self):
        return "Generic Vehicle"


class Car(Vehicle):
    def vehicle_type(self):
        return "Car"


class ElectricCar(Car):
    def vehicle_type(self):
        return "Electric Car"


# --------------------------
# 4. Hierarchical Inheritance
# --------------------------
class Shape:
    def area_info(self):
        return "Calculating area..."


class Square(Shape):
    def area_info(self):
        return "Area = side * side"


class Circle(Shape):
    def area_info(self):
        return "Area = pi * r^2"


# --------------------------
# Program Execution with User Input
# --------------------------

def single_inheritance_demo():
    name = input("\nEnter the name of an animal: ")
    dog = Dog(name)
    print(dog.speak())


def multiple_inheritance_demo():
    name = input("\nEnter the name of a duck: ")
    duck = Duck(name)
    print(duck.abilities())


def multilevel_inheritance_demo():
    vehicle_choice = input("\nEnter vehicle type (Vehicle/Car/ElectricCar): ").strip().lower()
    if vehicle_choice == "vehicle":
        v = Vehicle()
    elif vehicle_choice == "car":
        v = Car()
    else:
        v = ElectricCar()
    print(v.vehicle_type())


def hierarchical_inheritance_demo():
    shape_choice = input("\nEnter shape (Square/Circle): ").strip().lower()
    if shape_choice == "square":
        s = Square()
    else:
        s = Circle()
    print(s.area_info())


# --------------------------
# Main Program
# --------------------------
if __name__ == "__main__":
    print("Python Inheritance Demo Program")

    single_inheritance_demo()
    multiple_inheritance_demo()
    multilevel_inheritance_demo()
    hierarchical_inheritance_demo()
