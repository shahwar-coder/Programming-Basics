'''
Set operation quick lock 🔒 examples
'''

A = {1, 2, 3}
B = {3, 4, 5}

# | → OR (Union): in A or B
print(A | B)
# Output: {1, 2, 3, 4, 5}

# & → AND (Intersection): common in both
print(A & B)
# Output: {3}

# - → ONLY in first (Difference): in A but not in B
print(A - B)
# Output: {1, 2}

# ^ → in one, not both (Symmetric Difference)
print(A ^ B)
# Output: {1, 2, 4, 5}
