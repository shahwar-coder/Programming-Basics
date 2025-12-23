'''
Q1. Why are tuples called fixed-size?
Ans. Because their size is decided at creation and cannot be changed later.
'''

# Tuples are called fixed-size because their length is decided at creation
# and cannot be changed later.

# If you try to add or modify elements, Python does NOT change the
# original tuple. Instead, it creates a completely new tuple.

# The original tuple always remains the same.

tup = (1, 2, 3)
new_tup = tup + (4,)

print(tup)      # (1, 2, 3)
print(new_tup)  # (1, 2, 3, 4)
