# 🚀 DAY 16: Break and Continue Statements

Welcome to **Day 16** of your programming journey! Today, we focus on mastering two crucial control flow tools that can dramatically improve how you work with loops: the `break` and `continue` statements.

---

## 📘 Overview

In any programming language, loops are used to repeat a block of code multiple times. But what if you need to **exit a loop early** or **skip certain iterations**? That’s where `break` and `continue` come into play.

* ✅ `break` — Exits the loop entirely when a specific condition is met.
* 🔁 `continue` — Skips the rest of the current iteration and moves to the next cycle of the loop.

These simple but powerful tools help you write more efficient, readable, and flexible code.

---

## 📚 What You’ll Learn

By the end of Day 16, you’ll be able to:

* Understand the purpose and syntax of `break` and `continue`.
* Use `break` to stop a loop early when a condition is satisfied.
* Use `continue` to skip certain iterations based on a condition.
* Apply these statements in both `for` and `while` loops.
* Avoid common mistakes and write clean loop control logic.
* Use `break` and `continue` effectively in nested loops.

---

## 🧠 Key Concepts

### 🔹 `break` Statement

* Immediately exits the loop.
* Commonly used when a condition is met, like finding an element.

```python
for number in range(10):
    if number == 5:
        break
    print(number)
# Output: 0 1 2 3 4
```

### 🔹 `continue` Statement

* Skips the current loop iteration and moves to the next one.
* Useful for ignoring certain values during iteration.

```python
for number in range(10):
    if number % 2 == 0:
        continue
    print(number)
# Output: 1 3 5 7 9
```

---

## 🔍 Real-World Examples

* Stopping a password attempt loop after 3 failed tries.
* Skipping invalid entries in a dataset during processing.
* Exiting a search loop once a match is found.
* Ignoring null or empty values in a user input list.

---


## ✅ Summary

| Statement  | Function                           | When to Use                             |
| ---------- | ---------------------------------- | --------------------------------------- |
| `break`    | Exits the loop completely          | When a condition is met early           |
| `continue` | Skips current iteration, continues | To ignore certain values during looping |

---

## 💡 Pro Tip

While `break` and `continue` make code more flexible, **avoid overusing them**, as they can sometimes make loops harder to read if misused. Always comment on your logic when using them in complex loops.