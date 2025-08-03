# Python Variables and Data Types (Day 5)

## 📦 Variables in Python
---------------------
- A variable is a container for storing data values.
- Python variables do not need explicit declaration to reserve memory space.
- The declaration happens automatically when you assign a value to a variable.

### 🧾 Rules for Python Variables
---------------------
- A variable name must start with a letter or the underscore character.
- A variable name cannot start with a number.
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
- Variable names are case-sensitive (age, Age and AGE are three different variables).

## 📝 Variable Assignment
---------------------
```python
x = 5
y = "Hello"
z = 3.14
print(x, y, z)
```

## ➗ Multiple Assignment
---------------------
```python
a, b, c = 1, 2, 3
print(a, b, c)
```

## 🔄 Swapping Variables
---------------------
```python
a, b = b, a
```

## 🔒 Constants
---------------------
- Python does not have built-in constant types, but by convention, uppercase variable names indicate constants:
```python
PI = 3.14
```

## 🧠 Data Types in Python
---------------------
Python has the following built-in data types:

1. int – Whole numbers
   ```python
   x = 10
   print(type(x))  # <class 'int'>
   ```

2. float – Decimal numbers
   ```python
   y = 3.14
   print(type(y))  # <class 'float'>
   ```

3. str – Strings (text)
   ```python
   name = "Alice"
   print(type(name))  # <class 'str'>
   ```

4. bool – Boolean values
    ```python
   is_active = True
   print(type(is_active))  # <class 'bool'>
   ```

5. list – Ordered, mutable collection
   ```python
   items = [1, 2, 3]
   print(type(items))  # <class 'list'>
   ```

6. tuple – Ordered, immutable collection
   ```python
   coords = (4, 5)
   print(type(coords))  # <class 'tuple'>
   ```

7. dict – Key-value pairs
   ```python
   person = {"name": "Bob", "age": 30}
   print(type(person))  # <class 'dict'>
   ```

8. set – Unordered collection of unique items
   ```python
   unique_values = {1, 2, 2, 3}
   print(type(unique_values))  # <class 'set'>
   ```

9. NoneType – Represents absence of value
   ```python
   result = None
   print(type(result))  # <class 'NoneType'>
   ```

## 🔍 Type Checking
---------------------
- Use type() function to check the data type of a variable.
- Use isinstance() to check if a variable is of a specific type.
```python
print(type(x))  # <class 'int'>
print(isinstance(x, int))  # True
```

## 🔧 Type Conversion
---------------------
- Convert between data types using `int()`, `float()`, `str()`, etc.
```python
a = "123"
b = int(a)
print(b, type(b))  # 123 <class 'int'>
```

---