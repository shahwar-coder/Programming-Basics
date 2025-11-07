'''
Q. What does isalnum() verify?
Ans:
It returns **True** if all characters are **letters or digits** (alphanumeric).  
False if any character is a space or symbol.
'''
# Example
print("Python3".isalnum())   # True
print("Python 3".isalnum())  # False (space breaks it)
