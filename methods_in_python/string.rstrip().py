'''
Q1. How is rstrip() different from lstrip()?
Ans:
`rstrip([chars])` removes characters **only from the right side**  
(default: whitespace).
'''
# Example
text = "right side   "
print(text.rstrip())        # "right side"

txt = "###Python###"
print(txt.rstrip('#'))      # "###Python"



'''
Q2. Do these methods change the original string?
Ans:
No — all return **new strings**.  
Strings are immutable; the original remains unchanged.
'''
# Example
text = "  data  "
trimmed = text.strip()
print(text, trimmed)  # "  data  " "data"



'''
Q3. What happens if the string has internal spaces or symbols?
Ans:
`strip()`, `lstrip()`, and `rstrip()` only affect the **edges** of the string,  
not characters in the middle.
'''
# Example
text = "  clean  me  "
print(text.strip())  # "clean  me"
