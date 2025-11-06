'''
Q. What does float.hex() return?
Ans:
It returns the **hexadecimal representation** of the float  
in a standardized format used by IEEE-754.  
This format is reversible using `float.fromhex()`.
'''
# Example
print((0.75).hex())     # '0x1.8p-1'
print((1.0).hex())      # '0x1.0000000000000p+0'
print((3.5).hex())      # '0x1.c000000000000p+1'
