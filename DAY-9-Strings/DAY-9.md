<------------------------------------------------PYTHON DAY-9----------------------------------------------->
📘 Day 9: Strings in Python
---

🔤 **What is a String?**
A **string** in Python is a *sequence of characters* enclosed in *single*, *double*, or *triple* quotes.

Strings can contain letters, numbers, symbols, and even whitespace. They are commonly used to store text data such as names, messages, or any sequence of characters.

**📌 Examples:**
```python
str1 = 'Hello'
str2 = "World"
str3 = '''Triple quoted string'''
```

🔒 **Immutability of Strings**
Strings in Python are immutable — you cannot change their content after creation:

```python
text = "Hello"
# text[0] = 'h'  # ❌ This will raise an error
```

Because strings are immutable, any operation that modifies a string actually creates a new string. For example, using string concatenation or methods like `.replace()` will return a new string instead of altering the original one.

🧠 **Summary**
Strings are immutable sequences of characters.

You can access them via indexing and slicing.

Python provides a wide range of built-in string methods.

Use formatting techniques for cleaner outputs.

Common string methods include:
- **`.lower()`** and **`.upper()`** for changing case
- **`.strip()`** for removing whitespace
- **`.replace()`** for substituting characters
- **`.find()`** and **`.index()`** for searching
- **`.split()`** and **`.join()`** for splitting and combining strings

You can also use escape sequences like `\n` for new lines or `\t` for tabs within strings.
