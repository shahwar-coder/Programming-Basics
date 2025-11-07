'''
Q. Can any() work with generator expressions?
Ans:
Yes — `any()` can take generators, evaluating elements lazily (one by one).
'''
# Example
nums = [0, 0, 2, 4]
print(any(n > 0 for n in nums))  # True
