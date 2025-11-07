'''
Q. How is lstrip() different from strip()?
Ans:
`lstrip([chars])` removes characters **only from the left side**  
(default: whitespace).
'''
# Example
text = "   spaced left"
print(text.lstrip())        # "spaced left"

txt = "***Code***"
print(txt.lstrip('*'))      # "Code***"
