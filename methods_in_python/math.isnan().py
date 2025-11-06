'''
Q1. What does math.isnan(x) do?
Ans:
It checks whether a number is **NaN (Not a Number)** —  
a special floating-point value that represents undefined or invalid results.
'''
# Example
import math
print(math.isnan(float('nan')))  # True
print(math.isnan(10.5))          # False



'''
Q2. What is NaN in Python?
Ans:
NaN stands for *Not a Number*.  
It’s used to represent undefined numeric results —  
like `0.0 / 0.0` or invalid floating-point operations.
'''
# Example
import math
x = float('nan')
print(x, math.isnan(x))  # nan True



'''
Q3. What does math.isnan() return?
Ans:
- `True` → if the value is NaN  
- `False` → for any other valid number (finite or infinite)
'''
# Example
import math
print(math.isnan(float('inf')))  # False
print(math.isnan(0.0))           # False
print(math.isnan(float('nan')))  # True



'''
Q4. Why is math.isnan() important?
Ans:
Because NaN values **don’t compare equal** to anything, not even themselves!  
So you can’t use `==` to check for NaN — you must use `math.isnan()`.
'''
# Example
import math
x = float('nan')
print(x == x)          # False  ← NaN never equals itself
print(math.isnan(x))   # True



'''
Q5. How does math.isnan() differ from math.isinf()?
Ans:
- `math.isnan()` → checks for NaN (invalid number).  
- `math.isinf()` → checks for positive or negative infinity.
'''



'''
Q6. Can NaN appear in regular arithmetic?
Ans:
Yes — operations like `0.0 / 0.0`, `inf - inf`, or invalid math operations produce NaN.
'''



'''
Q7. How does NaN behave in comparisons?
Ans:
NaN is **never equal to anything**, even itself.  
`<`, `>`, and `==` all return False when NaN is involved.
'''
# Example
import math
x = float('nan')
print(x == x, x > 0, x < 0)   # False False False
