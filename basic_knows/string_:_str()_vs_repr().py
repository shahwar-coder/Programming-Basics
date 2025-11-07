'''
Q. What does repr(x) do?
Ans:
It returns a **developer-friendly** string form of an object —  
includes quotes and escape characters for clarity.  
Often used for debugging or logging.
'''
# Example
text = "Hello\nWorld"
print(str(text))   # Prints on two lines
print(repr(text))  # 'Hello\nWorld'
