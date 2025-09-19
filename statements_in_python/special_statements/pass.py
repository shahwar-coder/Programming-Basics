'''
Q1. What is the purpose of the `pass` statement in Python?
Ans: It acts as a placeholder. It does nothing when executed, 
but keeps the code syntactically valid.

Example:
'''

if True:
    pass   # valid but does nothing


'''
Q2. What are common use cases for `pass`?
Ans:
- Defining empty functions or classes.
- Keeping empty loops or conditionals.
- Writing stubs during development before real code is added.

Example:
'''

def todo_function():
    pass

class Empty:
    pass


'''
Q3. How does the `pass` statement behave at runtime?
Ans: It executes silently with no side effects, 
just like an empty block of code.

Example:
'''

for i in range(3):
    pass
print("Loop finished")  # runs normally


'''
Q4. Output ?
'''

def stub():
    pass

result = stub()
print("Result of calling stub():", result)

# ✅ Output: None
# Reason: The function executes pass (does nothing) 
# and since there is no return statement, 
# Python implicitly returns None.
