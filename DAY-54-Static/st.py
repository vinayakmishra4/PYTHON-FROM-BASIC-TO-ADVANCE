class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b


# Taking input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calling static methods using class name
print("Addition:", Calculator.add(num1, num2))
print("Subtraction:", Calculator.subtract(num1, num2))
