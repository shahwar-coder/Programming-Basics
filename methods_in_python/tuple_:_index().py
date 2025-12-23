'''
Q1. What does `t.index(x)` do for a tuple?
Ans. It returns the index of the FIRST occurrence of value `x`.
'''
# Example
t = ("a", "b", "c", "b")
t.index("b")
# Output: 1


'''
Q2. What happens if the value is not found using `index()`?
Ans. Python raises a ValueError.
'''
# Example
t = (1, 2, 3)
# t.index(5)  ❌ ValueError: tuple.index(x): x not in tuple


'''
Q3. Why does `index()` return only the first position?
Ans. Because it stops searching as soon as it finds the value.
'''
# Example
t = (9, 8, 9, 8)
t.index(8)
# Output: 1 (not 3)


'''
Q4. How can you safely use `index()` without crashing?
Ans. Check membership using `in` before calling `index()`.
'''
# Example
t = (1, 2, 3)
if 2 in t:
    pos = t.index(2)
# Safe usage ✔️
# Note: I do not think for big tuple, this will be optimised.


'''
Q5. Are `count()` and `index()` available for lists too?
Ans. Yes. Both methods work the same way for lists and tuples.
'''
# Example
lst = [1, 2, 2, 3]
lst.count(2)   # 2
lst.index(3)   # 3


'''
Q6. What is the one-line rule to remember?
Ans. `count()` tells how many times a value appears, `index()` tells where it appears first.
'''
# Example (lock it 🔒)
# count → quantity
# index → position
