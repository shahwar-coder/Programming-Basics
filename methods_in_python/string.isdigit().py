'''
Q. What does isdigit() check?
Ans:
It returns **True** if all characters are digits (`0–9`).  
Does not consider signs, decimals, or spaces as digits.
'''
# Example
print("12345".isdigit())   # True
print("12a45".isdigit())   # False
print("-123".isdigit())    # False (minus not allowed)
