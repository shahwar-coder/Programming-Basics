'''
Q1. What does + do with strings?
Ans:
The `+` operator **concatenates** (joins) two or more strings to make one new string.  
Because strings are immutable, this always creates a new object.
'''
# Example
a = "Hello"
b = "World"
print(a + " " + b)   # "Hello World"
print(a + b + "!")   # "HelloWorld!"



'''
Q2. What does * do with strings?
Ans:
The `*` operator repeats the string a given number of times.  
Useful for formatting, padding, or pattern generation.
'''
# Example
print("Hi" * 3)    # "HiHiHi"
print("-" * 10)    # "----------"



'''
Q3. How does indexing work with strings?
Ans:
Use `s[index]` to access a specific character.  
Indexes start at 0, and negative indexes count from the end.
'''
# Example
s = "Python"
print(s[0], s[-1])  # P n
print(s[2])         # t



'''
Q4. What is slicing in strings and how does it work?
Ans:
Slicing extracts substrings using `[start:stop:step]`.  
It creates a new string, never changes the original.
'''
# Example
text = "Python"
print(text[1:4])   # "yth"
print(text[:4])    # "Pyth"
print(text[::2])   # "Pto"
print(text[::-1])  # "nohtyP" (reversed)



'''
Q5. What does the `in` operator check in strings?
Ans:
It tests **membership**, i.e., if a substring exists within another string.  
Returns True or False.
'''
# Example
msg = "learning Python"
print("Python" in msg)    # True
print("java" in msg)      # False



'''
Q6. How can you iterate over a string?
Ans:
Strings are iterable — you can loop through characters using a `for` loop.  
Each iteration gives one character in order.
'''
# Example
for ch in "abc":
    print(ch)
# Output:
# a
# b
# c



'''
Q7. Are + and * efficient for large strings?
Ans:
Not always — since strings are immutable, each operation makes a new copy.  
For performance, use `"".join(iterable)` when joining many strings.
'''
# Example
parts = ["Py", "thon", "3"]
print("".join(parts))  # "Python3"



'''
Q8. What’s the difference between slicing and indexing safety-wise?
Ans:
- **Indexing**: error if out of range  
- **Slicing**: safely returns empty string if range is invalid
'''
# Example
s = "abc"
print(s[1:10])  # "bc" (safe)
# print(s[10])  # IndexError

