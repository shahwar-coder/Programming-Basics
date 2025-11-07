'''
Q1. What does repr(x) do?
Ans:
It returns a **developer-friendly** string form of an object —  
includes quotes and escape characters for clarity.  
Often used for debugging or logging.
'''
# Example
text = "Hello\nWorld"
print(str(text))   # Prints on two lines
print(repr(text))  # 'Hello\nWorld'



'''
Q2. How are str() and repr() different in intent?
Ans:
- `str()` → human-readable (user-friendly)  
- `repr()` → machine-readable (for developers, debugging)
'''
# Example
import datetime
d = datetime.date(2025, 11, 7)
print(str(d))   # '2025-11-07' (friendly)
print(repr(d))  # 'datetime.date(2025, 11, 7)' (precise)
