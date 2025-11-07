'''
`extend(iterable)` → adds multiple elements from another iterable
'''

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

# Example 5: Extending an empty list
empty = []
empty.extend([100, 200])
print(empty)       # [100, 200]

# Example 6: Extending with range()
values = [0]
values.extend(range(1, 5))
print(values)      # [0, 1, 2, 3, 4]

# Example 7: Extending with another list variable
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)           # [1, 2, 3, 4, 5, 6]

# Example 8: Using += (works same as extend)
nums = [1, 2, 3]
nums += [7, 8, 9]
print(nums)        # [1, 2, 3, 7, 8, 9]
