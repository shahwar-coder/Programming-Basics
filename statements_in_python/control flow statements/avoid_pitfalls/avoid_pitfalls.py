'''
Q1. What does “wrong order of conditions” mean in control flow?
Ans:
Python checks conditions left to right.  
If we write them in the wrong order, logic can break.  
Use natural chaining like `if 0 < x < 10:` instead of nested or reversed checks.
'''
# Example
x = 5
if 0 < x < 10:
    print("In range!")   # clean and clear



'''
Q2. Why should we avoid mixing data types in conditions?
Ans:
Because Python doesn’t auto-convert between types in comparisons.  
For example, `"5" == 5` gives False, and `"5" > 4` gives a TypeError.
Always compare values of the same type.
'''
# Example
print("5" == 5)    # False
# print("5" > 4)   # ❌ TypeError
print(int("5") > 4) # ✅ True after conversion



'''
Q3. Why is deep nesting a bad practice?
Ans:
Too many if-inside-if layers make code hard to read and debug.  
Instead, use logical operators (`and`, `or`) or return early in functions.
'''
# Example
# Bad:
# if a:
#     if b:
#         if c:
#             print("Go")

# Better:
if a and b and c:
    print("Go")



'''
Q4. What’s the difference between equality (==) and identity (is)?
Ans:
`==` checks if values are equal.  
`is` checks if two names point to the same object in memory.
'''
# Example
a = [1, 2]; b = [1, 2]
print(a == b)   # True → values same
print(a is b)   # False → different objects



'''
Q5. When should we use ‘is’ instead of ‘==’?
Ans:
Use ‘is’ for identity checks — especially for special objects like `None`.  
For normal value comparison, use `==`.
'''
# Example
x = None
if x is None:
    print("Empty")   # correct way



'''
Q6. How can we make control flow more readable and error-free?
Ans:
- Write clear, ordered conditions.  
- Avoid mixing data types.  
- Use early returns to reduce nesting.  
- Remember: `==` for values, `is` for identity.
Clean logic → fewer bugs.
'''
# Example
def safe_check(x):
    if x is None:
        return "Missing"
    if 0 < x < 10:
        return "Valid"
    return "Out of range"
