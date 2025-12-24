'''
Q. What does `remove(x)` do?
Ans. It removes element `x` from the set, but raises an error if `x` is not present.
'''
# Example
s = {1, 2, 3}
s.remove(2)
# s = {1, 3}

# s.remove(5) ❌ KeyError
