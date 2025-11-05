'''
Q. What happens when using negative exponents?
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
