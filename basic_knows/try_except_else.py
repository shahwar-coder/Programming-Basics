'''
Q. `try` / `except` / `else` — how `else` helps
Ans:
- `else` after `try/except` runs only if the `try` block did NOT raise an exception.
- Use `else` to keep the `try` block minimal (only the code that may raise).
Example:
'''
s = "123"
try:
    value = int(s)       # only this in try
except ValueError:
    print("Bad number")
else:
    print("Parsed:", value)

# -> When exception is raised, the story ends then and there
# -> When no exception (everything alright), we go to else part (we can do something we wanna do, like printing some value etc.)
