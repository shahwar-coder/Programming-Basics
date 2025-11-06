'''
Q. What does float.as_integer_ratio() do?
Ans:
It returns the exact **fractional representation** of a float  
as a tuple `(numerator, denominator)` — showing its precise binary ratio.
'''
# Example
print((2.5).as_integer_ratio())   # (5, 2)
print((0.75).as_integer_ratio())  # (3, 4)
print((1.0).as_integer_ratio())   # (1, 1)
