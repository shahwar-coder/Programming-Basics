'''
- removes 1st Occurence of a specific mentioned value from the list.
- modifies/mmutates original list.
- operation itself return none.
- if first matching item is found, it stops further search.
- it is value based meaning, it searches by equality (==) not identity (is)
- raises Valueerror if specified value is not found.
- time complexity : O(n) in the worst case as it may scan through the whole list to find the element and then delete.
- To Remove ALL Occurrences : Use list comprehension.
'''

# Removal
nums=[1,2,3,4,5]
nums.remove(4)
print(nums) # [1, 2, 3, 5]

# Removal
fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana')
print(fruits) # ['apple', 'cherry']

# See error on missing value
data=[1,2,3,4,5]
data.remove(7) # ValueError: list.remove(x): x not in list
