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



'''
Q. How does NaN behave in comparisons?
Ans:
NaN is **never equal to anything**, even itself.  
`<`, `>`, and `==` all return False when NaN is involved.
'''
# Example
import math
x = float('nan')
print(x == x, x > 0, x < 0)   # False False False

