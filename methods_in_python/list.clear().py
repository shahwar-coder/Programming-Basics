'''
`clear()` → empties the list
'''

# Example 1: Basic usage
nums = [10, 20, 30, 40]
nums.clear()
print(nums)           # []

# Example 2: Clearing an already empty list
lst = []
lst.clear()
print(lst)            # []

# Example 3: Using clear() after modifications
items = ["apple", "banana", "cherry"]
items.pop()
items.clear()
print(items)          # []

# Example 4: Reusing the same list after clearing
data = [1, 2, 3]
data.clear()
data.append(100)
print(data)           # [100]

# Example 5: clear() vs del lst[:]
values = [1, 2, 3]
values.clear()
print(values)         # []
values = [4, 5, 6]
del values[:]
print(values)         # []

# Example 6: Clearing nested lists
matrix = [[1, 2], [3, 4]]
matrix[0].clear()     # clears first sublist only
print(matrix)         # [[], [3, 4]]
