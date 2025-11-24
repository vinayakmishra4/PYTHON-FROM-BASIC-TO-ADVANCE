# ✨ Day 50 – Python Decorators ✨

## 📘 Definition
A **decorator** in Python is a powerful tool that allows you to modify, extend, or enhance the behavior of a function or method without altering its actual code. It acts as a **wrapper** that surrounds a function, adding pre-processing or post-processing steps. Decorators help maintain clean, reusable, and readable code by separating core logic from supporting features.

> ⚠️ **Note:** Decorators are widely used in modern Python frameworks such as Django, Flask, and FastAPI.

--- 💠 ---

## 🧠 How Decorators Work (Conceptually)
- A **decorator** **takes** an existing function.
- It **adds** extra steps before, after, or around the execution of that function.
- It **returns** a new function with these additional capabilities.
- The original function remains unchanged—only its behavior is enhanced.

> This makes **decorators** ideal for tasks that apply across multiple parts of a program, such as logging, authentication, or timing.

--- 💠 ---

## 🧩 Key Features of Python Decorators
### ✔ Enhance Functionality
**Decorators** add extra features such as security checks, logging, or performance tracking without modifying the original function code.

### ✔ Code Reusability
Once defined, a **decorator** can be used on many different functions that require similar modifications.

### ✔ Clean & Organized Code Structure
**Decorators** keep the core logic clean by separating concerns. The `@decorator_name` syntax clearly expresses what extra behavior a function has.

### ✔ Support for Arguments
**Decorators** can handle:
- Function arguments
- Decorator-specific arguments
- Keyword-based configurations

### ✔ Stacking (Chaining) Support
Multiple **decorators** can be layered on a single function, with each providing its own extra behavior.

### ✔ Works with Functions and Classes
**Decorators** can be applied not only to functions but also to class methods and even entire classes.

--- 💠 ---

## 📝 Conceptual Examples (No Code)
### 1️⃣ Logging Decorator 📝
A **decorator** that keeps track of when a function is called, what inputs it receives, and what results it returns.

### 2️⃣ Authentication Decorator 🔐
A **decorator** that ensures a user is logged in before allowing a function to run—commonly used in web applications.

### 3️⃣ Performance Timer Decorator ⏱️
A **decorator** that measures how long a function takes to execute, helping developers identify slow sections of code.

### 4️⃣ Repetition Decorator 🔁
A **decorator** that runs a function multiple times automatically.

### 5️⃣ Validation Decorator ✔️
A **decorator** that checks whether the inputs provided to a function meet required conditions before executing the main logic.

--- 💠 ---

## 📚 Additional Concepts
### 🎀 **Decorator** Chaining
Multiple **decorators** can be wrapped around a function. Each **decorator** adds its own layer of behavior.

### 🎀 **Higher-Order Functions**
**Decorators** rely on the idea that functions can be passed as arguments and returned from other functions.

### 🎀 **Wrapper Functions**
A **decorator** typically uses an inner function called a "**wrapper**" to add behavior around the original function.

--- 💠 ---

## 🏁 Summary
- **Decorators** modify or extend the behavior of functions elegantly.
- They help reduce code repetition and improve clarity.
- They support nesting, customization, and chaining.
- They are widely used in advanced Python development, web frameworks, and automation.

--- 💠 ---

## 🎯 Tasks to Practice
- Write documentation explaining a logging **decorator**.
- Describe how you would design a **decorator** that checks user roles.
- Explain how a **decorator** can be used to measure execution time.

--- 💠 ---
### 🚀 Keep Practicing — You're Becoming a Python Pro!