'''
Q. What happens when two variables reference the same object?
Ans:
- Both names point to the same memory object. Changing a mutable object through one name affects the other.

Example:
'''
a = b = [1, 2]
a.append(3)
print(b)

# Step-by-step:
# 1. a and b both point to same list.
# 2. append changes that list.
# 3. Both a and b see [1,2,3].
