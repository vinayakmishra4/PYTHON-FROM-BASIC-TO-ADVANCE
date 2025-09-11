# 📌 Day 33: Custom Errors in Python

---

## 📝 Definition

> Custom errors in Python are user-defined exceptions that allow developers to handle specific situations in a program more clearly. They are created by defining new exception classes that usually inherit from the built-in **`Exception`** class.
> 
> These errors give developers the flexibility to represent domain-specific issues in a more descriptive way. Instead of relying solely on built-in exceptions like **`ValueError`** or **`TypeError`**, custom errors make the intent of the exception clearer.

---

## 🧩 Syntax
```python
class CustomErrorName(Exception):
    """Optional docstring for the custom error."""
    pass
```

- ✅ The custom class should inherit from `Exception` or a subclass of it.  
- ✅ By convention, custom error class names end with `Error`.  
- ✅ You can add custom attributes or methods inside the class to provide more context about the error.  

---

## 💡 Example

> Custom errors can be demonstrated by creating a new exception class and raising it in situations where built-in exceptions are not descriptive enough. For example, you might create a **`NegativeNumberError`** when a function should not accept negative inputs.
> 
> For instance, in a banking application, you might define custom errors like **`InsufficientFundsError`** or **`InvalidTransactionError`** to handle issues that are specific to the domain of finance.

---

## 🎯 Use Cases
- ✔️ To provide meaningful error messages for application-specific problems.  
- ✔️ To separate custom application logic errors from Python’s built-in exceptions.  
- ✔️ To improve code readability and maintainability.  
- ✔️ To make debugging easier by categorizing different failure cases with specific exceptions.  

---

## ⚙️ Features
- 🔹 Inherits from the base **`Exception`** class.  
- 🔹 Can include custom error messages.  
- 🔹 Can be extended with additional attributes or methods for more detailed debugging information.  
- 🔹 Integrates seamlessly with Python’s **`try-except`** handling.  
- 🔹 They can be nested or chained with built-in exceptions for more detailed error reporting.  
- 🔹 Custom errors improve communication between developers working on large codebases.  

---

## 🌟 Advantages
- ✨ Improves clarity by distinguishing between system errors and application-specific errors.  
- ✨ Provides precise control over exception handling.  
- ✨ Enhances debugging by allowing custom messages and context-specific information.  
- ✨ Promotes cleaner and more maintainable code.  
- ✨ Allows for more graceful error recovery by handling only specific error types.  

---

## ⚠️ Disadvantages
- ❌ May add unnecessary complexity if overused.  
- ❌ Requires extra effort to define and document properly.  
- ❌ Can lead to too many exception classes if not managed carefully.  
- ❌ Overuse may make the codebase harder for new developers to understand if there are too many similar exceptions.