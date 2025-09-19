'''
📌 Expression Statement
• Any expression used as a statement
• Evaluated → result ignored unless side effect
• Common use: function calls (print, update, etc.)
• In REPL → value is echoed; in scripts → ignored

📌 Docstrings
• A string literal as the first statement in a module, class, or function
• Stored in the __doc__ attribute
• Used for documentation; other string literals are just ignored expressions
'''

```Q1. Show how to print the docstring```
def greet():
    "This function prints a greeting"   # docstring
    print("Hello")

print(greet.__doc__)   # → This function prints a greeting (THIS IS THE OUTPT : PRINTING THE DOCSTRING)

```Q2. Which one will be the docstring and get printed?```
def f():
    "hello"
    "world"
    return 1

print(f.__doc__) # output : "hello" (1st one)

```Q3. When no doctring what will it print?```
def f():
    pass

print(f.__doc__)   # None
# None will be printed
