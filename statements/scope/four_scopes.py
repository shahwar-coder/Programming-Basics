'''
Q1. What is the LEGB rule in Python? Write a snippet showing all four levels.
Ans: LEGB = Local → Enclosing → Global → Built-in.
'''

Example:
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Inside inner:", x)   # Local
    inner()
    print("Inside outer:", x)       # Enclosing

outer()
print("At module level:", x)        # Global
print("Built-in len:", len([1,2,3]))  # Built-in
