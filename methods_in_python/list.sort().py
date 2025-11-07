'''
Q1. What does sort() do in lists?
Ans:
`sort()` arranges list elements in **ascending order by default**.  
It modifies the list **in-place** and returns `None`.
'''

# Example 1: Basic sorting (ascending)
nums = [5, 2, 9, 1]
nums.sort()
print(nums)        # [1, 2, 5, 9]

# Example 2: Sorting in descending order
nums = [10, 3, 7, 1]
nums.sort(reverse=True)
print(nums)        # [10, 7, 3, 1]

# Example 3: Sorting strings alphabetically
words = ["banana", "apple", "cherry"]
words.sort()
print(words)       # ['apple', 'banana', 'cherry']

# Example 4: Sorting strings in reverse alphabetical order
words.sort(reverse=True)
print(words)       # ['cherry', 'banana', 'apple']

# Example 5: Sorting with a custom key — by string length
fruits = ["apple", "kiwi", "banana", "fig"]
fruits.sort(key=len)
print(fruits)      # ['fig', 'kiwi', 'apple', 'banana']

# Example 6: Sorting numbers by their remainder when divided by 3
nums = [10, 7, 8, 11, 14]
nums.sort(key=lambda x: x % 3)
print(nums)        # [9, 12, 6, 15] → actually [9, 12, 6, 15] but depends on remainder order

# Example 7: Sorting tuples by second element
pairs = [(2, 5), (1, 3), (4, 1)]
pairs.sort(key=lambda x: x[1])
print(pairs)       # [(4, 1), (1, 3), (2, 5)]

# Example 8: Sorting mixed-case strings (case-sensitive)
names = ["Zebra", "apple", "Banana"]
names.sort()
print(names)       # ['Banana', 'Zebra', 'apple']  (uppercase < lowercase)

# Example 9: Case-insensitive sorting
names.sort(key=str.lower)
print(names)       # ['apple', 'Banana', 'Zebra']
