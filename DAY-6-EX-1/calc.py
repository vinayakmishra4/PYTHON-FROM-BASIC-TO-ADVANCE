a=int(input())
b=int(input())

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def modulus(a, b):
    return a % b

def exponent(a, b):
    return a ** b

def floor_divide(a, b):
    return a // b

# Example usage
if __name__ == "__main__":
    print("Addition:",a" + ",b,"=", add(a, b))
    print("Subtraction:", a, "-", b, "=", subtract(a, b))
    print("Multiplication:", a, "*", b, "=", multiply(a, b))
    print("Division:", a, "/", b, "=", divide(a, b))
    print("Modulus:", a, "%", b, "=", modulus(a, b))
    print("Exponentiation:", a, "**", b, "=", exponent(a, b))
    print("Floor Division:", a, "//", b, "=", floor_divide(a, b))