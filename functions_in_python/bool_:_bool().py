'''
Q1. What does bool(x) do?
Ans:
It converts any value into its **Boolean equivalent** —  
`True` or `False`, based on Python’s truth value testing rules.
'''
# Example
print(bool(5))        # True
print(bool(0))        # False
print(bool("Hello"))  # True
print(bool(""))       # False



'''
Q2. What values evaluate to False when passed to bool()?
Ans:
The following are **falsy**:
`0, 0.0, 0j, '', [], {}, set(), None, False`
Everything else is considered truthy.
'''
# Example
falsy = [0, 0.0, 0j, '', [], {}, set(), None, False]
print([bool(x) for x in falsy])   # [False, False, False, False, False, False, False, False, False]



'''
Q3. What’s the main use of bool() in Python?
Ans:
It’s used for:
- **Condition checking** (`if`, `while`)  
- **Filtering** truthy or falsy values  
- **Simplifying** logical decisions
'''
# Example
values = [0, 1, "", "yes", [], [1]]
truthy = [x for x in values if bool(x)]
print(truthy)   # [1, 'yes', [1]]



'''
Q4. How does bool() decide True or False for custom objects?
Ans:
It checks:
1️⃣ `obj.__bool__()` if defined  
2️⃣ Else `obj.__len__()`  
3️⃣ Else defaults to True
'''
# Example
class Box:
    def __len__(self): return 0
print(bool(Box()))   # False (because len() == 0)



'''
Q5. What is the relationship between bool and int?
Ans:
`bool` is a **subclass of int**, so:
- `True == 1`  
- `False == 0`  
But conceptually, they represent logical states, not numbers.
'''
# Example
print(True + True)      # 2
print(False * 10)       # 0
print(isinstance(True, int))  # True



'''
Q6. Can bool() handle complex numbers?
Ans:
Yes — complex numbers are truthy unless both real and imaginary parts are zero.
'''
# Example
print(bool(3+0j))   # True
print(bool(0+0j))   # False



'''
Q7. Can you customize truth behavior in your own class?
Ans:
Yes — define `__bool__()` (or `__len__()` fallback)  
to control how objects behave in Boolean contexts.
'''
# Example
class Signal:
    def __bool__(self):
        return False
print(bool(Signal()))  # False
