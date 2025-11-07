# Example 1: Extending with another list
lst = [1, 2, 3]
lst.extend([4, 5, 6])
print(lst)         # [1, 2, 3, 4, 5, 6]

# Example 2: Extending with a tuple
nums = [10, 20]
nums.extend((30, 40, 50))
print(nums)        # [10, 20, 30, 40, 50]

# Example 3: Extending with a string → adds each character separately
chars = ['A', 'B']
chars.extend('CD')
print(chars)       # ['A', 'B', 'C', 'D']

# Example 4: Extending with a set → order is not guaranteed
data = [1, 2]
data.extend({3, 4})
print(data)        # [1, 2, 3, 4] (order may vary)
