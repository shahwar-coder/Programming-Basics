'''
Q. Why is math.isnan() important?
Ans:
Because NaN values **don’t compare equal** to anything, not even themselves!  
So you can’t use `==` to check for NaN — you must use `math.isnan()`.
'''
# Example
import math
x = float('nan') # creating a nan
print(x == x)          # False  ← NaN never equals itself
print(math.isnan(x))   # True
