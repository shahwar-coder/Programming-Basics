'''
Q1. What do the bin(), oct(), and hex() functions do in Python?
Ans:
They convert integers into their string representations  
in base 2 (binary), base 8 (octal), and base 16 (hexadecimal) respectively.
'''
# Example
print(bin(42))  # '0b101010'
print(oct(42))  # '0o52'
print(hex(42))  # '0x2a'



'''
Q2. What is the syntax for each of these functions?
Ans:
- bin(x) → returns binary string prefixed with '0b'  
- oct(x) → returns octal string prefixed with '0o'  
- hex(x) → returns hexadecimal string prefixed with '0x'
'''



'''
Q3. What types of values do bin(), oct(), and hex() work with?
Ans:
They only work with **integers** — not floats, strings, or complex numbers.
Passing other types raises a `TypeError`.
'''
# Example
try:
    print(bin(3.14))
except TypeError as e:
    print("Error:", e)



'''
Q4. How do these functions handle negative numbers?
Ans:
They keep the minus sign in the result —  
only the number part is converted to the base form.
'''
# Example (+ve)
print(bin(42))  # '0b101010'
print(oct(42))  # '0o52'
print(hex(42))  # '0x2a'

# Example (-ve)
print(bin(-42))  # '-0b101010'
print(oct(-42))  # '-0o52'
print(hex(-42))  # '-0x2a'



'''
Q5. How can you remove the base prefix from the result?
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



'''
Q6. How can you convert a base string back to an integer?
Ans:
Use the `int()` function with a base argument.
'''
# Example
print(int('101010', 2))  # 42
print(int('2a', 16))     # 42
print(int('52', 8))      # 42



'''
Q7. What happens if you use them with boolean values?
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



'''==good to know==
Q9. Are there alternative ways to format numbers in different bases?
Ans:
Yes — using the built-in `format()` or f-strings:
`format(x, 'b')`, `format(x, 'o')`, `format(x, 'x')`.
'''
# Example
x = 42
print(format(x, 'b'))  # '101010'
print(format(x, 'x'))  # '2a'
print(f"{x:#X}")       # '0X2A'
