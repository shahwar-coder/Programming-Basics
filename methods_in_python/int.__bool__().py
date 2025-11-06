'''
Q. How do bool() and x.__bool__() behave for integers?
Ans:
Integers are **truthy** if nonzero, and **falsy** if zero.
'''
# Example
print(bool(0))    # False
print(bool(7))    # True
print((0).__bool__())  # False
