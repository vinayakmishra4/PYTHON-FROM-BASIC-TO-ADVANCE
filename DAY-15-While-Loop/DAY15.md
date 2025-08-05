# 🌟 **Day 15: While Loop Statement** 🌟

---

## 📌 What is a **While Loop**?

A **while loop** lets you **repeat a block of code** as long as a **condition** is true.

It’s like saying:

> *"Keep doing this until something changes."*

---

## 🧩 Syntax

```python
while condition:
    # code to repeat
```

* The loop **checks the condition first**.
* If **True**, it runs the code inside.
* When condition becomes **False**, it stops.

---

## 🔥 Example

```python
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1
```

**Output:**

```
Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5
```

---

## 💡 Important Tips

* Always **update variables** inside the loop to avoid infinite loops!
* Infinite loops run forever — be cautious!

**Example of infinite loop:**

```python
while True:
    print("This runs endlessly!")
```

---

## 🚀 Why Use While Loops?

* Repeat tasks until a condition changes.
* Wait for user input or external events.
* Process data until no more remains.

---