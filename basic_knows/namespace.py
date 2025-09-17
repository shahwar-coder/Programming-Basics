'''
Q: What is a namespace in Python?
A: A namespace is a mapping between names (identifiers) and objects (values/functions).
   It works like a dictionary: {"name": object}. 
   Python uses namespaces to keep track of all variables, functions, classes, etc.

Example:
    x = 10
    y = "hello"
Namespace looks like: {"x": 10, "y": "hello"}

Q: Types of namespaces?
1. Built-in namespace → provided by Python (e.g., print, len, sum)
2. Global namespace → names defined at the top level of a module/script
3. Local namespace → names inside a function

Example:
    def func():
        a = 5   # local
    b = 10      # global
    print(len([1,2,3]))  # built-in

Q: How do namespaces relate to modules?
- When you `import math`, Python creates a 'math' module object in the current namespace.
- Its attributes must be accessed with dot notation.

Example:
    import math
    print(math.sqrt(16))   # accessing sqrt from math namespace
'''
