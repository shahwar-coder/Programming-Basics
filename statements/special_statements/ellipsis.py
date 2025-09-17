'''
It is an expression (NOT Statement)
'''

'''
Q1. What is the Ellipsis object in Python, and how is it written?
Ans: Ellipsis is a built-in object written as `...`.  
It is a literal syntax for the object `Ellipsis`.

Example:
'''

print(...)          # Output: Ellipsis
print(type(...))    # <class 'ellipsis'>



'''
Q2. How is `...` different from `pass`?
Ans:
- `pass` → a statement; does nothing when executed.  
- `...`  → an expression; evaluates to the Ellipsis object.  
- `pass` cannot be used in slicing, but `...` can.  

Example:
if True:
    pass    # ✅ valid
# print(...) inside slicing ✅ valid
'''


'''
Q3. How is `...` used in slicing?
Ans: In slicing, `...` is shorthand for “fill in missing dimensions.”  
It is often used in NumPy arrays or multi-dimensional data.

Example:
'''

lst = [1, 2, 3]
print(lst[...])   # ✅ Works, same as lst[:]



'''
Q4. Coding ?
'''
print("Ellipsis literal:", ...)
# ✅ Output: Ellipsis
# Reason: ... is literally the Ellipsis object.

print("Equality check:", ... == Ellipsis)
# ✅ Output: True
# Reason: ... is just another way to write the built-in Ellipsis.

def placeholder():
    ...
result = placeholder()
print("Result of placeholder():", result)
# ✅ Output: Ellipsis
# Reason: A function with only ... returns Ellipsis, 
# because ... is an expression, unlike pass which does nothing and returns None.
