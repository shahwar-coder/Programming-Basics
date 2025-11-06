'''
Q1. What does the pow() function do in Python?
Ans:
`pow()` raises a number to a power.  
- `pow(x, y)` computes x ** y  
- `pow(x, y, z)` computes (x ** y) % z efficiently (modular exponentiation)
'''
# Example
print(pow(2, 3))     # 8
print(pow(9, 0.5))   # 3.0
print(pow(2, 5, 3))  # (2 ** 5) % 3 = 32 % 3 = 2



'''
Q2. What is the syntax of pow()?
Ans:
pow(base, exp)  
pow(base, exp, mod) → optional third argument for modular exponentiation.
'''
# Example
print(pow(5, 2))       # 25
print(pow(5, 2, 7))    # 25 % 7 = 4



'''
Q3. How is pow() different from the ** operator?
Ans:
- `pow(x, y)` is the same as `x ** y`.  
- But only `pow(x, y, z)` supports fast modular exponentiation —  
  useful for large numbers and cryptographic calculations.
'''
# Example
x = 2 ** 5       # 32
y = pow(2, 5, 3) # 2 (faster modular version)
print(x, y)



'''important
Q4. What types of numbers does pow() work with?
Ans:
- Works with int and float.  
- The 3-argument form (mod) works only with integers and non-negative exponents.
'''
# Example
print(pow(2, 3.5))   # 11.313...
try:
    print(pow(2.0, 3.0, 5))
except TypeError as e:
    print("Error:", e)
# 11.313708498984761
# Error: pow() 3rd argument not allowed unless all arguments are integers



'''
Q5. Why is pow(x, y, z) preferred for modular arithmetic?
Ans:
It’s much faster than `(x ** y) % z`,  
because it uses **exponentiation by squaring** — efficient even for very large numbers.
'''
# Example
# Regular power → slower for large exponents
# pow() → optimized
# pow(x, y, z) is faster because it uses modular exponentiation (exponentiation by squaring), 
# applying the modulus at each step to avoid large intermediate results.
print((2 ** 10) % 3)   # slower way
print(pow(2, 10, 3))   # faster, same result → 1



'''
Q6. What happens when using negative exponents?
Ans:
For two arguments, `pow(x, -n)` returns 1 / (x ** n) as a float.  
In the 3-argument form, negative exponents are not allowed.
'''
# Example
print(pow(2, -3))    # 0.125
try:
    print(pow(2, -3, 5))
except ValueError as e:
    print("Error:", e)



'''
Q7. How does pow() handle type conversion?
Ans:
If all arguments are integers, result is int.  
If any is float, result becomes float automatically.
'''
# Example
print(pow(3, 2))       # 9 (int)
print(pow(3.0, 2))     # 9.0 (float)



'''
Q8. What errors can pow() raise?
Ans:
- `TypeError` → if arguments have invalid types (e.g., float with mod).  
- `ValueError` → if exponent is negative in 3-argument form.
'''
# Example
try:
    print(pow(2.0, 3.0, 5))
except TypeError as e:
    print("Error:", e)



'''
Q9. When should you prefer pow() over **?
Ans:
Use `pow()` when:
- You need modular results.  
- You want optimized performance for large exponents.  
- You need modular inverse computations (from Python 3.8+).
'''



'''
Q10. Why is pow() often used in cryptography?
Ans:
Because modular exponentiation is the core of many crypto algorithms  
like RSA — it handles huge exponents securely and efficiently.
'''
