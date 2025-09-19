'''
Q. How does local scope work in Python? Show with an example.
Ans: A variable created inside a function is local to that function by default.  
It cannot be accessed outside the function.

Example:
'''

def f():
    x = 42   # local to f
    print("Inside f:", x)

f()
# print(x)  # ❌ Error → NameError: x is not defined (outside local scope)
