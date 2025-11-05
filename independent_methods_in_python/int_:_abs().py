'''
Q1. What does the abs(x) function do in Python?
Ans:
`abs(x)` returns the absolute (non-negative) value of a number.  
If x is complex, it returns its magnitude (distance from origin).
'''
# Example
print(abs(-10))     # 10
print(abs(-3.14))   # 3.14
print(abs(3 + 4j))  # 5.0



'''
Q2. What types of values can abs() handle?
Ans:
It works with:
- Integers → abs(-5) = 5  
- Floats → abs(-3.2) = 3.2  
- Complex numbers → abs(3 + 4j) = 5.0
'''



'''
Q3. How does abs() work internally?
Ans:
It calls the object’s `__abs__()` method.  
That means user-defined classes can override this method  
to define custom absolute behavior.
'''
# Example
class Box:
    def __init__(self, w): self.w = w
    def __abs__(self): return f"Box size: {self.w}"

b = Box(10)
print(abs(b))    # Box size: 10



'''
Q4. What are some common uses of abs()?
Ans:
- Getting distance or magnitude  
- Comparing numbers with tolerance (`abs(a - b) < ε`)  
- Normalizing data  
- Working with vector or complex magnitudes
'''
# Example
a, b = 10.2, 10.0
if abs(a - b) < 0.5:
    print("Close enough!")



'''
Q5. How does abs() handle complex numbers?
Ans:
For complex `z = a + bj`, it returns `√(a² + b²)` —  
the magnitude (distance from the origin in the complex plane).
'''
# Example
z = 3 + 4j
print(abs(z))   # √(3² + 4²) = 5.0



'''
Q6. What happens if abs() is called on a non-numeric type?
Ans:
It raises a `TypeError` unless the object defines a custom `__abs__()` method.
'''
# Example
try:
    print(abs("hello"))
except TypeError as e:
    print("Error:", e)



'''
Q7. Can abs() be customized for user-defined classes?
Ans:
Yes — by defining the `__abs__()` method inside your class.  
Then calling abs(obj) will invoke that method.
'''
# Example
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5

v = Vector(3, 4)
print(abs(v))   # 5.0




'''
Q8. What’s the difference between abs() and math.fabs()?
Ans:
- `abs()` works with int, float, and complex.  
- `math.fabs()` works only with real numbers (float/int).  
`math.fabs()` always returns a float.
'''
# Example
import math
print(abs(-5), math.fabs(-5))   # 5 5.0
print(abs(3+4j))                # 5.0
# math.fabs(3+4j) → TypeError



'''
Q9. Is abs() affected by negative zero in floats?
Ans:
No — `abs(-0.0)` returns `0.0`.  
Python treats +0.0 and -0.0 as equal in numeric comparisons.
'''
# Example
print(abs(-0.0))   # 0.0
print(abs(0.0))    # 0.0
