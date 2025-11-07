'''
Q. How do you include an if–else condition inside list comprehension?
Ans:
1️⃣ **if–else before the `for`** → used to **choose a value** based on a condition
2️⃣ **if after the `for`** → used to **filter items** (no `else` allowed)  
'''
# ------------------------------------------------------------
# Example 1 – if–else **before** for  → conditional value
# ------------------------------------------------------------
nums = [-2, -1, 0, 1, 2]
result = [x if x > 0 else 0 for x in nums]
print(result)   # [0, 0, 0, 1, 2]

# ------------------------------------------------------------
# Example 2 – if **after** for  → conditional filter
# ------------------------------------------------------------
nums = [-2, -1, 0, 1, 2]
positive = [x for x in nums if x > 0]
print(positive)  # [1, 2]
