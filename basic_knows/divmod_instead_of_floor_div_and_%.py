'''
Q. Is divmod() faster than using // and % separately?
Ans:
Yes — Python computes both values in a single C-level operation,  
so it’s slightly faster and more efficient.
'''

'''
Q. How is divmod() related to floor division and modulus?
Ans:
It’s equivalent to performing both at once:  
`divmod(a, b) == (a // b, a % b)`  
but slightly more efficient since it computes both in one step.
'''
# Example
a, b = 9, 4
print(divmod(a, b))          # (2, 1)
print((a // b, a % b))       # (2, 1)
