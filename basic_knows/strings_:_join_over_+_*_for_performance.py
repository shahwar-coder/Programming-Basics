'''
Q. Are + and * efficient for large strings?
Ans:
Not always — since strings are immutable, each operation makes a new copy.  
For performance, use `"".join(iterable)` when joining many strings.
'''
# Example
parts = ["Py", "thon", "3"]
print("".join(parts))  # "Python3"
