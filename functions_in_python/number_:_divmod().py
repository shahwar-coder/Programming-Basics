'''
Q1. What does the divmod(a, b) function do?
Ans:
It performs division and modulus together, returning a tuple:  
(quotient, remainder) → same as `(a // b, a % b)`.
'''
# Example 1
print(divmod(7, 3))   # (2, 1)
print(divmod(8.5, 2.5))  # (3.0, 1.0)

# Example 2
q, r = divmod(10, 4)
print("Quotient:", q, "Remainder:", r)
# Output: Quotient: 2 Remainder: 2



'''
Q3. How is divmod() related to floor division and modulus?
Ans:
It’s equivalent to performing both at once:  
`divmod(a, b) == (a // b, a % b)`  
but slightly more efficient since it computes both in one step.
'''
# Example
a, b = 9, 4
print(divmod(a, b))          # (2, 1)
print((a // b, a % b))       # (2, 1)



'''
Q4. What types of numbers does divmod() support?
Ans:
- Works with integers → integer results  
- Works with floats → float results  
(But mixing types converts everything to float.)
'''



'''
Q5. What are common uses of divmod()?
Ans:
- Time formatting (seconds → minutes, seconds)  
- Base conversions (e.g., number → digits)  
- Efficient combined division and remainder calculation
'''
# Example
minutes, seconds = divmod(125, 60)
print(minutes, "min", seconds, "sec")   # 2 min 5 sec



'''
Q6. How does divmod() handle negative numbers?
Ans:
It follows *floor division* rules:  
The quotient is rounded toward negative infinity,  
and the remainder has the same sign as the divisor.
'''
# Example
print(divmod(-7, 3))   # (-3, 2)
print(divmod(7, -3))   # (-3, -2)



'''
Q7. Can divmod() be used with complex numbers?
Ans:
No — it raises a `TypeError`.  
divmod() works only with real (int/float) numbers.
'''
# Example
try:
    print(divmod(4 + 2j, 2))
except TypeError as e:
    print("Error:", e)



'''
Q8. Is divmod() faster than using // and % separately?
Ans:
Yes — Python computes both values in a single C-level operation,  
so it’s slightly faster and more efficient.
'''
