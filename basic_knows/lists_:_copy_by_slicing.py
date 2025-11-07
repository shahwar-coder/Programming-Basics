L1 = [10, 20, 30, 40]

# Copy by slicing
L2 = L1[:]

print("Original:", L1)
print("Copy:", L2)
print("Same object?", L1 is L2)     # False (different lists)
