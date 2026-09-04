# Single Inheritance


# Parent class
class Animal:
    def eat(self):
        print("Animal eats food")


# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")


# Creating object of child class
d = Dog()

d.eat()   # Inherited from Animal
d.bark()  # Dog's own method