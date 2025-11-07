'''
Q. Do these operations create a new list?
Ans:
No — all modification methods (`append`, `extend`, `insert`, etc.)  
**change the list in place** and return `None`.
'''
# Example
lst = [1, 2, 3]
result = lst.append(4)
print(lst, result)   # [1, 2, 3, 4] None
