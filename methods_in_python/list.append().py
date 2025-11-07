'''
`append(x)` → adds one element at the **end**
'''

# Example 1: Basic usage
lst = [1, 2, 3]
lst.append(4)
print(lst)           # [1, 2, 3, 4]

# Example 2: Appending strings
words = ["Python", "is"]
words.append("fun")
print(words)         # ['Python', 'is', 'fun']

# Example 3: Appending a list (adds as a single element)
nums = [1, 2, 3]
nums.append([4, 5])
print(nums)          # [1, 2, 3, [4, 5]]

# Example 4: Appending different data types
data = []
data.append(10)
data.append("Hello")
data.append(3.14)
print(data)          # [10, 'Hello', 3.14]

# Example 5: Appending inside a loop
squares = []
for i in range(1, 6):
    squares.append(i**2)
print(squares)       # [1, 4, 9, 16, 25]

# Example 6: Appending tuples or sets
items = [1, 2]
items.append((3, 4))
items.append({5, 6})
print(items)         # [1, 2, (3, 4), {5, 6}]

# Example 7: Nested append (building 2D lists)
matrix = []
for i in range(3):
    matrix.append([i, i+1])
print(matrix)        # [[0, 1], [1, 2], [2, 3]]
