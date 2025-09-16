'''
Q. What is enclosing scope in Python? Show with an example.
Ans: Enclosing scope is the scope of an outer (non-global) function.  
A nested function can access variables from its enclosing function.

Example:
'''

def outer():
    msg = "enclosing variable"
    def inner():
        print("Inner sees:", msg)   # accesses outer's variable
    inner()

outer()
# Output: Inner sees: enclosing variable


'''
Q. How does the `nonlocal` keyword work in nested functions? Show with an example.
Ans: It lets a nested function modify a variable in its enclosing function (not global).
'''

Example:
def outer():
    x = 5
    def inner():
        nonlocal x
        x = 10   # modifies outer's x
    inner()
    print("Outer x:", x)  # 10

outer()

'''
✅ — let’s make it crystal clear.
Enclosing scope = variables defined in an outer (non-global) function.
nonlocal keyword = the tool you use inside a nested function to modify those enclosing variables.

So:
Enclosing = the place (outer function scope).
nonlocal = the keyword that lets you write to that place.
'''
