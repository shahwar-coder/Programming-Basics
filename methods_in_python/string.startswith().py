'''
Q1. What does startswith() do?
Ans:
Checks whether the string starts with a given prefix.  
Case-sensitive, but supports optional `start` and `end` slice arguments.
'''
# Example
text = "learning python"
print(text.startswith("learn"))   # True
print(text.startswith("Learn"))   # False
print(text.startswith("python", 9))  # True (checks slice)



'''
Q2. What’s the difference between these and regex checks?
Ans:
These methods are **faster and simpler** for direct checks,  
while regular expressions are more flexible for complex patterns.
'''
# Example
import re
print("abc123".isalnum())            # True
print(bool(re.match(r"^[a-z0-9]+$", "abc123")))  # Same result, slower
