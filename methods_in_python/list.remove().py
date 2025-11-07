'''
`remove(value)` → removes the first occurrence of a value
'''

# Example 1: Basic usage
nums = [10, 20, 30, 20, 40]
nums.remove(20)
print(nums)           # [10, 30, 20, 40]  (only first 20 removed)

# Example 2: Removing a string
words = ["apple", "banana", "cherry"]
words.remove("banana")
print(words)          # ['apple', 'cherry']

# Example 3: Removing from mixed list
data = [1, "a", 2, "b", 3]
data.remove("a")
print(data)           # [1, 2, "b", 3]

# Example 4: Removing nested element (as a full object)
lst = [[1, 2], [3, 4], [5, 6]]
lst.remove([3, 4])
print(lst)            # [[1, 2], [5, 6]]

# Example 5: Removing inside a loop (⚠️ use with caution)
values = [1, 2, 3, 2, 4]
while 2 in values:
    values.remove(2)
print(values)         # [1, 3, 4]

# Example 6: Trying to remove non-existing value → error
nums = [1, 2, 3]
# nums.remove(10)     # ValueError: list.remove(x): x not in list
