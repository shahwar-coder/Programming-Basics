'''
Q1. What does ord(char) return?
Ans:
It returns the **Unicode (ASCII) code point** for a single character.  
Useful for encoding, sorting, or character arithmetic.
'''
# Example
print(ord('A'))   # 65
print(ord('a'))   # 97
print(ord('€'))   # 8364



'''
Q2. What does chr(code) do?
Ans:
It performs the **inverse of ord()** —  
returns the **character** corresponding to a Unicode code point.
'''
# Example
print(chr(65))    # 'A'
print(chr(8364))  # '€'



'''
Q3. What happens if you use ord() with multi-character strings?
Ans:
It raises a **TypeError** — `ord()` only accepts **one character**.
'''
# Example
try:
    print(ord("AB"))
except TypeError as e:
    print("Error:", e)



'''
Q4. Can chr() and ord() handle Unicode beyond ASCII?
Ans:
Yes — they support **full Unicode range** (0–1,114,111).  
So you can convert emojis, foreign symbols, and more.
'''



'''
Q5. What happens if chr() receives an invalid code point?
Ans:
It raises a **ValueError** if the code is outside Unicode’s valid range.
'''
# Example
try:
    print(chr(999999999))
except ValueError as e:
    print("Error:", e)
