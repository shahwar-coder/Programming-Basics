'''
Q1. Why does a single-element tuple need a comma?
Ans. Without the comma, Python treats it as a normal value, not a tuple.
'''
# Example
x = (5)     # ❌ int, not tuple
y = (5,)    # ✅ tuple with one element
