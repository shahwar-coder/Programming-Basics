'''
Q1. What does the + operator do with lists?
Ans:
It **concatenates** (joins) two or more lists into a new one.  
The original lists remain unchanged.
'''
# Example
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)  # [1, 2, 3, 4, 5, 6]
print(a)  # [1, 2, 3]  (unchanged)



'''
Q2. What does the * operator do with lists?
Ans:
It **repeats** the elements of the list a given number of times.  
This creates a new list without modifying the original.
'''
# Example
nums = [1, 2]
print(nums * 3)    # [1, 2, 1, 2, 1, 2]
print(['Hi'] * 4)  # ['Hi', 'Hi', 'Hi', 'Hi']



'''
Q6. What is the difference between sort() and sorted()?
Ans:
- `sort()` → modifies the list **in-place**, returns None.  
- `sorted(iterable)` → returns a **new sorted list**, leaving the original unchanged.
'''

# Example
nums = [5, 3, 1, 4, 2]

# Using sorted() → returns a new list
new_list = sorted(nums)
print("Original list:", nums)       # [5, 3, 1, 4, 2]
print("Sorted copy: ", new_list)    # [1, 2, 3, 4, 5]

# Using sort() → changes the same list
nums.sort()
print("After sort():", nums)        # [1, 2, 3, 4, 5]
