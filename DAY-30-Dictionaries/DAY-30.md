# 🌟 **DAY 30 – Dictionaries**  

---

## 📖 **Definition**  
A **dictionary** in Python is an **ordered, mutable, and dynamic collection** that stores data in **key-value pairs**.  

- 🔑 **Keys** → must be unique & immutable (string, int, tuple).  
- 📦 **Values** → can be any type (string, int, list, dict, etc.).  
- 🧭 Used for **mapping** and **fast lookups**.  

---

## 📝 **Syntax**  
```python
# Empty dictionary
my_dict = {}

# Dictionary with key-value pairs
my_dict = {
    "key1": "value1",
    "key2": "value2"
}
```

---

## 🧑‍💻 **Example**  
```python
# Creating a dictionary
student = {
    "name": "John",
    "age": 21,
    "course": "Python",
    "skills": ["coding", "debugging"]
}

# Access values
print(student["name"])       # John
print(student.get("age"))    # 21

# Update value
student["age"] = 22

# Add new pair
student["city"] = "New York"

# Delete key
del student["course"]

# Iterate through dictionary
for key, value in student.items():
    print(f"{key} : {value}")
```

---

## ✨ **Features**  
✅ Stores data as **key-value pairs**  
✅ **Mutable** → Can be updated  
✅ **Keys = unique & immutable**  
✅ **Values = any type**  
✅ **Insertion-ordered (Python ≥3.7)**  
✅ Supports **nesting** (dictionary inside dictionary)  

---

## 🎯 **Uses**  
- 📊 Represent structured data (like JSON)  
- 🔍 Fast searching/lookup tables  
- 📚 Counting frequencies (word counter)  
- 🧩 Mapping relationships (e.g., ID → info)  

---

## ⚡ **Advantages**  
- 🚀 **Fast lookups** (O(1) on average)  
- 🔧 **Flexible** → mixed keys & values  
- 🏗️ Supports **nested data**  
- 🌍 Useful for **real-world data mapping**  

---

## ⚠️ **Disadvantages**  
- 📂 Consumes **more memory** than lists  
- 🔑 Keys must be **immutable**  
- ❌ Accessing invalid key → `KeyError`  
- 📌 Order preserved only in Python ≥3.7  

---

## 🛠️ **Common Dictionary Methods**  

| Method              | 📝 Description |
|---------------------|----------------|
| `dict.get(key)`     | Returns value for key (or None if not found) |
| `dict.keys()`       | Returns all keys |
| `dict.values()`     | Returns all values |
| `dict.items()`      | Returns key-value pairs as tuples |
| `dict.update({...})`| Updates with new values |
| `dict.pop(key)`     | Removes key-value pair |
| `dict.clear()`      | Removes all items |
| `dict.copy()`       | Returns a shallow copy |
| `dict.setdefault()` | Returns value if key exists, else adds it |

---

## 🔄 Difference: List vs Tuple vs Set vs Dictionary  

| Feature        | List (📋) | Tuple (📦) | Set (🌀) | Dictionary (📖) |
|----------------|-----------|------------|----------|-----------------|
| **Syntax**     | `[ ]`     | `( )`      | `{ }`    | `{key: value}` |
| **Mutable**    | ✅ Yes    | ❌ No      | ✅ Yes   | ✅ Yes |
| **Ordered**    | ✅ Yes    | ✅ Yes     | ❌ No    | ✅ (Python ≥3.7) |
| **Duplicates** | ✅ Allowed| ✅ Allowed | ❌ Not allowed | ❌ Keys not allowed (values can repeat) |
| **Indexing**   | ✅ Yes    | ✅ Yes     | ❌ No    | ✅ By key |
| **Use Case**   | General collection | Fixed data | Unique items | Key-value mapping |