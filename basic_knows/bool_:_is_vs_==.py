'''
Q. What’s the difference between `is` and `==` with Booleans?
Ans:
- `is` → checks **identity** (same object in memory)  
- `==` → checks **value equality**  
Since True/False are singletons, both usually behave the same — but `is` is preferred.
'''
# Example
x = True
print(x is True)   # True
print(x == True)   # True
