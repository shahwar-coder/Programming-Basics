'''
Q1. What does .conjugate() do for a complex number?
Ans:
It returns the **complex conjugate**,  
which flips the sign of the imaginary part:  
`(a + bj).conjugate()` → `(a - bj)`
'''
# Example
z = 3 + 4j
print(z.conjugate())  # (3-4j)



'''
Q2. How do conjugates help simplify division of complex numbers?
Ans:
They remove the imaginary part from the denominator using:  
`(a + bj)/(c + dj) × (c - dj)/(c - dj)`
'''
# Example
z1, z2 = 3 + 4j, 1 - 2j
manual = (z1 * z2.conjugate()) / (z2 * z2.conjugate()).real
print(manual)  # (-1+2j)

