'''
Q1. How does float() handle integers and booleans?
Ans:
- Integers → converted to float form (5 → 5.0).  
- Booleans → True → 1.0, False → 0.0.
'''
# Example
print(float(5))       # 5.0
print(float(True))   # 1.0
print(float(False))  # 0.0
print(float())        # 0.0



'''
Q2. How does float() work with strings?
Ans:
If the string represents a valid floating number,  
it converts successfully. Otherwise, it raises a ValueError.
'''
# Example
print(float("3.14"))   # 3.14
print(float("-2.5"))   # -2.5
print(float("1e3"))    # 1000.0  (scientific notation)



'''
Q3. What happens when no argument is passed to float()?
Ans:
Calling `float()` without arguments returns **0.0**.
'''
# Example
print(float())   # 0.0



'''
Q4. Can float() handle numeric expressions like "3 + 2"?
Ans:
No — `float()` only parses plain numeric strings,  
not expressions. Use `eval()` if safe and necessary.
'''
# Example
try:
    print(float("3 + 2"))
except ValueError as e:
    print("Error:", e)
# Error: could not convert string to float: '3 + 2'
