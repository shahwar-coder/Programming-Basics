'''
- Inserts single item
- At specified Index
- And ofcourse rest of the elements will shift to the right
- index=0, inserting at front
- index=len(list), like appending
- index >= len(list), still will be appended
- you cannot insert multiple items at once, you have to use extend for that
- and negative indices will count from end
- index = -1 , will insert just before the last element
- operation itself will return none, so perform operation separately and then return
- Time Complexity : O(1)
- Try to use other methods or concepts instead like : append, slicing etc. use insert only when positional insertions are truely needed.
'''

# Insert at front (Return None)
nums=[2,3,4]
print(nums.insert(0,1))

# Insert at front (Return Updated List)
nums=[2,3,4]
nums.insert(0,1)
print(nums) # [1, 2, 3, 4]

# Insert in the middle
nums=['a', 'c', 'd']
nums.insert(1,'b')
print(nums) # ['a', 'b', 'c', 'd']

# Insert at last , using exact length index
fruits = ['apple', 'banana']
fruits.insert(2, 'cherry')
print(fruits) # ['apple', 'banana', 'cherry']

# Insert at last using index exceeding the actual len(list)
fruits = ['apple', 'banana']
fruits.insert(84, 'cherry')
print(fruits) # ['apple', 'banana', 'cherry']

# Insert at "just before last" using -1
# Note : Using -1 you cannot insert at last but at the penultimate position.
fruits = ['apple', 'banana']
fruits.insert(-1, 'cherry')
print(fruits) # ['apple', 'banana', 'cherry']

