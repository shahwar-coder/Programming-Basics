'''
Q. How can XOR *swap two numbers* without a temporary variable?
Ans:
Using XOR three times swaps values because XOR is reversible and uses no extra storage.
'''
# Let a = 9 (1001), b = 5 (0101)

# Step 1: a = a ^ b
a = 9 ^ 5 = 12   # (1001 ^ 0101 = 1100)

# Step 2: b = a ^ b    (now a is 12)
b = 12 ^ 5 = 9    # (1100 ^ 0101 = 1001) → original a

# Step 3: a = a ^ b    (now b is original a)
a = 12 ^ 9 = 5     # (1100 ^ 1001 = 0101) → original b

# Final: a = 5, b = 9  (values swapped)

# ==== CODE ====

# XOR Swap in Python

a = 9
b = 5

print("Before swap:")
print("a =", a, "b =", b)

# Step 1
a = a ^ b
# Step 2
b = a ^ b
# Step 3
a = a ^ b

print("\nAfter swap:")
print("a =", a, "b =", b)

# OUTPUT:
# Before swap:
# a = 9 b = 5

# After swap:
# a = 5 b = 9
