'''
Q7. Are integers mutable or immutable?
Ans:
Integers are *immutable*.  
Any operation that changes their value creates a new object in memory.
'''
# Example
x = 10
print(id(x))
x += 1
print(id(x))   # different id → new object created
