'''
Q1. What is a deep copy and how does it differ from a shallow copy?
Ans:
A **deep copy** creates a **completely independent clone** of an object,  
including all nested (inner) objects.  
This means any modification in one copy **does not affect** the other.

Why?
Because `copy.deepcopy()` recursively duplicates every object inside,  
instead of just copying references like a shallow copy does.
'''
# Example 1: Deep copy with nested list
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)   # full independent copy

print("Before change:")
print("a:", a)
print("b:", b)

b[0][0] = 99           # modify inner list of b

print("\nAfter modifying b[0][0]:")
print("a:", a)         # [[1, 2], [3, 4]] → unchanged
print("b:", b)         # [[99, 2], [3, 4]] → changed independently
print(a is b)          # False (different outer lists)
print(a[0] is b[0])    # False (different inner lists too)
