'''
Q. How are sets used to compare collections?
Ans. Using set operations like union, intersection, and difference.
'''
# Example
a = {1, 2, 3}
b = {3, 4}
a & b   # {3}   → common
a | b   # {1, 2, 3, 4} → all
a - b   # {1, 2} → only in a
