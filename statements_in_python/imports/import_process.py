'''
Q1. What are the two main phases of Python’s import process?
Ans:
- Search: Python locates the module (built-ins → current dir → sys.path).
- Bind: It loads/creates the module object and binds the name in the current namespace.

Example:
'''
import math
print(math.__name__)   # "math"




'''
Q2. What is __import__() in Python?
Ans: It’s the low-level function used by the import statement.  
__import__('math') ≈ import math  

Example:
'''
m = __import__('math')
print(m.sqrt(16))   # 4.0




'''
Q3. Why should you prefer importlib.import_module() over __import__()?
Ans: importlib.import_module() is higher-level, more readable, and recommended 
for dynamic imports.  

Example:
'''
import importlib
random = importlib.import_module('random')
print(random.randint(1, 6))




'''
Q4. Why isn’t a module re-imported if imported again?
Ans: Because it’s cached in sys.modules.  
Re-import just returns the cached object.

Example:
'''
import math, sys
print(id(math), id(sys.modules['math']))   # same id




'''
Q5. Code Output?
'''

'''
# Output you saw:
True
True
'''

'''
Explanation:
- m1 = __import__('math') and m2 = __import__('math') both call the low-level import.
  Because the module is cached in sys.modules after the first load,
  the second call returns the same module object. Hence m1 is m2 → True.

- sys.modules stores the module object under the key 'math'.
  Comparing m1 with sys.modules['math'] shows they are the same cached object,
  so m1 is sys.modules['math'] → True.

Key takeaway: __import__ uses the same import machinery and caching as the import statement.
'''
