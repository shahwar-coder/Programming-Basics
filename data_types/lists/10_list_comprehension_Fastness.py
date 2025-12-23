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

# List comprehension is faster because the looping and list construction are implemented in optimized C code inside CPython. 
# It avoids repeated Python-level operations like method lookups and function calls (append), 
# reduces interpreter overhead, 
# and allocates memory more efficiently.
# ======
# List comprehension is faster because Python does most of the work behind the scenes in very fast C code.
# Instead of running each step slowly in Python again and again, Python handles the looping and list creation in one optimized block.
# It also avoids extra work like repeatedly finding and calling the append() function for every item. Because of this, Python has less interpreter overhead (less “thinking work”), and it can create the list more efficiently in memory.
# As a result, list comprehensions usually run faster than normal for loops.
