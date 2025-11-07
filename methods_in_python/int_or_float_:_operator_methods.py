'''
Q1. What are special operator methods in Python?
Ans:
They are built-in methods (starting and ending with `__`)  
that define how objects respond to operators like `+`, `-`, `*`, `/`, etc.
'''
# Example
a = 5
b = 3
print(a + b)         # 8
print(a.__add__(b))  # 8 (same as a + b)



'''
Q2. What are common numeric special methods shared by int and float?
Ans:
Both int and float implement:

- `__add__()` → addition (`a + b`)
- `__sub__()` → subtraction (`a - b`)
- `__mul__()` → multiplication (`a * b`)
- `__truediv__()` → division (`a / b`)
- `__abs__()` → absolute value (`abs(a)`)
'''

# __add__() → addition
print((5).__add__(3))   # 8  (same as 5 + 3)

# __sub__() → subtraction
print((10).__sub__(4))  # 6  (same as 10 - 4)

# __mul__() → multiplication
print((6).__mul__(7))   # 42  (same as 6 * 7)

# __truediv__() → division
print((10).__truediv__(4))  # 2.5  (same as 10 / 4)

# __abs__() → absolute value
print((-9).__abs__())   # 9  (same as abs(-9))
