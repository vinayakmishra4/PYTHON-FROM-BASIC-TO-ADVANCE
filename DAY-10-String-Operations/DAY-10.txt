String Slicing:-

Slicing is a way to extract a subset of characters from a string. It is done by specifying
the start and end index of the subset of characters you want to extract.

The general syntax for slicing a string is:-
string[start_index:end_index]

where start_index is the index of the first character you want to extract and end_index is the index
of the last character you want to extract.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
🎯 **String Operations in Python** 🎯  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Python offers a variety of powerful tools to work with strings. Here's a beautifully organized guide to the most useful string operations:

---

🔗 **1. Concatenation (`+`)**  
Join two or more strings together.
```python
str1 = "Hello"
str2 = "World"
print(str1 + str2)  # Output: HelloWorld
```

🌀 **2. Repetition (`*`)**  
Repeat a string multiple times.
```python
str = "Hello"
print(str * 3)  # Output: HelloHelloHello
```

🔍 **3. Membership (`in`)**  
Check if a substring exists within a string.
```python
str = "Hello World"
print("World" in str)   # Output: True
print("Python" in str)  # Output: False
```

📏 **4. Length (`len()`)**  
Get the number of characters in a string.
```python
str = "Hello World"
print(len(str))  # Output: 11
```

🔡 **5. Case Conversion (`lower()`, `upper()`)**  
Convert a string to lowercase or uppercase.
```python
str = "Hello World"
print(str.lower())  # Output: hello world
print(str.upper())  # Output: HELLO WORLD
```

🧵 **6. Split (`split()`)**  
Split a string into a list of words.
```python
str = "Hello World"
print(str.split())  # Output: ['Hello', 'World']
```

🧹 **7. Strip (`strip()`)**  
Remove leading and trailing whitespace.
```python
str = "   Hello World   "
print(str.strip())  # Output: Hello World
```

🧩 **8. Replace (`replace()`)**  
Replace parts of a string with another string.
```python
str = "Hello World"
print(str.replace("World", "Python"))  # Output: Hello Python
```

🔎 **9. Find (`find()`)**  
Find the index of the first occurrence of a substring.
```python
str = "Hello World"
print(str.find("World"))  # Output: 6
```

🪢 **10. Join (`join()`)**  
Join iterable elements into a single string.
```python
words = ["Hello", "World"]
print(" ".join(words))  # Output: Hello World
```

🔢 **11. Count (`count()`)**  
Count occurrences of a substring.
```python
str = "Hello Hello World"
print(str.count("Hello"))  # Output: 2
```

🚦 **12. Start/End Check (`startswith()`, `endswith()`)**  
Check how a string begins or ends.
```python
str = "Hello World"
print(str.startswith("Hello"))  # Output: True
print(str.endswith("World"))    # Output: True
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✨ Now you're equipped to slice, dice, and style your strings like a pro!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
