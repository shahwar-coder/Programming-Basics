'''
Q. How does immutability of integers relate here?
Ans:
- Integers are immutable.
- x += 1 creates a new int object and rebinds x to it.
- Not an in-place change.

Example:
'''
x = 10
print(id(x))
x += 1
print(id(x))

# Step-by-step:
# IDs differ → shows new object created, not mutation.
