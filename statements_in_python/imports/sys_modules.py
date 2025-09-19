'''
Q1. What is sys.modules in Python?
Ans: It’s a dictionary that stores all loaded modules, 
mapping module names to module objects.

Example:
'''
import sys, math
print("math" in sys.modules)   # True



'''
Q2. Why are repeated imports cheap in Python?
Ans: Because after the first import, the module object is cached 
in sys.modules. Later imports just reuse it (no recompilation, 
no reloading).

Example:
'''
import math, sys
print(id(math), id(sys.modules["math"]))   # same id



'''
Q3. How can you force a module to reload?
Ans: Use importlib.reload(module). This re-executes the module’s code, 
creating a fresh state.

Example:
'''
import importlib, math
importlib.reload(math)   # reloads math module



'''
Q4. What are the benefits of sys.modules caching?
Ans:
- Performance boost (avoid re-importing)
- Consistent identity (all parts of program see the same module object)
'''
