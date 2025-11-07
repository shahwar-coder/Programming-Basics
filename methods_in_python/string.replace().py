'''
Q1. What does replace() do?
Ans:
`replace(old, new[, count])` returns a new string where occurrences of `old`  
are replaced with `new`.  
You can limit replacements by specifying an optional `count`.
'''
# Example
text = "python is easy, python is powerful"
print(text.replace("python", "coding"))  # "coding is easy, coding is powerful"
print(text.replace("python", "AI", 1))   # "AI is easy, python is powerful"



'''
Q2. Do find(), index(), and replace() modify the original string?
Ans:
No — all these methods return **new strings**.  
Strings are immutable; originals remain unchanged.
'''
# Example
s = "hello"
s2 = s.replace("h", "H")
print(s, s2)  # "hello" "Hello"



'''
Q3. How does replace() behave with count argument = 0?
Ans:
If `count = 0`, no replacements are made; the original string is returned unchanged.
'''
# Example
text = "spam spam spam"
print(text.replace("spam", "eggs", 0))  # "spam spam spam"



'''
Q4. What happens if the substring is not found in replace()?
Ans:
No error is raised — if `old` isn’t found, the original string is returned as-is.
'''
# Example
text = "hello world"
print(text.replace("java", "python"))  # "hello world"
