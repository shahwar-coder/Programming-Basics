'''
Creating Integers:
'''

# 1. int()->0
print(int())

# 2. Float Truncate
print(int(3.9))

# 3. Bool is subclass of int
print(int(True))
print(int(False))

#4. x=0000001230000 , as will be syntax error
# print(int(x))

# 5. Fix for 4. is str format having padding zeroes in start.
#4. x=0000001230000 , as will be syntax error
x="0000001230000"
print(int(x))

# 6. Can int take 2 arguments?
print(int('11', 2))
print(int('ff', 16))
# what's happening here is : `int(x, base=10)`
# base should be between 2 and 36
