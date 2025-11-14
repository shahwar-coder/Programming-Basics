'''
Q1. What is a module in Python?
Ans:
A module is a .py file containing functions, variables, classes, etc.
It helps organize code into reusable components.
'''
# Example
# mymodule.py  → contains functions/variables you can import


'''
Q2. How do you create and use your own module?
Ans:
Create a Python file (e.g., mymodule.py) and import it in another script using import.
'''
# Example (mymodule.py)
# def greeting(name):
#     print("Hello,", name)

# main.py
# import mymodule
# mymodule.greeting("Alice")


'''
Q3. How do you access variables inside a module?
Ans:
Import the module and use dot notation.
'''
# Example
# mymodule.py → person1 = {"name": "John", "age": 36}
# import mymodule
# print(mymodule.person1["age"])


'''
Q4. How do you give a module a shorter alias?
Ans:
Use "import module as alias".
'''
# Example
# import mymodule as mx
# mx.greeting("Bob")


'''
Q5. How do you import only specific items from a module?
Ans:
Use: from module_name import item1, item2.
'''
# Example
# from mymodule import greeting, person1
# greeting("Charlie")
# print(person1["name"])


'''
Q6. How do you inspect what's inside a module?
Ans:
Use dir(module) to list functions, classes, variables, etc.
'''
# Example
import platform
print(dir(platform)[:5])  # show first few names


'''
Q7. Difference between import module and from module import name?
Ans:
import module → use module.name  
from module import name → use name directly  
'''
# Example
# import math; math.sqrt(9)
# from math import sqrt; sqrt(9)


'''
Q8. How does Python find modules? (Module Search Path)
Ans:
Python searches in:
1. Current directory
2. PYTHONPATH env variable
3. Installed site-packages
Check using sys.path
'''
# Example
import sys
print(sys.path[:3])


'''
Q9. What are circular imports and why avoid them?
Ans:
Circular import = A imports B and B imports A.
Causes errors or incomplete imports.
Fix by restructuring code.
'''
# Example (concept)
# A.py imports B; B.py imports A → circular import error


'''
Q10. Difference between a module and a package?
Ans:
Module → single .py file  
Package → folder with modules + __init__.py  
'''
# Example
# myproject/
#    utils/
#       __init__.py
#       math_utils.py


'''
Q11. How do you reload a module during development?
Ans:
Use importlib.reload(module) to re-import without restarting Python.
'''
# Example
import importlib
import math
importlib.reload(math)


'''
Q12. Why avoid "from module import *"?
Ans:
It pollutes your namespace and may override existing names.
'''
# Example
# from math import *  # Not recommended
