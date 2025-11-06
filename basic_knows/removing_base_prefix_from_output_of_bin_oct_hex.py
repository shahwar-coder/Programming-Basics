'''
Q. How can you remove the base prefix from the result?
Ans:
Slice the string starting from index 2 (`[2:]`) to remove '0b', '0o', or '0x'.
'''
# Without slicing → includes base prefixes
print(bin(10))  # '0b1010'
print(oct(10))  # '0o12'
print(hex(10))  # '0xa'

# With slicing → prefixes removed
print(bin(10)[2:])  # '1010'
print(oct(10)[2:])  # '12'
print(hex(10)[2:])  # 'a'
