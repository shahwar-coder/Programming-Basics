'''
Q3. How does the `nonlocal` keyword work in nested functions? Show with an example.
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
