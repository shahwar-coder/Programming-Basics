'''
- pass
- pass is a null operation
- what does it do? - "nothing"
- used when ? - when you do not want ot write the code on that line yet but also do not want it to through any syntac error.
- python will not allow you to have empty blocks
'''

# Basic use 1 (Function and Class):
def future_function():
    pass

class ShahwarClass:
    pass

# Basic use 2 (if, else, loop):
for i in range(5):
    pass

x=6
if x>0:
    pass # acts as a placeholder, to place the logic later here, I have not decoded the logic here, so we can put pass here
else:
    print("x is not positive!")


# Basic use 3 (to handle exceptions):
try:
    pass
except ValueError:
    pass # ignore the error for now

# Real logic will be written later, that's the main use case of pass.
