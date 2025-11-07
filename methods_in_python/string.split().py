'''
Q. What does split() do in Python strings?
Ans:
It splits a string into a **list of substrings**, using a separator (`sep`).  
If no separator is given, it splits on **whitespace** by default.
'''
# Example 1: Default split (on whitespace)
text = "Python is fun to learn"
print(text.split())        
# ['Python', 'is', 'fun', 'to', 'learn']

# Example 2: Split with a custom separator
data = "apple,banana,mango,grapes"
print(data.split(','))     
# ['apple', 'banana', 'mango', 'grapes']

# Example 3: Using maxsplit
text = "Python is fun to learn"
print(text.split(' ', 2))  
# ['Python', 'is', 'fun to learn']

# Example 4: Splitting on newline characters
para = "line1\nline2\nline3"
print(para.split('\n'))    
# ['line1', 'line2', 'line3']

# Example 5: Handling multiple spaces (default behavior)
msg = "Hello     world   Python"
print(msg.split())         
# ['Hello', 'world', 'Python']   ← ignores extra spaces

# Example 6: When separator not found
s = "hello world"
print(s.split(','))        
# ['hello world']   ← no split happens

# Example 7: Splitting file paths or URLs
path = "home/user/documents/report.txt"
print(path.split('/'))     
# ['home', 'user', 'documents', 'report.txt']

