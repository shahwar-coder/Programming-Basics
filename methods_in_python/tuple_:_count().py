'''
Q1. What does `t.count(x)` do for a tuple?
Ans. It returns how many times the value `x` appears in the tuple.
'''
# Example
t = (1, 2, 2, 3, 2)
t.count(2)
# Output: 3


'''
Q2. What kind of value does `count()` return?
Ans. It always returns an integer (0 or more).
'''
# Example
t = (5, 6, 7)
t.count(10)
# Output: 0
