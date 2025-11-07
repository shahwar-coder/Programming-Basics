'''
Q. How can you use all() with generators?
Ans:
You can pair it with generator expressions for memory-efficient checks.
'''
# Example
nums = [2, 4, 6, 8, 10]
print(all(n % 2 == 0 for n in nums))  # True
