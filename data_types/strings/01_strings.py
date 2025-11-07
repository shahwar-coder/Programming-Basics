'''
Q1. What is a Python string (str)?
Ans:
A string is an **immutable**, ordered sequence of Unicode characters.  
Used to store text like words, sentences, or any characters.
'''
# Example (tiny)
s = "Hello, 世界"
print(type(s), s)   # <class 'str'> Hello, 世界



'''
Q2. How can you create strings (different quote styles)?
Ans:
Use single `'...'`, double `"..."`, or triple quotes `'''...'''` / `"""..."""`.  
Triple quotes allow multi-line text. All produce str objects.
'''
# Example
a = 'single'
b = "double"
c = """line1
line2"""
print(a, b)
print(c)   # preserves newline



'''
Q3. What are raw strings and when to use them?
Ans:
Prefix with `r` (e.g. `r"\n"`) to treat backslashes literally.  
Good for regexes or Windows paths where you don't want escape processing.
'''
# Example
print("newline:\\n")   # shows escape
print(r"newline:\n")   # backslash + n, not a newline



'''
Q4. What are f-strings and how do they help?
Ans:
f-strings (`f"..."`) let you embed expressions inside `{}` directly.  
They are concise and evaluated at runtime (Python 3.6+).
'''
# Example
name = "Ava"
age = 14
print(f"{name} is {age} years old")  # interpolation
print(f"{2 + 3}")                    # expression inside braces



'''
Q5. What does "immutable" mean for strings and what follows?
Ans:
You cannot change a string in-place. Operations (replace, slice, concat) produce a **new** string.  
This makes strings safe to share but requires re-assignment for "changes".
'''
# Example
s = "cat"
s2 = s.replace("c", "b")  # new string created
print(s, s2)              # "cat" "bat"
# To 'change' s you must assign: s = s2
