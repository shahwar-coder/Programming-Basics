'''
Q. What does capitalize() do?
Ans:
It capitalizes **only the first character** of the string  
and converts the rest to lowercase.
'''
# Example
print("hELLO wORLD".capitalize())   # "Hello world"



'''
Q. What’s the difference between title() and capitalize()?
Ans:
- `title()` → Capitalizes *every* word’s first letter.  
- `capitalize()` → Only the *first word*; rest lowercase.=
'''
# Example
s = "welcome to python"
print(s.title())      # "Welcome To Python"
print(s.capitalize()) # "Welcome to python"
