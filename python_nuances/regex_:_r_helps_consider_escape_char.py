'''
Q. What are raw strings and when to use them?
Ans:
Prefix with `r` (e.g. `r"\n"`) to treat backslashes literally.  
Good for regexes or Windows paths where you don't want escape processing.
'''
# Example
print("newline:\\n")   # shows escape
print(r"newline:\n")   # backslash + n, not a newline
