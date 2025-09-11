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

def greet():
    "This function prints a greeting"   # docstring
    print("Hello")

print(greet.__doc__)   # → This function prints a greeting (THIS IS THE OUTPT : PRINTING THE DOCSTRING)
