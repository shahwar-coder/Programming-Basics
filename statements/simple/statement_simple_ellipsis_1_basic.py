'''
- ellipsis
- ...
- it's a built in constant in python
- ellipsis is a built-in singleton object in Python.
'''

# Ellipsis == ...
print(Ellipsis == ...) # True

# Type of Ellipsis
print(type(Ellipsis)) # <class 'ellipsis'>
print(type(...)) # <class 'ellipsis'>

# Use in functions:
def future_function():
    ...

# 2D array manipulation using ellpsis
import numpy as np
arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# 0th column
print(arr[:, 0])
print(arr[..., 0])

# 1st column
print(arr[:, 1])
print(arr[..., 1])

# ....
# ....

# 0th row
print(arr[0, :])
print(arr[0, ...])

# 1st row
print(arr[1, :])
print(arr[1, ...])

# ....
# ....

# Big Take away:
# arr[:, x] is always equal to arr[..., x]
