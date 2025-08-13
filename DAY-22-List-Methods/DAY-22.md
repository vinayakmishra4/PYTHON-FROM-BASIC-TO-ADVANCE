# 📘 DAY 22: Python List Methods Documentation

Master the essential Python list methods with clear definitions, syntax, parameters, return values, and real-world usage cases.

---

## 🔹 1. `append()`

- **Description**: Adds a single element to the end of the list.
- **Syntax**: `list.append(element)`
- **Parameters**:
  - `element`: The item to be added.
- **Returns**: `None` (modifies the list in place)
- **Use Case**: Dynamically build a list by adding one item at a time.

---

## 🔹 2. `extend()`

- **Description**: Adds all elements from an iterable to the end of the list.
- **Syntax**: `list.extend(iterable)`
- **Parameters**:
  - `iterable`: A list, tuple, set, or other iterable.
- **Returns**: `None`
- **Use Case**: Merge or concatenate lists efficiently.

---

## 🔹 3. `insert()`

- **Description**: Inserts an element at a specific index.
- **Syntax**: `list.insert(index, element)`
- **Parameters**:
  - `index`: Position to insert the item.
  - `element`: The item to insert.
- **Returns**: `None`
- **Use Case**: Place an item exactly where you want it in the list.

---

## 🔹 4. `remove()`

- **Description**: Removes the first occurrence of a specified element.
- **Syntax**: `list.remove(element)`
- **Parameters**:
  - `element`: The value to remove.
- **Returns**: `None`
- **Use Case**: Delete specific items by value.
- ⚠️ **Note**: Raises `ValueError` if the element is not found.

---

## 🔹 5. `pop()`

- **Description**: Removes and returns an element at the given index (last item by default).
- **Syntax**: `list.pop([index])`
- **Parameters**:
  - `index` *(optional)*: Index of the element to remove.
- **Returns**: The removed element.
- **Use Case**: Useful in stack/queue operations and temporary data handling.

---

## 🔹 6. `index()`

- **Description**: Finds the index of the first occurrence of a specified value.
- **Syntax**: `list.index(element)`
- **Parameters**:
  - `element`: The value to search for.
- **Returns**: Index of the element (integer).
- **Use Case**: Locate elements in a list.
- ⚠️ **Note**: Raises `ValueError` if not found.

---

## 🔹 7. `count()`

- **Description**: Counts how many times an element appears in the list.
- **Syntax**: `list.count(element)`
- **Parameters**:
  - `element`: The value to count.
- **Returns**: Count (integer).
- **Use Case**: Analyze frequency of elements in a dataset.

---

## 🔹 8. `sort()`

- **Description**: Sorts the list in ascending order by default.
- **Syntax**: `list.sort(key=None, reverse=False)`
- **Parameters**:
  - `key` *(optional)*: A function that serves as a sort key.
  - `reverse` *(optional)*: Set to `True` for descending order.
- **Returns**: `None`
- **Use Case**: Organize data for easier analysis or presentation.
- 📝 **Note**: Sorts in place and does **not** return a new list.

---

## 🔹 9. `reverse()`

- **Description**: Reverses the elements of the list in place.
- **Syntax**: `list.reverse()`
- **Parameters**: None
- **Returns**: `None`
- **Use Case**: Flip list order quickly without sorting.

---

## 🔹 10. `clear()`

- **Description**: Removes all elements from the list.
- **Syntax**: `list.clear()`
- **Parameters**: None
- **Returns**: `None`
- **Use Case**: Reset a list to an empty state while keeping the variable name.

---

💡 **Tip**: These methods are mutable operations — they directly modify the original list!