'''
Q. What does ord(char) return?
Ans:
It returns the **Unicode (ASCII) code point** for a single character.  
Useful for encoding, sorting, or character arithmetic.
'''
# Example
print(ord('A'))   # 65
print(ord('a'))   # 97
print(ord('€'))   # 8364



'''
Q. What does chr(code) do?
Ans:
It performs the **inverse of ord()** —  
returns the **character** corresponding to a Unicode code point.
'''
# Example
print(chr(65))    # 'A'
print(chr(8364))  # '€'
