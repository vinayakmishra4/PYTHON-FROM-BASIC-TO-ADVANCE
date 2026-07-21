# 🐍 Dunder Methods (`__dunder__`) in Python

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Topic](https://img.shields.io/badge/Topic-Dunder%20Methods-success?style=for-the-badge)
![Level](https://img.shields.io/badge/Level-Beginner%20to%20Advanced-orange?style=for-the-badge)
![OOP](https://img.shields.io/badge/Python-OOP-red?style=for-the-badge)

**Master Python's Special (Magic) Methods and make your custom classes behave like built-in Python objects.**

</div>

---

# 📖 Overview

**Dunder Methods** (short for **Double Underscore Methods**) are special methods in Python that begin and end with double underscores (`__`). They are also known as **Magic Methods** or **Special Methods**.

These methods are automatically invoked by the Python interpreter whenever specific operations are performed on an object, allowing custom classes to integrate seamlessly with Python's built-in features.

By implementing Dunder Methods, you can define how your objects behave during operations such as object creation, printing, comparison, arithmetic, iteration, indexing, and much more.

---

# 🎯 Learning Objectives

After completing this topic, you will be able to:

- Understand what Dunder Methods are.
- Learn why Python uses special methods.
- Customize object behavior.
- Perform operator overloading.
- Create Pythonic and reusable classes.
- Work with built-in Python functions using custom objects.
- Build advanced object-oriented applications.

---

# 📝 Syntax

A Dunder Method always follows the same naming convention:

- Starts with double underscores (`__`)
- Ends with double underscores (`__`)
- Contains a predefined method name recognized by Python

Some common examples include:

- `__init__()`
- `__str__()`
- `__repr__()`
- `__len__()`
- `__add__()`
- `__eq__()`
- `__call__()`

---

# 🌟 Features

- Built into the Python language.
- Automatically executed by the Python interpreter.
- Allow custom classes to behave like built-in objects.
- Support operator overloading.
- Customize object representation.
- Improve object-oriented programming.
- Work with built-in functions like `print()` and `len()`.
- Support iteration, indexing, slicing, and comparisons.
- Improve code readability and maintainability.
- Encourage Pythonic programming practices.

---

# 🚀 Benefits

- Makes custom classes powerful and reusable.
- Enables operator overloading.
- Produces meaningful object representations.
- Integrates with Python's built-in functions.
- Supports iterable and callable objects.
- Allows custom comparison logic.
- Makes programs cleaner and easier to maintain.
- Improves software design using object-oriented principles.

---

# 🏷️ Types of Dunder Methods

## 1️⃣ Object Initialization Methods

| Method | Purpose |
|---------|----------|
| `__new__()` | Creates a new object |
| `__init__()` | Initializes object attributes |
| `__del__()` | Executes before object destruction |

---

## 2️⃣ String Representation Methods

| Method | Purpose |
|---------|----------|
| `__str__()` | User-friendly representation |
| `__repr__()` | Developer-friendly representation |
| `__format__()` | Custom formatting |
| `__bytes__()` | Byte representation |

---

## 3️⃣ Arithmetic Methods

| Operator | Dunder Method |
|-----------|---------------|
| `+` | `__add__()` |
| `-` | `__sub__()` |
| `*` | `__mul__()` |
| `/` | `__truediv__()` |
| `//` | `__floordiv__()` |
| `%` | `__mod__()` |
| `**` | `__pow__()` |

---

## 4️⃣ Comparison Methods

| Operator | Dunder Method |
|-----------|---------------|
| `==` | `__eq__()` |
| `!=` | `__ne__()` |
| `<` | `__lt__()` |
| `<=` | `__le__()` |
| `>` | `__gt__()` |
| `>=` | `__ge__()` |

---

## 5️⃣ Container Methods

| Method | Purpose |
|---------|----------|
| `__len__()` | Returns object length |
| `__getitem__()` | Retrieves an item |
| `__setitem__()` | Updates an item |
| `__delitem__()` | Deletes an item |
| `__contains__()` | Membership testing |

---

## 6️⃣ Iterator Methods

| Method | Purpose |
|---------|----------|
| `__iter__()` | Returns an iterator |
| `__next__()` | Returns the next element |

---

## 7️⃣ Callable Method

| Method | Purpose |
|---------|----------|
| `__call__()` | Makes an object callable like a function |

---

## 8️⃣ Context Manager Methods

| Method | Purpose |
|---------|----------|
| `__enter__()` | Executes when entering a context |
| `__exit__()` | Executes when leaving a context |

---

## 9️⃣ Attribute Access Methods

| Method | Purpose |
|---------|----------|
| `__getattr__()` | Handles missing attributes |
| `__getattribute__()` | Handles every attribute access |
| `__setattr__()` | Handles attribute assignment |
| `__delattr__()` | Handles attribute deletion |

---

# ⭐ Commonly Used Dunder Methods

| Method | Description |
|----------|-------------|
| `__init__()` | Constructor |
| `__new__()` | Creates an object |
| `__del__()` | Destructor |
| `__str__()` | String representation |
| `__repr__()` | Official representation |
| `__len__()` | Returns object length |
| `__add__()` | Addition |
| `__sub__()` | Subtraction |
| `__mul__()` | Multiplication |
| `__truediv__()` | Division |
| `__eq__()` | Equality comparison |
| `__lt__()` | Less-than comparison |
| `__gt__()` | Greater-than comparison |
| `__getitem__()` | Item access |
| `__setitem__()` | Item assignment |
| `__contains__()` | Membership testing |
| `__iter__()` | Iterator |
| `__next__()` | Next element |
| `__call__()` | Callable object |
| `__enter__()` | Context manager entry |
| `__exit__()` | Context manager exit |

---

# 📂 Example Program

The repository includes a comprehensive Python program demonstrating multiple Dunder Methods, including:

- Object Initialization (`__init__()`)
- String Representation (`__str__()`)
- Length (`__len__()`)
- Addition (`__add__()`)
- Comparison (`__gt__()`)
- Callable Objects (`__call__()`)
- Container Access (`__getitem__()`)

🔗 **Source Code:**  
**[Day 62 – Dunder Methods (Python Program)](https://github.com/vinayakmishra4/PYTHON-FROM-BASIC-TO-ADVANCE/blob/main/DAY-62-Dunder/Day-62-Dunder.py)**

---

# 🎯 Applications

Dunder Methods are widely used in:

- Object-Oriented Programming (OOP)
- Custom Data Structures
- Python Libraries and Frameworks
- Scientific Computing
- Machine Learning
- Data Science
- API Development
- Automation
- Game Development

---

# 📚 Key Takeaways

- Dunder Methods are Python's **special methods**.
- They are automatically invoked by the interpreter.
- They allow custom classes to behave like built-in Python objects.
- They enable operator overloading and object customization.
- Understanding Dunder Methods is essential for writing professional, Pythonic, and maintainable object-oriented code.

---

<div align="center">

### ⭐ If you found this repository helpful, don't forget to **Star** it!

**Happy Learning! 🚀**

</div>
