'''
Q1. What is a decorator in Python, in simple words?
A.
A decorator is a function that adds extra behavior to another function
without changing the original function’s code.
It “wraps” a function and runs code before or after it.
'''
# Example:
# def decorator(func):
#     def wrapper():
#         print("Before function")
#         func()
#     return wrapper
#
# @decorator
# def hello():
#     print("Hello")
#
# hello()
# Output:
# Before function
# Hello


'''
Q2. What problem do decorators solve?
A.
Decorators solve the problem of code repetition.
They help move common logic (like login checks, logging, validation)
out of multiple functions into one reusable place.
'''
# Example:
# Without decorator → login check inside many functions
# With decorator → one login_required decorator reused everywhere


'''
Q3. How does the @decorator syntax actually work?
A.
The @decorator syntax replaces the function with the decorated version.
It is just a cleaner way of writing function assignment.
'''
# Example:
# @login_required
# def orders():
#     pass
#
# Is the same as:
# orders = login_required(orders)


'''
Q4. Why do decorators use inner (wrapper) functions?
A.
Because the wrapper function allows the decorator to:
- run code before the original function
- decide whether to call the original function
- modify or block the result
'''
# Example:
# def decorator(func):
#     def wrapper():
#         return func()
#     return wrapper


'''
Q5. Why should decorators use *args and **kwargs?
A.
Using *args and **kwargs makes decorators flexible.
It allows them to work with any function signature,
not just functions with fixed parameters.
'''
# Example:
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper


'''
Q6. Why is functools.wraps important in decorators?
A.
@wraps preserves the original function’s metadata
like name, docstring, and help() output.
Without it, everything looks like "wrapper".
'''
# Example:
# from functools import wraps
#
# def decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper
