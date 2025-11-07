'''
Q. What does int.bit_length() do?
Ans:
It returns the **number of bits** required to represent a positive integer in binary,  
excluding the sign bit and leading zeros.
'''
# Example
print((10).bit_length())   # 4 (binary 1010 → 4 bits)
print((255).bit_length())  # 8
print((0).bit_length())    # 0
