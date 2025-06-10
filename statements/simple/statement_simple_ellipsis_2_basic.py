'''
✅ Understanding Identity
What will be the output of the following code, and why?

print(Ellipsis is ...)
print(Ellipsis == ...)

'''

print(Ellipsis is ...) # True
print(Ellipsis == ...) # True

# `is` returns True because both point to the same object in memory.
# `==` returns True because their values are also the same.
