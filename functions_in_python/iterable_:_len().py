'''
Q. What does len() do for strings?
Ans:
`len(x)` returns the **number of characters** in a string  
(or more generally, the length of any iterable).
'''
# Example 1: Normal text
text = "Hello World"
print(len(text))       # 11

# Example 2: Including spaces
msg = "Python is fun"
print(len(msg))        # 13 (spaces are counted)

# Example 3: Empty string
empty = ""
print(len(empty))      # 0

# Example 4: Special characters
special = "Hi!\nBye!"
print(len(special))    # 8  (newline \n counts as one char)

# Example 5: Unicode / Emoji
emoji_text = "😀Hi😊"
print(len(emoji_text)) # 4 (each emoji counts as one character)

# Example 6: Multiline string
multiline = """Line1
Line2
Line3"""
print(len(multiline))  # 17 (includes \n characters)

# Example 7: String with tabs and spaces
tabbed = "A\tB\tC"
print(len(tabbed))     # 5 (\t counts as one character)




'''
Q. What does len() do for lists?
Ans:
`len(x)` returns the **number of elements** present in the list.
'''
# Example
nums = [10, 20, 30, 40]
print(len(nums))       # 4
print(len([]))         # 0



'''
Q. What does len() do for tuples?
Ans:
`len(x)` returns the **number of items** in a tuple.
'''
# Example
t = (1, 2, 3, 4, 5)
print(len(t))          # 5
print(len(()))         # 0



'''
Q. What does len() do for sets?
Ans:
`len(x)` returns the **number of unique elements** in a set.
'''
# Example
s = {1, 2, 3, 3, 4}
print(len(s))          # 4  (duplicates ignored)
print(len(set()))      # 0



'''
Q. What does len() do for dictionaries?
Ans:
`len(x)` returns the **number of key-value pairs** in a dictionary.
'''
# Example
d = {'a': 1, 'b': 2, 'c': 3}
print(len(d))          # 3
print(len({}))         # 0
