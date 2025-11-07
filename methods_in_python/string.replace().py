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
