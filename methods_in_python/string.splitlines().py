'''
Q. What does splitlines() do?
Ans:
It splits a string by **line breaks** (`\n`, `\r`, `\r\n`)  
and returns a list of lines.  
With `keepends=True`, newline characters are preserved.
'''
# Example 1: Basic usage
text = "Hello\nWelcome\nPython"
print(text.splitlines())        
# ['Hello', 'Welcome', 'Python']
print(text.splitlines(True))    
# ['Hello\n', 'Welcome\n', 'Python']


# Example 2: Handles different newline styles
mixed = "Line1\rLine2\r\nLine3\nLine4"
print(mixed.splitlines())
# ['Line1', 'Line2', 'Line3', 'Line4']


# Example 3: Works even without newline
s = "SingleLine"
print(s.splitlines())
# ['SingleLine']
