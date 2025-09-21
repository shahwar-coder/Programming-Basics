'''
Q. Why is choosing the right data structure important?
Ans:
- Impacts performance and clarity.
- Example: searching in list = O(n), searching in set/dict = O(1) average.

Example:
'''
lst = [1,2,3,4,5]
s = {1,2,3,4,5}
print(5 in lst, 5 in s)

# Step-by-step:
# In list: scans sequentially (slower).
# In set: hash lookup (faster).
