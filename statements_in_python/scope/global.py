'''
Q. How does the `global` keyword affect scope? Show with an example.
Ans: It lets a function modify a variable at module (global) scope.
Example:
'''

x = 10

def update():
    global x
    x = 20   # modifies global x

update()
print("Global x:", x)   # 20

'''
Q. Why does assigning inside a function sometimes cause UnboundLocalError? Show with an example.
Ans: Python treats a name as local if assigned inside the function, unless declared global/nonlocal.
'''

Example:
x = 100

def f():
    print(x)   # ❌ Error → UnboundLocalError
    x = 200    # Python thinks x is local, but it’s used before assignment

# f()  # uncomment to see error

