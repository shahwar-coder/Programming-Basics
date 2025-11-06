'''
Q1. What does math.isfinite(x) do?
Ans:
It checks whether a number is **finite** —  
i.e., not positive infinity, negative infinity, or NaN (Not a Number).
'''
# Example
import math
print(math.isfinite(5.6))        # True
print(math.isfinite(math.inf))   # False
print(math.isfinite(math.nan))   # False

# Example
import math
print(math.isfinite(0))         # True
print(math.isfinite(-3.14))     # True
print(math.isfinite(1e308))     # True



'''
Q2. When does math.isfinite(x) return False?
Ans:
It returns False if `x` is:
- Positive infinity (`math.inf`)
- Negative infinity (`-math.inf`)
- NaN (Not a Number)
'''
# Example
import math
print(math.isfinite(math.inf))     # False
print(math.isfinite(-math.inf))    # False
print(math.isfinite(math.nan))     # False



'''
Q3. How is math.isfinite() different from math.isinf() and math.isnan()?
Ans:
- `math.isfinite(x)` → True for normal numbers  
- `math.isinf(x)` → True for ±infinity  
- `math.isnan(x)` → True for NaN  
Together, they classify any float precisely.
'''
# Example
import math
x = math.inf
print(math.isfinite(x), math.isinf(x), math.isnan(x))  # False True False



'''
Summary:
✅ `math.isfinite(x)` checks if a number is bounded and valid.  
🔹 True → finite real number  
🔹 False → inf, -inf, or nan  
🔹 Prevents invalid results in math-heavy applications.
'''

