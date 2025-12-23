'''
Q1. What is aliasing in Python lists?
Ans. Aliasing means two variables point to the SAME list in memory.
'''
# Example
a = [1, 2, 3]
b = a        # aliasing

b.append(4)
# a is now [1, 2, 3, 4] ❗
# b is also [1, 2, 3, 4]


'''
Q2. What is copying a list, and how is it different from aliasing?
Ans. Copying creates a NEW list in memory, so changes do not affect the original.
'''
# Example
a = [1, 2, 3]
b = a.copy()     # or list(a) or a[:]

b.append(4)
# a = [1, 2, 3]
# b = [1, 2, 3, 4]


'''
Q3. Why is aliasing dangerous in real programs?
Ans. Because changes through one variable silently affect another variable.
'''
# Example
def add_item(lst):
    lst.append(99)

nums = [1, 2]
add_item(nums)
# nums becomes [1, 2, 99]
# Side effect happened ❗
