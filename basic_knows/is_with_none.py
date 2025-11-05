'''
Q. When should we use ‘is’ instead of ‘==’?
Ans:
Use ‘is’ for identity checks — especially for special objects like `None`.  
For normal value comparison, use `==`.
'''
# Example
x = None
if x is None:
    print("Empty")   # correct way
