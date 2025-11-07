'''
Q. What does strip() do in Python strings?
Ans:
`strip([chars])` removes **leading and trailing whitespace** by default.  
If `chars` is given, it removes all specified characters from both ends.
'''
# Example 1: Basic usage (default whitespace removal)
text = "   hello world   "
print(text.strip())         
# "hello world"

# Example 2: Removes tabs and newlines too
s = "\n\t  Python\n"
print(s.strip())            
# "Python"

# Example 3: Removing specific characters
txt = "---Python---"
print(txt.strip('-'))       
# "Python"

# Example 4: Removing multiple different characters
data = "...,,,Python!!!..."
print(data.strip(".,!"))    
# "Python"

# Example 5: Only characters at the **ends** are removed
t = "xyxPythonxy"
print(t.strip("xy"))        
# "Python"   ← middle 'xy' not removed

# Example 6: When string contains only removable chars
s = "####"
print(s.strip('#'))         
# ""  ← completely removed

