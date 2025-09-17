'''
Q1. What is a circular import?
Ans: When two or more modules import each other, causing incomplete initialization.  
'''
Example:
# a.py
import b
print("a sees b.x:", b.x)

# b.py
import a
x = 42
# Running python a.py → AttributeError (b imports a before a is finished loading).


'''
Q2. Why do circular imports cause problems?
Ans: Because import executes top-level code.  
If module A is still half-loaded when module B tries to use it, attributes may not exist yet.
'''



'''
Q3. What are common fixes for circular imports?
Ans:
- Refactor shared code into a third module.
- Use local imports inside functions to delay importing.
- Redesign to reduce tight coupling.
- Advanced: use importlib for dynamic import.
'''



'''
LET'S SEE THE PROBLEM AND A FIX HERE NOW:
'''

'''
❌ Circular import problem
--------------------------
'''

# a.py
# -------
import b

def func_a():
    print("func_a calling func_b")
    b.func_b()

# b.py
# -------
import a

def func_b():
    print("func_b calling func_a")
    a.func_a()

# Now if you try : python a.py ---> You’ll likely hit an error (AttributeError) because when b imports a, a isn’t fully loaded yet.


'''
✅ Fixed with local import
--------------------------
'''

# a.py
# -------
def func_a():
    print("func_a calling func_b")
    from b import func_b   # local import (only runs when function is called)
    func_b()

# b.py
# -------
def func_b():
    print("func_b called")
# Now when you run, python a.py,
'''
Output : 
func_a calling func_b
func_b called
'''

'''
Explanation:
- By moving `import b` into the function body, the import only happens at runtime 
  when `func_a()` is called.
- At that moment, both modules are already defined → no half-loaded module issue.
'''

'''
📌 Fixing Circular Imports
- Problem: modules import each other → one is half-loaded → errors.  
- Quick fix: use **local imports** (inside functions/methods) → delays import until needed.  
- Cleaner fix: refactor shared logic into a **common utility module**.  
- Best practice: keep module dependencies one-directional, avoid cycles.  
'''


'''
✅ Refactored with Common Module: (ONE MORE WAY TO FIX)
'''

common.py
------------
def shared_helper():
    print("Shared helper running")


a.py
------------
import common

def func_a():
    print("func_a running")
    common.shared_helper()

b.py
------------
import common

def func_b():
    print("func_b running")
    common.shared_helper()

# On running a.py
# func_a running
# Shared helper running

# On running b.py
# func_b running
# Shared helper running

'''
Explanation:
- The logic that both `a` and `b` need is moved to common.py.
- `a` and `b` now depend only on common, not on each other.
- This breaks the circular dependency cycle.
'''

'''
Think of common.py as a neutral “hub” module that stores shared code so other modules don’t have to reach into each other.
'''

