# 🐍 Python: `is` vs `=`

## 📘 Overview
In Python, **`is`** and **`=`** are very different.  
While they may sound similar in English, in code they serve **completely different purposes**.

---

## 🔹 `=` → Assignment Operator
**Purpose:** Assign a value to a variable.  
It **does not compare**; it just **stores** a value.

```python
x = 10
name = "Alice"
````

✅ **Meaning:**

* Assign value `10` to variable `x`.
* Assign string `"Alice"` to variable `name`.

---

## 🔹 `is` → Identity Operator

**Purpose:** Check if **two variables refer to the same object in memory**.
It tests **object identity**, **not value equality**.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True  → values are equal
print(a is b)  # False → different objects in memory
```

✅ **Meaning:**

* `==` checks **if the contents are the same**.
* `is` checks **if they are literally the same object**.

---

## ⚖️ Comparison Table

| Operator | Type       | Meaning                  | Example  | Result                 |
| -------- | ---------- | ------------------------ | -------- | ---------------------- |
| `=`      | Assignment | Assigns a value          | `x = 5`  | Assigns 5 to `x`       |
| `==`     | Equality   | Compares values          | `x == 5` | True if equal in value |
| `is`     | Identity   | Compares memory identity | `x is y` | True if same object    |

---

## 🔍 Example

```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x == y)  # True
print(x is y)  # True (same object)

print(x == z)  # True
print(x is z)  # False (different object)
```

---

## 💡 Tips

* Use `=` for **assignment**
* Use `==` for **value comparison**
* Use `is` for **object identity comparison**

```

---