'''
Q. How does XOR help *remove duplicates* (find the single unique element)?
Ans:
XOR cancels identical numbers because x ^ x = 0 and x ^ 0 = x. 
If every element appears twice except one, XORing the whole array leaves the unique element.
'''
# Array: [4, 1, 2, 1, 2]
# Goal: find the element that appears once.

# Step 1: Start with result = 0
result = 0

# Step 2: XOR each element into result
result = result ^ 4   # 0 ^ 4 = 4
result = 4 ^ 1        # = 5
result = 5 ^ 2        # = 7
result = 7 ^ 1        # = 6  (because 7 ^ 1 = (4^1) ^ 2 ^ 1 = 4 ^ (1^1) ^ 2 = 4 ^ 0 ^ 2 = 6)
result = 6 ^ 2        # = 4  (2 cancels with earlier 2)

# Final result = 4  → the unique element.
