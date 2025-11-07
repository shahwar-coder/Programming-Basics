'''
Aim here : To empty the list.
TC : O(n), both, same performance
'''
# Example 5: clear() vs del lst[:]
values = [1, 2, 3]
values.clear()
print(values)         # []
values = [4, 5, 6]
del values[:]
print(values)         # []
