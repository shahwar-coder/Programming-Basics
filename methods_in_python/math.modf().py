'''
Q1. What does math.modf(x) do?
Ans:
It splits a number into its **fractional** and **integer** parts,  
returning a tuple `(fractional_part, integer_part)` — both as floats.
'''
# Example
import math
print(math.modf(5.75))   # (0.75, 5.0)
print(math.modf(-3.25))  # (-0.25, -3.0)
print(math.modf(7.0))    # (0.0, 7.0)



'''
Q2. What is the return type of math.modf()?
Ans:
It always returns a **tuple of two floats**,  
even if the input was an integer or a float without a fraction.
'''
# Example
import math
print(math.modf(10))   # (0.0, 10.0)
print(type(math.modf(10)[0]), type(math.modf(10)[1]))  # both float



'''
Q3. How does math.modf() handle negative numbers?
Ans:
Both returned parts carry the same **sign** as the input.  
For example, `math.modf(-3.25)` → (-0.25, -3.0)
'''
# Example
import math
print(math.modf(-3.25))  # (-0.25, -3.0)



'''
Q5. When is math.modf() useful?
Ans:
It’s helpful when you need both integer and fractional components —  
for example in rounding, normalization, or splitting real numbers.
'''
# Example
import math
fraction, whole = math.modf(12.345)
print(f"Fraction: {fraction}, Whole: {whole}")  # Fraction: 0.345, Whole: 12.0



'''
Q6. How does math.modf() behave with infinity or NaN?
Ans:
- For `math.inf` → returns (0.0, inf)  
- For `math.nan` → returns (nan, nan)
'''
# Example
import math
print(math.modf(math.inf))  # (0.0, inf)
print(math.modf(math.nan))  # (nan, nan)



'''
Q7. Why is math.modf() more precise than manually using int(x) or x % 1?
Ans:
Because it works directly on floating-point representations,  
avoiding rounding errors from subtraction or modulo operations.
'''
# Example
import math
x = 3.99999999999999
print(math.modf(x))     # (0.99999999999999, 3.0)
print(x - int(x))       # Might lose precision



'''
Q8. Summary:
Ans:
- Splits float into (fraction, integer).  
- Preserves sign for both.  
- Both results are floats.  
- Safer, more precise, and cleaner than manual splitting.
'''
