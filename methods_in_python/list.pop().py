'''
`pop([index])` → removes and returns an element (default: last)
'''

# Example 1: Remove last element (default behavior)
nums = [10, 20, 30, 40]
removed = nums.pop()
print(nums)          # [10, 20, 30]
print(removed)       # 40

# Example 2: Remove element at specific index
nums = [1, 2, 3, 4, 5]
removed = nums.pop(2)
print(nums)          # [1, 2, 4, 5]
print(removed)       # 3

# Example 3: Pop first element (index 0)
lst = ['a', 'b', 'c', 'd']
lst.pop(0)
print(lst)           # ['b', 'c', 'd']

# Example 4: Using pop() in a loop
stack = [1, 2, 3]
while stack:
    print(stack.pop())   # removes from end → 3, 2, 1
print(stack)             # []

# Example 5: Pop from nested list
matrix = [[1, 2], [3, 4], [5, 6]]
row = matrix.pop(1)
print(row)           # [3, 4]
print(matrix)        # [[1, 2], [5, 6]]

# Example 6: Negative index with pop()
nums = [10, 20, 30, 40]
nums.pop(-2)
print(nums)          # [10, 20, 40]

# Example 7: Error if list is empty
empty = []
# empty.pop()        # IndexError: pop from empty list
