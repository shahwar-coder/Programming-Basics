'''
Q. What does replace() do?
Ans:
`replace(old, new[, count])` returns a new string where occurrences of `old`  
are replaced with `new`.  
You can limit replacements by specifying an optional `count`.
'''
# Example
text = "python is easy, python is powerful"
print(text.replace("python", "coding"))  # "coding is easy, coding is powerful"
print(text.replace("python", "AI", 1))   # "AI is easy, python is powerful"
