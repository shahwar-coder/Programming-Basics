'''
- assert
- if True : program continues
- if False : Python raises 'AssertionError' or you can print a message
- Syntax : assert condition
OR
- Syantax : assert condition, "Error message if assertion fails"
'''

# Simple Example:
x=5
assert x>0
assert x<0, "x must be less than 0" # AssertionError: x must be less than 0

# Why use assert?
'''
- input validation/ defensive programming
- early failure : Instead of letting buggy code run, assert halts immediately when the assumption is violated
- they act as inline assumptions/self documentation
- can be very helpful while development (Note: To be avoided in production)
'''

# Demirit of assert?
'''
- cannot be used in production code as error handlings
- as assertions can be globally disabled using 'python -0' (optimised mode)
'''
