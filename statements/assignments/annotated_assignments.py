'''
Q1. What is an annotated assignment in Python?
Ans: It is an assignment with a type hint (annotation).  
Syntax: x: int = 5  
It binds the name x with value 5, and stores its annotation "int".

Q2. Where are annotations stored for variables, classes, and functions?
Ans: 
- Module level → __annotations__ (dict)
- Inside a class → Class.__annotations__
- Inside a function → func.__annotations__

Q3. What is the difference between an annotated assignment with and without a value?
Ans: 
- With value: x: int = 5 → annotation + binding.  
- Without value: x: int → annotation only, name is not yet bound.

Q4. Are type hints enforced at runtime?
Ans: No. Python does not enforce annotations.  
They are hints for static type checkers (mypy, IDEs) 
and available at runtime for introspection.

Q5. (Coding)
# Try this:
'''

x: int = 10
y: str

print("Module annotations:", __annotations__)

class Person:
    name: str
    age: int = 25

print("Class annotations:", Person.__annotations__)

def greet(name: str) -> str:
    return "Hello " + name

print("Function annotations:", greet.__annotations__)

'''
Module annotations: {'x': <class 'int'>, 'y': <class 'str'>}
# Reason: At module level, __annotations__ collects variable type hints.
# x bound to int, y annotated but unbound.

Class annotations: {'name': <class 'str'>, 'age': <class 'int'>}
# Reason: Inside a class, annotations go into Class.__annotations__.
# Both 'name' and 'age' show up, regardless of default value.

Function annotations: {'name': <class 'str'>, 'return': <class 'str'>}
# Reason: Function.__annotations__ stores parameter and return type hints.
# 'name' param is str, return type is str.
'''
