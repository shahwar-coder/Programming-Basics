'''
Q. What is an important limitation of generators?
A.
Once a generator is exhausted, it cannot be reused and must be recreated.
'''
# Example:
# gen = (x for x in range(2))
# list(gen)  # [0, 1]
# list(gen)  # []  (already exhausted)
