# 🐍 Day 13: Match Case Statements in Python

Match Case Statements were introduced in **Python 3.10**. They work similarly to `switch` statements in other languages and allow for cleaner conditional logic.

> ⚠️ Make sure you're using **Python 3.10+**

---

## ✅ What is `match-case`?

The `match-case` statement allows pattern matching—comparing a value against one or more patterns and executing code based on the match.

---

## 🧠 Syntax

```python
match variable:
    case pattern1:
        # Code block
    case pattern2:
        # Code block
    case _:
        # Default case (like 'else')
````
---

## 📘 Example 1: Basic Match

```python
command = "start"

match command:
    case "start":
        print("System is starting...")
    case "stop":
        print("System is stopping...")
    case "pause":
        print("System is paused.")
    case _:
        print("Unknown command")
```

**Output:** `System is starting...`

---

## ⚠️ Notes

* `case _:` acts like a default case.
* Python checks the cases **top to bottom**, so order matters.
* You can use `case x if condition:` for more control.

---