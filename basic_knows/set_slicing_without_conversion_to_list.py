'''
Q. What’s a memory-efficient way to slice large sets?
Ans:
- Use itertools.islice() → it lazily slices without converting everything to a list.
'''
from itertools import islice

s = {10, 20, 30, 40, 50}
print(list(islice(s, 2, 4)))  # Slices 2nd to 4th element (in iteration order)
