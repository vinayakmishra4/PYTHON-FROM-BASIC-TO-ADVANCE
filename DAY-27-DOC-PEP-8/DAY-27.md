# 📚 DAY 27: DOCSTRINGS and PEP-8

---

## 🔹 Definition

### ✅ Docstrings
- A **docstring** (documentation string) is a **special string** used to document a module, class, function, or method in Python.
- It’s the **first statement** in a Python block and is enclosed in **triple quotes** (`'''` or `"""`).
- Python’s built-in functions like `help()` and documentation generators like **Sphinx** rely on docstrings for auto-generated documentation.

> 📌 *Docstrings are different from regular comments. Comments use `#` and are for developers, while docstrings become part of the program’s documentation.*

---

### ✅ PEP-8
- **PEP** stands for **Python Enhancement Proposal**.  
- **PEP-8** is the **official style guide for writing readable Python code**.
- It focuses on:
  - Code **layout**
  - **Naming conventions**
  - **Indentation**
  - **Line length**
  - **Whitespace**
  - **Commenting**
  - **Docstring conventions**
- Following PEP-8 helps in **collaborative coding**, **maintainability**, and **professionalism**.

---

## 🧾 Syntax

```python
def function_name(parameters):
    """
    One-line summary of the function.

    Detailed explanation if necessary.
    
    Parameters:
        param1 (type): Description
        param2 (type): Description

    Returns:
        return_type: What the function returns
    """
    # code logic
    return result
````

---

## 🧪 Example

```python
def multiply(x, y):
    """
    Multiply two numbers and return the result.

    Parameters:
        x (int or float): First number
        y (int or float): Second number

    Returns:
        int or float: Product of x and y
    """
    return x * y
```

**Accessing the docstring:**

```python
print(multiply.__doc__)
help(multiply)
```

---

## 🧰 Use of Docstrings

* ✅ Makes **code self-documenting**
* ✅ Helps **IDE features** (tooltips, inline documentation)
* ✅ Essential for **team projects** and **open-source** contributions
* ✅ Enables **third-party tools** (e.g., Sphinx, pdoc3) to generate full documentation websites

---

## ✨ Key Features of Docstrings

| Feature                  | Description                                             |
| ------------------------ | ------------------------------------------------------- |
| **Triple Quotes**        | Supports multi-line documentation                       |
| **First Statement Rule** | Must be the first line inside a function/class          |
| **Access via `__doc__`** | Every object with a docstring has a `__doc__`           |
| **Standard Format**      | Can follow reStructuredText or Google/Numpy doc formats |

---

## 🌟 Boon (Advantages)

* ✅ **Improves readability** and self-documentation
* ✅ **Increases maintainability** for long-term projects
* ✅ Helps with **onboarding new developers**
* ✅ **Encourages thoughtful design** before coding
* ✅ **Compatible with auto-documentation tools**

---

## ⚠️ Bane (Disadvantages)

* ❌ If outdated, can be **misleading**
* ❌ **Increases maintenance overhead**
* ❌ Overuse may **clutter simple functions**
* ❌ Some devs write **vague or generic docstrings**
* ❌ No strict enforcement unless using **linters** or **code reviews**

---