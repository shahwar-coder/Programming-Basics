'''
- reverses the elements of a list, in-place
- takes no argument
- to get a reverse copy, use slicing "[::-1]"
'''

# Simple (original list is modified)
numbers=[1,2,3,9,7,5]
numbers.reverse()
print(numbers)

# Reverse by Slicing (a copy is made)
nums=[1,2,3,4,5,6,7,8,9]
rev_copy = nums[::-1]
print(f"Reversed by Slicing : {rev_copy}")
