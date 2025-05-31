'''
- count()
- returns no:of times a specific value occurs in the list
- basically frequency
- can return 0 as well ,if number not present
- hence no error if not found
- time complexity : O(n) : as it has to scan whole list to count occurrences.
- fast for small lists but you need to avoid it for large, it will bring slowness.
'''

# Simple (with strings)
colors = ['red', 'blue', 'red', 'green', 'red']
print(f"Red count : {colors.count('red')}")
print(f"Blue count : {colors.count('blue')}")
print(f"Green count : {colors.count('green')}")

# Simple (with numbers)
nums = [1, 2, 2, 3, 4, 2, 5]
print("Count of 2 : ", nums.count(2))

# Simple (with mixed types)
mixed = [1, '1', 1.0, True]
print("Count of 1 : " ,mixed.count(1)) # Count of 1 :  3 # as 1==1, 1.0==1, True==1, but '1'!=1 (because str != int)
print("Count of '1' : " ,mixed.count('1')) # Count of '1' :  1
print("Count of True : " ,mixed.count(True)) # Count of True :  3
# Note : Remember -> '1' evalutes to True but is not equal to True in the first instnce. OR
# Note: Remember → '1' evaluates to True in a boolean context (like if '1':), but it is not equal to True when using == because they are different types.

# Working with sets = Best use of count()
# same concept implemented in list_13.py , do visit.
# POWERFUL Concept::::::
fruits = [
    'apple', 'banana', 'orange', 'apple', 'banana', 'apple',
    'kiwi', 'banana', 'grape', 'orange', 'banana', 'grape'
]

freq_of_all_unique_items = {unique_fruit: fruits.count(unique_fruit) for unique_fruit in set(fruits)}
print(freq_of_all_unique_items)
