'''
Q1. What types of values can int() convert?
Ans:
- **Float** → truncates decimals  
- **String** → interprets numeric text (optional base)  
- **Boolean** → True → 1, False → 0  
- **No argument** → returns 0
'''
# Example
print(int("42"))    # 42
print(int(True))    # 1
print(int(False))   # 0
print(int())        # 0
print(int(5.99))   # 5
print(int(-3.2))   # -3



'''
Q2. How can int() convert numbers from different bases?
Ans:
You can specify a base (2–36) when converting from a string.  
Example: binary (base 2), hexadecimal (base 16), octal (base 8).
'''
# Example
print(int("101", 2))   # 5 (binary → decimal)
print(int("1A", 16))   # 26 (hexadecimal → decimal)
print(int("77", 8))    # 63 (octal → decimal)



'''
Q3. What’s the difference between int() and math.trunc()?
Ans:
Both remove the fractional part, but:
- `int()` → type conversion (returns int)
- `math.trunc()` → mathematical truncation (requires float input)
'''
# Example
import math
x = 5.9
print(int(x))         # 5 #eg. can take and convert string form of number to integer : "132"->132
print(math.trunc(x))  # 5 #eg. cannot take string form of a number : "132"



'''
Q4. What happens when converting booleans?
Ans:
`True` becomes `1` and `False` becomes `0`,  
because `bool` is a subclass of `int` in Python.
'''
# Example
print(int(True))   # 1
print(int(False))  # 0



'''
Q5. How does int() handle whitespace or signs in strings?
Ans:
It ignores leading/trailing spaces and recognizes `+` or `-` signs.
'''
# Example
print(int("   +42  "))  # 42
print(int("-99"))        # -99



'''
Q6. What’s the default behavior when no arguments are passed?
Ans:
Calling `int()` without arguments simply returns **0**.
'''
# Example
print(int())  # 0



'''
Summary:
✅ `int(x, base)` converts values to integers.  
🔹 Floats → truncated  
🔹 Strings → interpreted by base  
🔹 Booleans → 1 or 0  
🔹 No args → 0  
🔹 Raises errors for invalid types.
'''
