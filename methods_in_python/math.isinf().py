'''
Q1. What does math.isinf(x) do?
Ans:
It checks whether a number is **infinite**,  
i.e., equal to positive or negative infinity.  
Returns `True` for infinities and `False` otherwise.
'''
# Example
import math
print(math.isinf(float('inf')))   # True
print(math.isinf(float('-inf')))  # True
print(math.isinf(10.5))           # False
# NOTE : float('inf') creates +ve infinite value
# NOTE : float('-inf') creates -ve infinite value



'''
Q2. What does infinity mean in floating-point numbers?
Ans:
Infinity (`inf`) represents a value **too large** to fit in normal float range,  
usually caused by overflow or division by zero in floating-point arithmetic.
'''
print(1e308 * 1e308)   # inf (overflow)



'''
Q3. What values make math.isinf() return True?
Ans:
It returns `True` for:
- `float('inf')`
- `float('-inf')`
- results of operations that overflow to infinity
'''
# Example
import math
print(math.isinf(float('inf')))   # True
print(math.isinf(float('-inf')))  # True
print(math.isinf(-float('inf')))  # True



'''
Q4. How can infinity be created in Python?
Ans:
- Using `float('inf')` or `float('-inf')`  
- From arithmetic overflow (`1e308 * 1e308`)  
- From division by zero in floating-point (`1.0 / 0.0`) in some contexts
'''
# Example
import math
print(float('inf'), -float('inf'))
print(1e308 * 1e308)  # inf



'''
Q7. What happens in comparisons with infinity?
Ans:
Infinity behaves as expected in numeric comparisons:
- `float('inf') > any finite number` → True  
- `float('-inf') < any finite number` → True
'''
# Example
print(float('inf') > 9999999999999999)   # True
print(float('-inf') < -9999999999999999) # True



'''
Q8. What happens if you perform arithmetic with infinity?
Ans:
Infinity propagates in operations —  
any operation involving infinity tends to result in infinity (unless invalid).
'''
# Example
print(float('inf') * 2)       # inf
print(float('inf') - 1e300)   # inf
print(float('inf') - float('inf'))  # nan (undefined)
