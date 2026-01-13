'''
Q1. What problem does functools.wraps solve?
A.
When a function is decorated, the original function’s identity
(name, docstring, annotations) is lost and replaced by the wrapper’s.
functools.wraps fixes this by preserving the original function’s metadata.
'''
# Example:
# Without @wraps:
# orders.__name__ → 'wrapper'
# orders.__doc__  → None
#
# With @wraps:
# orders.__name__ → 'orders'
# orders.__doc__  → 'Return orders page'


'''
Q2. What is functools.wraps in simple terms?
A.
functools.wraps is a helper decorator that copies important metadata
from the original function to the wrapper function.
'''
# Example:
# @wraps(func)
# def wrapper(...):
#     ...
# This makes wrapper look like func to Python tools.


'''
Q3. Which metadata does @wraps copy?
A.
@wraps copies key attributes such as:
- __name__
- __doc__
- __module__
- __annotations__
- __wrapped__
'''
# Example:
# wrapper.__name__ = func.__name__
# wrapper.__doc__  = func.__doc__


'''
Q4. Why is losing function metadata dangerous in real applications?
A.
Because many tools depend on it:
- logging systems
- debuggers
- API frameworks
- documentation generators
- type checkers
'''
# Example:
# Flask/FastAPI routes may break
# Swagger docs may disappear
# Stack traces become confusing


'''
Q5. What is __wrapped__ and why is it important?
A.
__wrapped__ points to the original function before decoration.
It allows tools to unwrap decorators and inspect the real function.
'''
# Example:
# inspect.signature(func)
# Works correctly only if __wrapped__ exists


'''
Q6. When should @wraps ALWAYS be used?
A.
Whenever you write a decorator that wraps another function.
This is an industry-standard best practice with no exceptions.
'''
# Example:
# def my_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper
