def multiply(*args):
    product = 1
    for num in args:
        product *= num
    return product

def describe_person(**kwargs):
    print("Person details:")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

def power(base, exponent=2):
    return base ** exponent


# Testing the functions
print("Multiply:", multiply(2, 3, 4))   # Output: 24
print("Multiply:", multiply(5, 10))     # Output: 50
print("Multiply:", multiply())          # Output: 1

describe_person(name="John", age=34, city="London")

print("Power:", power(3))       # Output: 9
print("Power:", power(2, 3))    # Output: 8
print("Power:", power(5, 1))    # Output: 5