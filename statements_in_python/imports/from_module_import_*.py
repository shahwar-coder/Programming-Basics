'''
Q1. What does from module import * do in Python?
Ans: It imports all public names from a module into the current namespace.  
- Names starting with _ are ignored.  
- If the module defines __all__, only those names are imported.

Example:
'''
from math import *
print(sqrt(25))   # 5.0




'''
Q2. Why is from module import * discouraged?
Ans:
- Pollutes namespace with many names.
- Risk of name conflicts (overwriting existing functions/variables).
- Harder to trace where a function came from.

Example:
'''
from math import *
from cmath import *
print(sqrt(-1))   # Which sqrt? cmath.sqrt overwrote math.sqrt




'''
Q3. What is the best practice regarding from ... import *?
Ans:
- Avoid in production code.
- Use only in interactive/quick scripts.
- Prefer explicit imports for clarity.
'''




'''
Q4. Coding question?
'''
from math import *
print("Square root of 16:", sqrt(16))
# ✅ 4.0  (sqrt imported directly from math)

x = "hello"
from keyword import *
print("Is 'x' a keyword?", iskeyword("x"))
# ✅ False (since "x" is not a Python keyword)

print("Value of x:", x)
# ✅ hello (unchanged, because keyword module doesn’t define "x")



'''
Q5. How do '_' (leading underscore) and '__all__' affect from module import * ?
Ans:
- Names starting with _ are not imported by default.  
- If a module defines __all__, only the names listed in __all__ 
  are imported with *.  

Example (module demo.py):
'''
__all__ = ["func"]
def func(): return "visible"
def hidden(): return "invisible"

>>> from demo import *
>>> print(func())    # works
>>> print(hidden())  # NameError, not imported




'''
Important one-liners:
-> _name → private by convention, skipped by *.
-> __all__ → explicit whitelist for * imports.
'''
