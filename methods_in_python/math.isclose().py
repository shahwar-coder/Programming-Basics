'''
Q1. What does math.isclose(a, b) do?
Ans:
It checks whether two numbers are **approximately equal**,  
accounting for tiny floating-point errors that occur during calculations.
'''
# Example
import math
print(math.isclose(0.1 + 0.2, 0.3))  # True
print((0.1 + 0.2) == 0.3)            # False (due to rounding)



'''
Q2. Why do we need math.isclose() for floats?
Ans:
Because floating-point numbers can’t represent some decimals exactly,  
small rounding errors occur.  
`math.isclose()` safely compares such values with tolerance.
'''
# Example
import math
a = 0.1 + 0.2
b = 0.3
print(a, b, a == b, math.isclose(a, b))
# Output: 0.30000000000000004 0.3 False True



'''
Q3. What is the syntax of math.isclose()?
Ans:
math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)

- `rel_tol`: relative tolerance (fractional difference allowed)
- `abs_tol`: absolute tolerance (minimum difference allowed)
'''
# Example
import math
print(math.isclose(100.0, 101.0, rel_tol=0.02))  # True (2% difference allowed)
print(math.isclose(5.0, 5.1))                    # False



'''
Q4. What happens if you use math.isclose() with integers?
Ans:
It works fine — integers are converted to floats internally.
'''
# Example
import math
print(math.isclose(10, 10))       # True
print(math.isclose(10, 11))       # False



'''
Q5. How does math.isclose() handle infinities or NaN?
Ans:
- `inf` values are close only if both are the same infinity.  
- `NaN` is never close to anything, including itself.
'''
# Example
import math
print(math.isclose(math.inf, math.inf))   # True
print(math.isclose(math.inf, -math.inf))  # False
print(math.isclose(math.nan, math.nan))   # False



'''
Q6. When should you use math.isclose() in real programs?
Ans:
Use it when comparing:
- Results of floating-point calculations  
- Measurements or scientific data  
- Numbers that might differ due to rounding precision
'''
# Example
import math
area1 = 3.14 * 2 ** 2
area2 = 12.56
print(math.isclose(area1, area2))  # True (approx equal)



'''
Q7. Why is using == unsafe for float comparison?
Ans:
Because floating-point arithmetic introduces microscopic errors —  
so two logically equal results may differ by 1e-16 or less.
'''
# Example
x = 0.3
y = 0.1 + 0.2
print(x == y)         # False
print(math.isclose(x, y))  # True
