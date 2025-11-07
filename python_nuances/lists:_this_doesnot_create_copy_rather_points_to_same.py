'''
Q1. What happens when you assign one list to another using `=`?
Ans:
It **does not create a copy** — both variables point to the **same list** in memory.  
So, modifying one will affect the other.
'''
# Example
a = [1, 2, 3]
b = a
b.append(4)
print(a, b)     # [1, 2, 3, 4] [1, 2, 3, 4]
print(a is b)   # True (same object)
