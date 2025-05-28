'''
- returns index postion
- of the 1st occurrence of a specified value in the list
- search happens left to right
- you can limit the search to specific sub range using 'start' and 'end'
- ValueError will be raised if value is not found
- time complexity : O(n) - worst case is scanning the list.
- efficient when list is short and value is possibly near the beginning
'''

# Simple
fruits = ['apple', 'banana', 'cherry', 'banana']
print(fruits.index("cherry")) # 2

# With start argument
print(fruits.index("cherry", 0)) # search starts from 0th index
print(fruits.index("cherry", 1)) # search starts from 1st index
print(fruits.index("cherry", 2)) # here search will start from 3rd index, here it is cerry itself
# print(fruits.index("cherry", 3)) # here cherry won't be found now, start=3, ValueError: 'cherry' is not in list
# above all outputs = 2

# With Start and End:
print(fruits.index("cherry", 1, len(fruits)))

# Trick to avoid ValueError in general:
if "cherry" in fruits:
    position=fruits.index("cherry")
    print("Position = ", position)

# Trick to get all indices/occurences of cherry
fruits=["apple", "banana", "cherry", "guava", "cherry"]
all_indices=[i for i,fruit in enumerate(fruits) if fruit=="cherry"]
print(f"All indices having cherry : {all_indices}")
