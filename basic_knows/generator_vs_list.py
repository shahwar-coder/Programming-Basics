'''
Q. What is the key difference between a generator and a list?
A.
A list stores all values in memory immediately,
whereas a generator computes values lazily, one at a time.
'''
# Example:
# [x for x in range(1000000)]   # high memory usage
# (x for x in range(1000000))   # constant memory
