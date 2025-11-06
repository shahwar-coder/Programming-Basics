'''
Q1. What are complex numbers in Python?
Ans:
They represent numbers with **real and imaginary parts**,  
written as `a + bj` (where `j` is √(-1)).  
Python’s built-in type for these is `complex`.
'''
# Example
z1 = 3 + 4j
z2 = complex(2, -3)
print(z1, z2)  # (3+4j) (2-3j)



'''
Q2. How do you access the real and imaginary parts?
Ans:
Use the attributes `.real` and `.imag`,  
both always return **floats**, even if you started with ints.
'''
# Example
z = 3 + 4j
print(z.real)   # 3.0
print(z.imag)   # 4.0



'''
Q3. What operations are supported for complex numbers?
Ans:
Complex numbers fully support:
`+`, `-`, `*`, `/`, and `==`  
All results stay complex unless imaginary part is zero.
'''
# Example
z1, z2 = (3+4j), (1-2j)
print(z1 + z2)  # (4+2j)
print(z1 * z2)  # (11-2j)
print(z1 / z2)  # (-1+2j)



'''
Q4. Which built-in functions work with complex numbers?
Ans:
- `abs(z)` → magnitude (√(a² + b²))  
- `complex(a, b)` → construct number  
- `z.conjugate()` → mirror across real axis (a − bj)
'''
# Example
z = 3 + 4j
print(abs(z))            # 5.0
print(z.conjugate())     # (3-4j)
print(complex(5, -2))    # (5-2j)



'''
Q5. What is the cmath module used for?
Ans:
The `cmath` module provides **mathematical functions for complex numbers**,  
like `sqrt`, `exp`, `polar`, `rect`, and `phase`.
'''
# Example
import cmath
z = 3 + 4j
print(cmath.phase(z))   # 0.927... (angle in radians)
print(cmath.polar(z))   # (5.0, 0.927...)
print(cmath.rect(5, 0.927))  # (3.000...+4.000...j)



'''
Q6. What is the difference between math and cmath modules?
Ans:
- `math` → works only with **real** numbers.  
- `cmath` → handles **complex** numbers.  
Using math functions on complex values raises a `TypeError`.
'''



'''
Q7. What does abs(z) represent geometrically?
Ans:
It gives the **magnitude (distance from origin)** in the complex plane:  
`abs(a + bj) = √(a² + b²)`.
'''
# Example
z = 6 + 8j
print(abs(z))  # 10.0




'''
Q8. How do conjugates help in division of complex numbers?
Ans:
Conjugates simplify division by removing the imaginary part from the denominator.  
Python handles this internally, but conceptually it uses `(a+bi)(a−bi) = a²+b²`.
'''
# Example
z1, z2 = (3+4j), (1-2j)
print(z1 / z2)  # (-1+2j) — computed using conjugate internally
