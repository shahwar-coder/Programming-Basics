'''
Q1. What does math.trunc(x) do?
Ans:
It returns the **integer part** of a number by removing its fractional portion.  
Unlike rounding, it simply *cuts off* the decimals — no up or down adjustment.
'''
# Example
import math
print(math.trunc(5.9))   # 5
print(math.trunc(-5.9))  # -5
print(math.trunc(3.0))   # 3



'''
Q2. How is math.trunc(x) different from round(x)?
Ans:
- `math.trunc()` just removes the decimal part.  
- `round()` rounds to the nearest integer (using round-half-to-even rule).
'''
# Example
import math
print(math.trunc(2.9), round(2.9))   # 2, 3
print(math.trunc(-2.9), round(-2.9)) # -2, -3



'''
Q3. Is math.trunc(x) the same as int(x)?
Ans:
Yes — they behave identically for numeric types.  
`math.trunc()` is just clearer when you explicitly want to *truncate*.
'''
# Example
import math
x = -3.7
print(int(x))        # -3
print(math.trunc(x)) # -3



'''
Q4. What happens if you pass a non-numeric type to math.trunc()?
Ans:
It raises a `TypeError` unless the object defines `__trunc__()`.
'''



'''
Q5. How is math.trunc() different from math.floor() and math.ceil()?
Ans:
- `math.trunc()` → removes decimals (toward 0)  
- `math.floor()` → rounds down (toward −∞)  
- `math.ceil()` → rounds up (toward +∞)
'''



'''
Q6. Why is math.trunc() useful even though int(x) exists?
Ans:
Because it makes your *intent clear* in mathematical or data-processing code —  
you’re explicitly truncating, not converting types.
'''



'''
Q7. Can math.trunc() be used on complex numbers?
Ans:
No — it raises a `TypeError`.  
Only real numbers and compatible numeric objects are allowed.
'''



'''
Q8. What’s the key takeaway about math.trunc()?
Ans:
It’s a clean, explicit way to drop the fractional part of a number,  
keeping the integer portion intact — *no rounding, just truncation*.
'''
# Example
import math
print(math.trunc(9.999))   # 9
print(math.trunc(-9.999))  # -9
