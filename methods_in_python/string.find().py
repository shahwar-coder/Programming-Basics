'''
Q1. What does find() do in Python strings?
Ans:
`find(sub[, start[, end]])` searches for a substring and returns its **lowest index**.  
If not found, it returns **-1** instead of raising an error — safe for use in conditionals.
'''
# Example
text = "learning python is fun"
print(text.find("python"))  # 9
print(text.find("java"))    # -1



'''
Q2. How is index() different from find()?
Ans:
`index(sub[, start[, end]])` works like `find()` but raises a **ValueError**  
if the substring is not found — useful when you *expect* the substring to exist.
'''
# Example
text = "hello world"
print(text.index("world"))   # 6
# print(text.index("java"))  # ValueError: substring not found

