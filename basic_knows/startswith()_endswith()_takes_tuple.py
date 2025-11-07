'''
Q. Can startswith() and endswith() take tuples?
Ans:
Yes — you can pass a tuple of prefixes/suffixes,  
and it returns True if the string starts/ends with *any* of them.
'''
# Example
filename = "data.csv"
print(filename.endswith((".csv", ".txt")))  # True
print(filename.startswith(("log", "data"))) # True
