'''
Q1. What happens when you use import module in Python?
Ans: It loads the module (if not already loaded), creates a module object, 
and binds its name in the current namespace.  
Attributes must be accessed with dot notation.

Example:
'''
import math
print(math.sqrt(16))   # 4.0




'''
Q2. How does Python decide where to find a module?
Ans: Search order:
1) Built-in modules
2) Current working directory
3) Paths in sys.path (stdlib, site-packages, PYTHONPATH)

Example:
'''
import sys
print(sys.path)   # shows module search paths



'''
Q3. Why is a module not re-imported if you import it twice?
Ans: Because once loaded, it is cached in sys.modules.  
Re-import just reuses the same object.

Example:
'''
import math, sys
print(id(math))
print(id(sys.modules["math"]))   # same id




'''
Q4. What best practices should you follow with imports?
Ans:
- Prefer `import module` over `from module import *` (avoid polluting namespace).
- Use dot notation (math.sqrt for clarity).
- One import per line (PEP 8 style).
'''




'''
Q5. (Coding)
# Predict the outputs
'''
import math
import sys

print("math.sqrt(9):", math.sqrt(9))

print("First import id:", id(math))
import math   # importing again
print("Second import id:", id(math))

print("From sys.modules:", id(sys.modules["math"]))

'''
Actual Output:
math.sqrt(9): 3.0
First import id: <some_id>
Second import id: <same_id>
From sys.modules: <same_id>
'''

'''
Explanation:
- math.sqrt(9) → 3.0 (uses math module’s sqrt).
- The first import loads the module into memory and binds the name "math".
- The second import doesn’t reload it; it reuses the cached module from sys.modules.
- Therefore, both imports and sys.modules["math"] point to the same object → same id.
'''
