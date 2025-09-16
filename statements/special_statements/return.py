'''
Q1. What happens when a function executes a return statement?
Ans: It ends the function immediately.  
- With a value → returns that value.  
- With no value → returns None.  

Example:
'''

def f():
    return 42
print(f())   # 42

def g():
    return
print(g())   # None
