# 🧮 Python Calculator

A simple calculator implemented in Python that supports basic arithmetic operations.

## ✅ Features

This calculator supports the following operations:

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* 🟰 Modulus
* 🧠 Exponentiation
* 🟦 Square Root

## 🛠️ Functions

```python
add(a, b)        # Returns the sum of a and b
subtract(a, b)   # Returns the difference of a and b
multiply(a, b)   # Returns the product of a and b
divide(a, b)     # Returns the quotient of a divided by b; raises an error if b is zero
modulus(a, b)    # Returns the remainder of a divided by b
power(a, b)      # Returns a raised to the power of b
sqrt(a)          # Returns the square root of a
```

## 📦 Example Usage

```python
result = add(10, 5)        # Output: 15
result = subtract(10, 5)   # Output: 5
result = multiply(10, 5)   # Output: 50
result = divide(10, 5)     # Output: 2.0
```

## ⚠️ Notes

* Ensure input values are valid numbers to avoid runtime errors.
* The `divide()` function raises a `ZeroDivisionError` if the second argument is zero.