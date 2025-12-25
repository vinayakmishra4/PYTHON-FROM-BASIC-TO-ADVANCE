# 📌 Instance Variables vs Class Variables

In object-oriented programming (OOP), **variables** are used to store data inside a class. Based on **where the data belongs and how it is shared**, variables are mainly classified into **instance variables** and **class variables**. Understanding this difference is crucial for writing efficient, clear, and well-designed programs.

---

## 🌱 What Are Variables in OOP?

Variables in OOP represent the **state** of an object or a class.
They help store information that can be accessed and modified during program execution.

---

## 🔹 Instance Variables

### 📖 Definition

Instance variables are variables that belong to a **specific object (instance)** of a class. Each object maintains its **own independent copy** of these variables.

### ⭐ Key Characteristics

* Created when an object is created
* Stored inside each object
* Not shared with other objects
* Changing one object’s instance variable does **not** affect others

### 🎯 Purpose

Instance variables are used to represent **unique, object-specific data**.

### 🧠 Real-World Examples

* Student name and roll number
* Employee ID and salary
* Car color and engine number

---

## 🔸 Class Variables

### 📖 Definition

Class variables are variables that belong to the **class itself**, not to individual objects. A **single shared copy** exists for all instances of the class.

### ⭐ Key Characteristics

* Created when the class is defined
* Shared across all objects
* Common for all instances
* Changes affect every object of the class

### 🎯 Purpose

Class variables are used to represent **common data** shared by all objects.

### 🧠 Real-World Examples

* School name for all students
* Company name for all employees
* Tax rate or interest rate

---

## ⚖️ Instance vs Class Variables (Comparison)

| Aspect           | Instance Variables | Class Variables     |
| ---------------- | ------------------ | ------------------- |
| Belongs to       | Individual object  | Class               |
| Number of copies | One per object     | One shared copy     |
| Data type        | Unique             | Common              |
| Memory usage     | More (per object)  | Less (shared)       |
| Change impact    | Affects one object | Affects all objects |

---

## 🔁 Modification Behavior

### Instance Variables

* Changes apply **only to the object** being modified
* Safe for storing personal or unique data

### Class Variables

* Changes apply to **all existing and future objects**
* Best used for constants or shared information

⚠️ Misusing class variables can cause unexpected changes across all objects.

---

## 🧩 When to Use Each?

### ✅ Use Instance Variables When:

* Data differs from object to object
* Each object must store its own state

### ✅ Use Class Variables When:

* Data is the same for all objects
* A shared value improves consistency and memory efficiency

---

## 📝 Summary

* **Instance variables** → store object-specific information
* **Class variables** → store shared, class-level information
* Proper usage improves **design clarity, performance, and maintainability**

---

## 🎯 Key Takeaway

> **If the data describes the object → use an instance variable.
> If the data describes the class → use a class variable.**

---
