'''
`insert(index, value)` → adds element at a specific position
'''
# Example 1: Basic insertion
lst = [1, 2, 3]
lst.insert(2, 99)
print(lst)       # [1, 2, 99, 3]

# Example 2: Insert at beginning (index = 0)
nums = [10, 20, 30]
nums.insert(0, 5)
print(nums)      # [5, 10, 20, 30]

# Example 3: Insert at end (index >= len(list))
letters = ['a', 'b', 'c']
letters.insert(10, 'z')   # beyond length → appends at end
print(letters)    # ['a', 'b', 'c', 'z']

# Example 4: Insert negative index (counts from right)
data = [100, 200, 300, 400]
data.insert(-1, 350)
print(data)       # [100, 200, 300, 350, 400]

# Example 5: Insert lists or other objects
nums = [1, 2, 3]
nums.insert(1, [7, 8])
print(nums)       # [1, [7, 8], 2, 3]  (list inserted as a single element)

# Example 6: Insert strings into a list
words = ["Python", "fun"]
words.insert(1, "is")
print(words)      # ['Python', 'is', 'fun']

# Example 7: Insert repeatedly at same index
colors = ['red']
colors.insert(0, 'green')
colors.insert(0, 'blue')
print(colors)     # ['blue', 'green', 'red']
