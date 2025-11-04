'''
Q. How does zip() behave when iterables have different lengths?
Ans:
It stops at the shortest iterable — extra elements in longer ones are ignored.
'''
# Example
a = [1, 2, 3]
b = ["x", "y"]
print(list(zip(a, b)))    # [(1, 'x'), (2, 'y')]
