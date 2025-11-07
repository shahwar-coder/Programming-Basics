'''
Q. What are some advantages of format() over f-strings?
Ans:
It’s more **dynamic** — you can:
- Reorder or reuse placeholders  
- Pass variables dynamically  
- Use dictionary or object attributes for values
'''
# Example
data = {"lang": "Python", "ver": 3.12}
print("Using {lang} version {ver}".format(**data))  # Using Python version 3.12
