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



'''
Q2. How is the return statement different in normal functions vs generator functions?
Ans:
- Normal function: return gives a value back directly.  
- Generator (with yield): return ends the generator.  
  If it has a value, it raises StopIteration(value).  
This value is only visible if caught or via 'yield from'.
'''
