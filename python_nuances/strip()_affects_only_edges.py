'''
Q. What happens if the string has internal spaces or symbols?
Ans:
`strip()`, `lstrip()`, and `rstrip()` only affect the **edges** of the string,  
not characters in the middle.
'''
# Example
text = "  clean  me  "
print(text.strip())  # "clean  me"
