'''
Q. What happens when converting booleans?
Ans:
`True` becomes `1` and `False` becomes `0`,  
because `bool` is a subclass of `int` in Python.
'''
# Example
print(int(True))   # 1
print(int(False))  # 0
