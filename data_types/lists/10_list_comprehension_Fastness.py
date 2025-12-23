'''
Q1. Why is list comprehension faster than a normal loop?
Ans. Because it runs at C-level internally and avoids repeated Python overhead.
'''
# Example (slower)
result = []
for x in range(5):
    result.append(x * x)

# Example (faster)
result = [x * x for x in range(5)]


'''
Q2. When should you prefer list comprehension?
Ans. When transforming or filtering lists in a clean, readable, one-line way.
'''
# Example
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]
