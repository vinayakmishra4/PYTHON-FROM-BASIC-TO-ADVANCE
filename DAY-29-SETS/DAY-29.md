## 🌟 Day 29 – Sets in Python

---

### 🔹 1. **Definition**

A **Set** is a collection data type in Python that:  
- ✔ Stores **unique elements only** (no duplicates)  
- ✔ Is **unordered** (no index or position)  
- ✔ Is **mutable** (we can add/remove items)  
- ✔ Contains only **immutable elements** (numbers, strings, tuples, etc.)  

---

### 🔹 2. **Syntax**

```python
# Using curly braces
my_set = {1, 2, 3}

# Using set() constructor
my_set = set([1, 2, 2, 3])

# Empty Set
empty_set = set()    # {} makes a dictionary, not a set
```

---

### 🔹 3. **Example**

```python
fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)        # {'apple', 'banana', 'cherry'}

fruits.add("orange")       # Add element
fruits.remove("banana")    # Remove element
print("apple" in fruits)   # Membership test → True
```

---

### 🔹 4. **Types of Sets**

- 1️⃣ **Empty Set** → `set()`  
- 2️⃣ **Heterogeneous Set** → `{1, "hi", 3.14, (1,2)}`  
- 3️⃣ **Frozen Set (Immutable)** → `frozenset([1,2,3])`  

---

### 🔹 5. **Features**

- ✨ **Unordered** – no indexing  
- ✨ **Unique** – no duplicates  
- ✨ **Mutable** – can add/remove elements  
- ✨ Supports **set theory operations** (union, intersection, etc.)  
- ✨ **Heterogeneous** but **immutable-only elements**  

---

### 🔹 6. **Operations on Sets**

#### 🔸 Mathematical Operations

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)   # Union → {1, 2, 3, 4, 5, 6}
print(A & B)   # Intersection → {3, 4}
print(A - B)   # Difference → {1, 2}
print(A ^ B)   # Symmetric Difference → {1, 2, 5, 6}
```

#### 🔸 Common Methods

| Method             | Use                                  |
|--------------------|-------------------------------------|
| `.add(x)`          | Add element                         |
| `.remove(x)`       | Remove element (error if not found) |
| `.discard(x)`      | Remove element (safe)                |
| `.pop()`           | Remove random element                |
| `.clear()`         | Empty the set                       |
| `.update(iterable)`| Add multiple elements               |
| `.issubset(set2)`  | Check subset                       |
| `.issuperset(set2)`| Check superset                     |
| `.isdisjoint(set2)`| Check no common elements           |

---

### 🔹 7. **Uses of Sets**

- ✅ Remove duplicates from a list  
- ✅ Perform mathematical operations (Union, Intersection, etc.)  
- ✅ Fast membership checking (`x in set`)  
- ✅ Data filtering → keep only unique values  
- ✅ Checking relationships (subset, superset, disjoint sets)  

---

### 🔹 8. **Advantages**

- ✔ Removes duplicates automatically  
- ✔ Faster lookups than lists/tuples  
- ✔ Supports set-theory operations  
- ✔ Simplifies comparison between datasets  

---

### 🔹 9. **Disadvantages**

- ❌ No order → can’t use indexing/slicing  
- ❌ Cannot store mutable/unhashable types (list, dict, set)  
- ❌ More memory usage than tuples/lists  
- ❌ Not useful if duplicates/order are required  

---

### 🔹 10. **Comparison with Other Collections**

| Feature          | List | Tuple | Set | Frozen Set |
|------------------|:----:|:-----:|:---:|:----------:|
| Ordered          | ✅   | ✅    | ❌  | ❌         |
| Allows Duplicates | ✅   | ✅    | ❌  | ❌         |
| Mutable          | ✅   | ❌    | ✅  | ❌         |
| Indexing         | ✅   | ✅    | ❌  | ❌         |
| Hashable         | ❌   | ✅    | ❌  | ✅         |

---

✨ **Quick Tip:** Use sets when you need unique, unordered data with fast lookups.  
✨ Use frozen sets when you need an immutable collection of unique values.

---