'''
Q. What if the original order must be preserved?
Ans:
- Use dict.fromkeys(), which preserves insertion order since Python 3.7+.
'''
nums = [1, 2, 2, 3, 3, 1]
unique_ordered = list(dict.fromkeys(nums)) # dict.fromkeys(nums) -> {1: None, 2: None, 3: None}
print(unique_ordered)  # [1, 2, 3]
