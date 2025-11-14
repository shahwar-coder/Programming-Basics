'''
Q1. What are Python's most commonly used built-in math functions?
Ans:
min(), max(), abs(), and pow() are built-in numeric helpers that work 
without importing any module.
'''
# Example
print(min(3, 1, 2))   # 1
print(abs(-7))        # 7


'''
Q2. How does pow(x, y) differ from x ** y?
Ans:
Both compute exponentiation, but pow(x, y) also supports a third argument 
pow(x, y, mod) for efficient modular exponentiation.
'''
# Example
print(pow(2, 5))          # 32
print(pow(2, 5, 3))       # 2   (32 % 3)


'''
Q3. When should you import the math module?
Ans:
Import math when you need advanced mathematical functions like 
sqrt(), ceil(), floor(), log(), trig functions, constants, etc.
'''
# Example
import math
print(math.sqrt(25))      # 5.0


'''
Q4. What is the difference between math.ceil(x) and math.floor(x)?
Ans:
ceil() → rounds number UP to nearest integer  
floor() → rounds number DOWN to nearest integer
'''
# Example
print(math.ceil(3.2))     # 4
print(math.floor(3.8))    # 3


'''
Q5. What mathematical constants does math provide?
Ans:
Common ones include:
math.pi → π  
math.e  → Euler’s number  
math.tau → 2π  
These are precise constants used in math and science.
'''
# Example
print(math.pi)   # 3.141592653589793


'''
Q6. Why use math functions instead of manual calculations?
Ans:
math module is implemented in optimized C code,
ensuring precision, speed, and reliability.
Avoids bugs from manual rounding or custom logic.
'''
# Example
print(math.sqrt(2))  # precise √2


'''
Q7. What happens if you call math.sqrt() with a negative number?
Ans:
math.sqrt(-x) raises a ValueError because real square roots 
for negative numbers don't exist.  
Use cmath.sqrt() for complex results.
'''
# Example
# math.sqrt(-1)  # ValueError


'''
Q8. What is the difference between abs() and math.fabs()?
Ans:
abs()  → returns int for ints; float for floats  
fabs() → always returns float  
'''
# Example
print(abs(-5))         # 5
print(math.fabs(-5))   # 5.0


'''
Q9. How does Python handle very large integers in math functions?
Ans:
Python's int has unlimited precision, but math functions 
(use floats internally) may lose precision for very large values.
'''
# Example
print(abs(10**100))        # precise
# math.sqrt(10**100)        # may lose precision


'''
Q10. When is pow(x, y, mod) essential?
Ans:
Useful in cryptography, modular arithmetic, hashing, coding competitions.
Uses fast modular exponentiation (O(log y)), 
much faster than (x**y) % mod.
'''
# Example
print(pow(2, 1000, 13))   # very fast
