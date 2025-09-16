'''
Q2. How does the `global` keyword affect scope? Show with an example.
Ans: It lets a function modify a variable at module (global) scope.
Example:
'''

x = 10

def update():
    global x
    x = 20   # modifies global x

update()
print("Global x:", x)   # 20
