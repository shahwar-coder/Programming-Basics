'''
Q. What if you need a consistent slicing order?
Ans:
- Use sorted() before slicing — this gives a stable, predictable sequence.
'''
s = {50, 10, 30, 40, 20}
print(sorted(s)[1:4])  # [20, 30, 40]
