# 🧬 Single Inheritance in Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-Single%20Inheritance-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/OOP-Concept-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Level-Beginner-orange?style=for-the-badge" />
</p>

---

# 📖 Introduction

**Single Inheritance** is the simplest form of inheritance in Python. It allows a **single child class** to inherit the attributes and methods of **one parent class**. This promotes code reusability, reduces duplication, and helps organize programs using Object-Oriented Programming (OOP).

---

# 🎯 Definition

> **Single Inheritance** is a type of inheritance in which **one child (derived) class inherits the properties and methods of one parent (base) class**.

It establishes an **"is-a"** relationship between the parent and child classes.

---

# 🏗️ Syntax

```python
class ParentClass:
    # Parent class attributes and methods
    pass


class ChildClass(ParentClass):
    # Additional attributes and methods
    pass
```

---

# 🔄 Working of Single Inheritance

1. Create a **Parent Class** with common attributes and methods.
2. Create a **Child Class** by passing the parent class name inside parentheses.
3. The child class automatically inherits all accessible members of the parent class.
4. The child class can also define its own attributes and methods or override inherited methods.

---

# ✨ Features of Single Inheritance

## 🔹 One Parent, One Child
A single child class inherits from only one parent class.

---

## 🔹 Code Reusability
Common functionality is written once in the parent class and reused by the child class.

---

## 🔹 Easy to Understand
The class hierarchy is simple, making the code easy to read and maintain.

---

## 🔹 Method Inheritance
The child class automatically inherits public methods and attributes from the parent class.

---

## 🔹 Method Overriding
The child class can redefine inherited methods to provide specialized behavior.

---

## 🔹 Extensible Design
New functionality can be added in the child class without modifying the parent class.

---

# 🌟 Benefits of Single Inheritance

| ✅ Benefit | 📖 Description |
|------------|----------------|
| ♻️ Code Reusability | Reuse existing code without rewriting it. |
| 🧹 Reduced Code Duplication | Common code is written only once. |
| 🚀 Faster Development | Build applications more efficiently. |
| 📚 Better Readability | Maintains a simple and organized class structure. |
| 🔧 Easy Maintenance | Changes in the parent class can benefit the child class. |
| 📈 Scalability | Easy to extend applications by creating new child classes. |
| 🎯 Better Organization | Separates common functionality from specialized functionality. |
| 💼 Real-World Modeling | Represents simple "is-a" relationships effectively. |

---

# 📌 Key Characteristics

- Only **one parent class** is involved.
- Only **one child class** inherits from the parent.
- Supports **code reuse** and **modularity**.
- Child class can access the parent's public members.
- Child class can add new features or override inherited methods.

---

# 🎯 When to Use Single Inheritance

Use Single Inheritance when:

- A class is a specialized version of another class.
- Multiple classes do not need to inherit from multiple parents.
- You want a simple and clear inheritance hierarchy.
- Code reuse is required without increasing complexity.
- Building small to medium-sized object-oriented applications.

---

# 📊 Advantages at a Glance

| Feature | Benefit |
|---------|---------|
| One Parent Class | Simple hierarchy |
| Code Reusability | Less duplicate code |
| Easy Maintenance | Centralized updates |
| Better Readability | Clean and organized structure |
| Extensibility | Add new features easily |
| Faster Development | Saves coding time |

---

# 📝 Summary

**Single Inheritance** is the most basic type of inheritance in Python, where **one child class inherits from one parent class**. It helps developers reuse code, reduce redundancy, improve maintainability, and create a simple, organized class hierarchy. It is ideal for modeling straightforward parent-child relationships in object-oriented programming.

---

<div align="center">

### 🌟 *One Parent ➜ One Child = Single Inheritance*

🚀 **Single Inheritance is the foundation of Object-Oriented Programming in Python.**

</div>