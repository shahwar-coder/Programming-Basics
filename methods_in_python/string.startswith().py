'''
Q. What does startswith() do?
Ans:
Checks whether the string starts with a given prefix.  
Case-sensitive, but supports optional `start` and `end` slice arguments.
'''
# Example
text = "learning python"
print(text.startswith("learn"))   # True
print(text.startswith("Learn"))   # False
print(text.startswith("python", 9))  # True (checks slice)
