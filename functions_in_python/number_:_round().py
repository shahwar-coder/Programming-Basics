'''
Q1. What does the round() function do in Python?
Ans:
It rounds a number to the nearest integer or to a specified number of decimal places.  
You can control precision using the optional `ndigits` argument.
'''
# Example
print(round(3.7))         # 4
print(round(3.14159, 2))  # 3.14



'''
Q2. What is the syntax of round()?
Ans:
`round(number[, ndigits])`  
- `number`: value to round  
- `ndigits`: number of decimal places (optional)
'''



'''
Q3. What happens when ndigits is not provided?
Ans:
It rounds to the nearest whole number (integer).  
The return type is `int` if the number is a float with no fractional part.
'''
# Example
print(round(9.9))  # 10
print(round(2.1))  # 2



'''
Q4. How does round() handle the ndigits parameter?
Ans:
- Positive ndigits → round to that many decimals.  
- Negative ndigits → round to tens, hundreds, etc.
'''
# ✅ Positive ndigits → rounds to decimal places
print(round(3.14159, 2))   # 3.14
print(round(9.8765, 3))    # 9.877
print(round(12.3456, 0))   # 12.0   → 0 decimals

# ✅ Negative ndigits → rounds to tens, hundreds, thousands
print(round(1234, -1))     # 1230   → nearest 10
print(round(1234, -2))     # 1200   → nearest 100
print(round(67890, -3))    # 68000  → nearest 1000

# ✅ Edge and nuance cases
print(round(25, -1))       # 30     → halfway rounds to even (Banker’s rounding)
print(round(2.675, 2))     # 2.67   → floating-point precision effect
print(round(2.675, -2))    # 0.0    → rounds to nearest 100 (2.675 < 50 → 0)



'''
Q5. What rounding rule does Python use?
Ans:
It uses **banker’s rounding** (round-half-to-even).  
If the value is exactly halfway, it rounds to the nearest even number.
'''
# Example
print(round(2.5))  # 2
print(round(3.5))  # 4
print(round(1.25, 1))  # 1.2
print(round(1.35, 1))  # 1.4



'''
Q6. What data types does round() work with?
Ans:
It works with integers and floats.  
For complex numbers, it raises a `TypeError`.
'''
# Example
print(round(7))        # 7
print(round(3.7))      # 4
try:
    print(round(3 + 4j))
except TypeError as e:
    print("Error:", e)



'''
Q7. What type does round() return?
Ans:
- Returns `int` if no ndigits specified.  
- Returns `float` when ndigits is specified.
'''
# Example
print(round(5.6))        # 6 (int)
print(round(5.678, 2))   # 5.68 (float)



'''
Q8. How is round() different from math.floor() and math.ceil()?
Ans:
- `round()` → nearest value (banker’s rule)  
- `math.floor()` → always rounds down  
- `math.ceil()` → always rounds up
'''
# Example
import math
x = 3.7
print(round(x), math.floor(x), math.ceil(x))  # 4 3 4



'''
Q9. Can round() be used with negative numbers?
Ans:
Yes — rounding behavior is symmetric for negatives.  
It follows the same “round half to even” rule.
'''
# Example
print(round(-2.5))  # -2
print(round(-3.5))  # -4



'''
Q10. When is round() best used?
Ans:
Use it when you want approximate display-friendly values,  
not for financial or high-precision math (use Decimal for that).
'''
