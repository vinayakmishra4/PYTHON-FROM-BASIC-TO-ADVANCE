# 📘 **DAY 11: If-Else Statements in Python**

---

## 🧠 **What is an If-Else Statement?**

In Python, an **if-else statement** is a way to allow your program to make **decisions**. It checks whether a condition is **True** or **False** and then **executes** different blocks of code based on the result.

Think of it like asking:

> "If this condition is true, do this. Otherwise, do something else."

---

## 🧩 **Why Use If-Else?**

* To **control the flow** of your program.
* To handle **different outcomes** (like user input, conditions, etc.).
* To make your program **smart and interactive**.

---

## 🔤 **Syntax of If-Else in Python**

```python
if condition:
    # code to run if condition is true
elif another_condition:
    # code to run if the above is false but this is true
else:
    # code to run if all conditions are false
```

> 🔔 Python uses **indentation** (spaces/tabs) to define blocks of code.

---

## 🔹 **1. Simple If Statement**

```python
age = 20

if age >= 18:
    print("You are an adult.")
```

✅ If the condition is true (`age >= 18`), the message is printed.

---

## 🔹 **2. If-Else Statement**

```python
age = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")
```

✔️ If the condition is **false**, the `else` part runs.

---

## 🔹 **3. If-Elif-Else Statement**

```python
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")
```

📌 Python checks each condition **in order**, and runs the first `True` block it finds.

---

## 🔹 **4. Nested If**

```python
num = 10

if num > 0:
    if num % 2 == 0:
        print("Positive and even")
    else:
        print("Positive but odd")
else:
    print("Not positive")
```

🧩 You can place `if` statements **inside another if** block for more detailed checks.

---

## 🔹 **5. Shorthand If (One-liner)**

```python
x = 10
y = 20

if x < y: print("x is less than y")
```

### Shorthand if-else:

```python
print("x") if x > y else print("y")
```

---

## ⚙️ Logical Operators with If

You can combine conditions using:

* `and` → both must be True
* `or` → at least one must be True
* `not` → reverses the result

```python
a = 5
b = 10

if a < b and b < 20:
    print("Both conditions are True")
```

## ✅ Summary

| Concept      | Description                                   |
| ------------ | --------------------------------------------- |
| `if`         | Checks a condition                            |
| `elif`       | Checks another condition if previous is false |
| `else`       | Runs if no condition is True                  |
| `and/or/not` | Combine multiple conditions                   |
| Indentation  | Must use spacing correctly (usually 4 spaces) |

---

Would you like the **solutions** to the practice problems or a **PDF** version of this lesson?
