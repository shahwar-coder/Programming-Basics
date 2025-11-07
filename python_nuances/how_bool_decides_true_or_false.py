'''
Q. How does bool() decide True or False for custom objects?
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
