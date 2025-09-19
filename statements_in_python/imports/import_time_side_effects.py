'''
Q1. What are import-time side effects in Python?
Ans: When a module is imported, all its top-level code runs once.  
This can cause unintended side effects if the module does more than just definitions.
'''
# Example (mod.py):
print("Module loaded!")   # runs on import

>>> import mod
Module loaded!   # printed immediately



'''
Q2. In what order are imports executed?
Ans: Imports run top-to-bottom in the order they appear in a file.  
Dependencies may depend on this order.

Example:
'''
import a
import b
# a runs fully before b starts



'''
Q3. What problem arises with circular imports?
Ans: If module A imports B, and B imports A, 
one module may be only partially initialized when the other tries to use it → ImportError or AttributeError.
'''
# Example:
# a.py (this simply means in python file a.py)
import b
print("In a:", b.value)

# b.py
import a
value = 42



'''
Q4. What are best practices to avoid import-time problems?
Ans:
- Keep top-level code minimal (define functions/classes/constants).
- Do initialization inside functions (not at import).
- Be consistent with import ordering.
- Avoid circular dependencies by refactoring (e.g., move shared logic to a utils module).
'''



'''
📌 Import-time Key Points
- Module’s top-level code runs once at import.
- Imports execute in order, top to bottom.
- Circular imports can break (partially loaded modules).
- Best practice: keep top-level code minimal, avoid side effects.
'''
