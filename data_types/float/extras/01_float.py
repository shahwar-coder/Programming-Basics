'''
Q1. What are floating-point numbers (float) in Python?
Ans:
They represent real numbers with fractional parts.  
Floats are **approximate** due to binary representation limits  
and usually have 15–17 digits of precision.
'''
# Example
x = 3.14
y = -0.5
print(type(x), x + y)  # <class 'float'> 2.64



'''
Q2. What are the ways to write float literals?
Ans:
- Decimal notation: 3.14, -0.5, 2.0  
- Exponential notation: 1.5e2 (150.0), 2.5E-3 (0.0025)
'''
# Example
a = 1.5e2    # 150.0
b = 2.5E-3   # 0.0025
print(a, b)



'''
Q3. What are special floating-point values?
Ans:
Python supports:
- `math.inf` → positive infinity  
- `-math.inf` → negative infinity  
- `math.nan` → "Not a Number" (invalid results)
'''
# Example
import math
print(math.inf, -math.inf, math.nan) # inf -inf nan
print(math.isinf(math.inf))  # True
print(math.isnan(math.nan))  # True



'''
Q4. What built-in functions work commonly with floats?
Ans:
- `abs(x)` → absolute value  
- `round(x[, n])` → rounding  
- `pow(x, y)` → exponentiation  
- `math.floor(x)` / `math.ceil(x)` → down/up rounding
'''
# Example
import math
x = -3.75
print(abs(x), round(x), math.floor(x), math.ceil(x))
# Output: 3.75 -4 -3



'''
Q5. Why shouldn’t you compare floats directly with == ?
Ans:
Because floats are **approximate** —  
tiny rounding errors may cause unexpected mismatches.  
Use `math.isclose(a, b)` for safe comparison.
'''
# Example
import math
a = 0.1 + 0.2
b = 0.3
print(a == b)            # False (tiny rounding error)
print(math.isclose(a, b))  # True



'''
Q6. How can you detect infinite or NaN floats?
Ans:
Use `math.isinf(x)` and `math.isnan(x)` from the math module.
'''
# Example
import math
print(math.isinf(float('inf')))   # True
print(math.isnan(float('nan')))   # True



'''
Q7. Why does Python float have limited precision?
Ans:
Because floats are stored in **binary IEEE-754 format**,  
and some decimal fractions can’t be represented exactly in binary.
'''
# Example
print(0.1 + 0.2)  # 0.30000000000000004



'''
Q8. How can you perform exact decimal arithmetic?
Ans:
Use the `decimal` module, which stores numbers as base-10 decimals.
'''
# Example
from decimal import Decimal
x = Decimal("0.1") + Decimal("0.2")
print(x)  # 0.3 (exact)



'''
Q9. When should you use floats vs Decimal or Fraction?
Ans:
- Use **float** for speed and scientific data.  
- Use **decimal.Decimal** for money or precision-critical cases.  
- Use **fractions.Fraction** for exact rational math.
'''
# Example
from fractions import Fraction
print(Fraction(1, 3) + Fraction(1, 6))  # 1/2 (exact rational)
