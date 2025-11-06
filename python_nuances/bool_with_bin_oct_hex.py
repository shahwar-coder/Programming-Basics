'''
Q. What happens if you use them (bin/oct/hex functions) with boolean values?
Ans:
Since `bool` is a subclass of `int`,  
`bin(True)` and `bin(False)` work and return binary representations of 1 and 0.
'''
# Example
print(bin(True))   # '0b1'
print(oct(False))  # '0o0'

# With Slicing
print(bin(True)[2:])   # '1'
print(oct(False)[2:])  # '0'
