# Recursion in Python 📖

---

## Definition 📝
> **Recursion** is a programming technique where a function calls itself in order to solve a problem.  
> Each recursive call should bring the problem closer to a **_base case_**, which stops the recursion.  
> Recursion works by dividing a complex problem into smaller, more manageable subproblems that resemble the original problem.  
> This approach often mirrors mathematical definitions, such as the factorial or Fibonacci sequences, where the solution is expressed in terms of smaller instances of the same problem.

---

## Syntax 💡
The general syntax of a recursive function in Python:
```python
def recursive_function(parameters):
    if base_case_condition:
        return base_case_value
    else:
        # Recursive call with modified parameters
        return recursive_function(modified_parameters)
```
- ***Parameters***: Inputs to the function that typically change with each recursive call to approach the *base case*.  
- ***Base case***: A condition that stops the recursion by returning a value without making further recursive calls.  
- ***Recursive case***: The part where the function calls itself with modified parameters, moving the problem closer to the *base case*.  

---

## Example ⚙️
Example: Calculating the factorial of a number using recursion.
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```
Another example: Computing the nth Fibonacci number recursively.
```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

---

## Use ✨
Recursion is commonly used for problems that can be broken down into similar subproblems, such as:  
- ✅ Processing tree or graph structures (e.g., traversals)  
- 🔄 Solving mathematical problems (e.g., factorial, Fibonacci sequence)  
- 🧩 Implementing algorithms like quicksort and mergesort  
- 📂 Navigating nested data structures  
- 📂 Parsing expressions in compilers or interpreters  
- 📂 Traversing directories and file systems  
- 🧩 Solving backtracking problems like Sudoku, maze solving, and the N-Queens problem  

---

## Features ✨
✔️ A recursive function must have a *base case* to prevent infinite recursion.  
✔️ Each recursive call should progress toward the *base case*.  
✔️ Recursive solutions can be simpler and more elegant for certain problems, improving code clarity.  
✔️ However, recursion can sometimes be less efficient than iteration in terms of performance and memory usage due to call stack overhead.  
✔️ Python does not optimize tail recursion, so deep recursion may lead to stack overflow errors.  
✔️ Debugging recursive functions can be challenging; carefully tracing each call and understanding the call stack is important.  
✔️ Python has a recursion depth limit (default is 1000), which can be changed using `sys.setrecursionlimit()`.  
✔️ Recursion can be less memory-efficient than iteration for large problems due to call stack usage.

---

## Advantages 🌟
- ✅ Simplifies complex problems by breaking them into smaller subproblems.
- 🌿 Provides cleaner, more readable code for problems like tree/graph traversal.
- ✨ Naturally fits problems defined recursively (e.g., factorial, Fibonacci).
- 🎯 Useful for algorithms requiring backtracking.

---

## Disadvantages ⚠️
- ⚠️ Higher memory usage due to call stack overhead.
- 🐢 Slower execution compared to iteration in many cases.
- 🚫 Limited by Python’s recursion depth.
- 🔍 Harder to debug and trace recursive calls.
- ❌ Lack of tail recursion optimization in Python.