'''
Q. What does int.as_integer_ratio() return?
Ans:
It returns a tuple `(numerator, denominator)` representing the integer as a rational number.  
For integers, denominator is always `1`.
'''
# Example
print((5).as_integer_ratio())     # (5, 1)
print((-7).as_integer_ratio())    # (-7, 1)
print((0).as_integer_ratio())     # (0, 1)
print((12).as_integer_ratio())    # (12, 1)

print((2.5).as_integer_ratio())    # (5, 2)
print((0.75).as_integer_ratio())   # (3, 4)
print((-1.2).as_integer_ratio())   # (-5404319552844595, 4503599627370496)
print((1.0).as_integer_ratio())    # (1, 1)
print((0.1).as_integer_ratio())    # (3602879701896397, 36028797018963968)

x = 3 / 8
print(x.as_integer_ratio())        # (3, 8)

