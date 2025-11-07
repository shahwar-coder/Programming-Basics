'''
Q1. What does endswith() do?
Ans:
Checks whether the string ends with a specific suffix.  
Also supports optional `start` and `end` parameters for substring checks.
'''
# Example 1: straight forward
print(text.endswith("python"))   # True
print(text.endswith("Java"))     # False

# Example 2: Using a tuple of suffixes
filename = "report.pdf"
print(filename.endswith((".pdf", ".docx", ".txt")))   # True

# Example 3: Using start and end parameters
msg = "Welcome to Python programming"
print(msg.endswith("Python", 0, 18))   # True   (checks within substring)
print(msg.endswith("programming", 0, 25))  # False  (range ends before match)

# Example 4: On empty string
print("".endswith(""))   # True — every string (even empty) ends with ""




'''
Q2. Can startswith() and endswith() take tuples?
Ans:
Yes — you can pass a tuple of prefixes/suffixes,  
and it returns True if the string starts/ends with *any* of them.
'''
# Example
filename = "data.csv"
print(filename.endswith((".csv", ".txt")))  # True
print(filename.startswith(("log", "data"))) # True

