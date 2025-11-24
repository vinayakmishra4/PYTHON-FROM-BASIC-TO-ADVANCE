

# ---------------------------------------------
# Python Decorators – Day 50
# This file contains examples of decorators
# along with clear explanations for each example.
# ---------------------------------------------

# 1️⃣ Basic Decorator Example
# This decorator adds messages before and after
# the execution of the function it wraps.

def greet_decorator(func):
    def wrapper():
        print("🔹 Before the function runs")
        func()
        print("🔹 After the function runs")
    return wrapper

@greet_decorator
def say_hello():
    print("Hello, User!")

# Explanation:
# - greet_decorator takes say_hello as input
# - wrapper() adds extra behavior around say_hello
# - say_hello = greet_decorator(say_hello)
# - Calling say_hello() actually calls wrapper()

# --------------------------------------------------

# 2️⃣ Decorator With Arguments
# This decorator repeats function execution n times.

def repeat(n):
    def decorator(func):
        def wrapper():
            for _ in range(n):
                func()
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Welcome!")

# Explanation:
# - repeat(3) returns a decorator configured for 3 repetitions
# - decorator(func) receives the function
# - wrapper() runs func() inside a loop
# - greet() now executes 3 times

# --------------------------------------------------

# 3️⃣ Decorator With Arguments Passed to Function
# This decorator prints details about the provided arguments.

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

# Explanation:
# - wrapper accepts *args and **kwargs to support any function signature
# - before executing func(), arguments are printed
# - after execution, the result is printed

# --------------------------------------------------

# 4️⃣ Practical Decorator – Execution Timer
# Measures how long a function takes to run.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ Execution time: {end - start} seconds")
        return result
    return wrapper

@timer
def long_task():
    for _ in range(1_000_000):
        pass

# Explanation:
# - timer() records time before and after the function
# - difference shows how long func() took to execute

# --------------------------------------------------

# 5️⃣ Decorator Chaining Example
# Multiple decorators applied in order.

def deco1(func):
    def wrapper():
        print("Decorator 1 applied")
        func()
        print("Decorator 1 finished")
    return wrapper

def deco2(func):
    def wrapper():
        print("Decorator 2 applied")
        func()
        print("Decorator 2 finished")
    return wrapper

@deco1
@deco2
def process():
    print("Processing...")

# Explanation:
# - process() is first wrapped by deco2
# - The result is then wrapped by deco1
# - Order of execution: deco1 → deco2 → function

# --------------------------------------------------

# To test the examples, uncomment these calls:
# say_hello()
# greet()
# add(10, 20)
# long_task()
# process()