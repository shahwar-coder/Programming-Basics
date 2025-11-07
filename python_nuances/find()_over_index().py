l'''
Q1. How is index() different from find()?
Ans:
`index(sub[, start[, end]])` works like `find()` but raises a **ValueError**  
if the substring is not found — useful when you *expect* the substring to exist.
'''
# Example
text = "hello world"
print(text.index("world"))   # 6
# print(text.index("java"))  # ValueError: substring not found



'''
2.
Better to use find()
'''
# Example
text = "learning python is fun"
print(text.find("python"))  # 9
print(text.find("java"))    # -1
