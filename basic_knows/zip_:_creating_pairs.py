'''
Q. What does Python’s zip() function do?
Ans:
It combines elements from two or more iterables (like lists or tuples)  
into tuples, pairing items with the same index.  
It stops when the shortest iterable ends.
'''
# Example
names = ["Ali", "Sara", "Omar"]
scores = [85, 90, 88]
result = list(zip(names, scores))
print(result)    # [('Ali', 85), ('Sara', 90), ('Omar', 88)]
