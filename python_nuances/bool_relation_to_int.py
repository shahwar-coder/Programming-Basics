'''
Q. What is the relationship between bool and int?
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
