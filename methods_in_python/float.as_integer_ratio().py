'''
Q1. What does float.as_integer_ratio() do?
Ans:
It returns the exact **fractional representation** of a float  
as a tuple `(numerator, denominator)` — showing its precise binary ratio.
'''
# Example
print((2.5).as_integer_ratio())   # (5, 2)
print((0.75).as_integer_ratio())  # (3, 4)
print((1.0).as_integer_ratio())   # (1, 1)


'''
Q2. How accurate is as_integer_ratio()?
Ans:
It’s exact — it converts the binary representation into an exact rational form.  
Even repeating decimals like 0.1 get a long but precise ratio.
'''

# Example
print((0.1).as_integer_ratio())  
# (3602879701896397, 36028797018963968)
