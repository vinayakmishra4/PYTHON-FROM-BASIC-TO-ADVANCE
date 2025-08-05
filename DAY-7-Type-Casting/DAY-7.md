## 🧠 **Typecasting in Python**

---

### 🔄 What is Typecasting?

Typecasting is the process of converting the **data type of a value** into **another data type**. It allows us to perform operations between different data types by converting them into a common one.

---

### 📌 **Why is Typecasting Important?**

* To perform operations on mixed data types
* To avoid errors during operations
* To format values for output or storage
* To manage memory efficiently

---

## 🔸 **Types of Typecasting in Python**

Python provides **two types** of typecasting:

---

### ✅ 1. **Implicit Typecasting** (Automatic)

* Python automatically converts **smaller data types to larger data types** to avoid data loss.
* No need for user intervention.

#### 🔹 Example:

```python
a = 10       # Integer
b = 3.5      # Float
c = a + b    # Result will be float

print(c)     # Output: 13.5
print(type(c))  # Output: <class 'float'>
```

> 🧠 Python converted `int` to `float` automatically — this is *implicit typecasting*.

---

### ✍️ 2. **Explicit Typecasting** (Manual)

* The user manually converts one data type into another using built-in functions.
* Syntax: `datatype(value)`

#### 🔹 Common Functions:

* `int()` → Converts to integer
* `float()` → Converts to float
* `str()` → Converts to string
* `bool()` → Converts to boolean
* `list()`, `tuple()`, `set()`, etc.

#### 🔹 Example:

```python
x = "100"
y = int(x)     # Converting string to int
z = float(y)   # Converting int to float

print(y + 50)  # Output: 150
print(z + 0.5) # Output: 100.5
```

> 🔧 Here, we manually cast `str` → `int` → `float`.

---

## ⚠️ Things to Remember

* Not all conversions are valid (e.g., `"abc"` to `int` will raise an error)
* Explicit typecasting should be used carefully to avoid **data loss** or **errors**
* Always verify data types with `type()` function

---

### 🧪 Quick Practice:

Try converting the following values:

```python
a = "123"
b = 45.67
c = True

# Convert and print their types
```

---

### 🚀 Summary:

| Type         | Performed By | Safe?              | Example                |
| ------------ | ------------ | ------------------ | ---------------------- |
| **Implicit** | Python       | ✅ Yes              | `int + float` → float  |
| **Explicit** | Developer    | ⚠️ Sometimes risky | `str(100)`, `int("5")` |