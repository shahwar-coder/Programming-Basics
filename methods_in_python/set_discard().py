'''
Q. What does `discard(x)` do?
Ans. It removes element `x` if present, and does NOTHING if it is not.
'''
# Example
s = {1, 2, 3}
s.discard(2)
# s = {1, 3}

s.discard(5)
# No error 👍
