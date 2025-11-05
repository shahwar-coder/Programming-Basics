'''
Q. Why is pow(x, y, z) preferred for modular arithmetic?
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
