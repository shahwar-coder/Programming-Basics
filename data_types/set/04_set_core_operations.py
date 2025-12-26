'''
Q1. What is union (`a | b`) in sets?
Ans. Union returns ALL unique elements that are in set `a` OR set `b`.
'''
# Example
a = {1, 2, 3}
b = {3, 4, 5}
a | b
# Output: {1, 2, 3, 4, 5}


'''
Q2. What is intersection (`a & b`) in sets?
Ans. Intersection returns ONLY the elements that are common to both sets.
'''
# Example
a = {1, 2, 3}
b = {3, 4, 5}
a & b
# Output: {3}


'''
Q3. What is difference (`a - b`) in sets?
Ans. Difference returns elements that are in `a` but NOT in `b`.
'''
# Example
a = {1, 2, 3}
b = {3, 4}
a - b
# Output: {1, 2}


'''
Q4. Is set difference directional?
Ans. Yes. `a - b` is different from `b - a`.
'''
# Example
b - a
# Output: {4}


'''
Q5. What is symmetric difference (`a ^ b`)?
Ans. It returns elements that are in either set, but NOT in both.
'''
# Example
a = {1, 2, 3}
b = {3, 4, 5}
a ^ b
# Output: {1, 2, 4, 5}


'''
Q6. Why are these operations useful?
Ans. They help compare groups, find overlaps, and remove duplicates efficiently.
'''
# Example
# Common students → intersection
# All students → union
# Missing students → difference


'''
Q7. Do these operations change the original sets?
Ans. No. They return new sets and keep the originals unchanged.
'''
# Example
c = a | b
# a and b remain the same


'''
Q8. What is the one-line rule to remember?
Ans. Set operations let you combine, compare, and separate data using math-like symbols.
'''
# Example (lock it 🔒)
# | → OR
# & → AND
# - → ONLY in first
# ^ → in one, not both
