'''
Q1. What is None in Python?
Ans:
None is a special constant that represents “no value”, “nothing”, or “empty”.
Its type is NoneType, and there is only one instance of it in Python.
'''
# Example
x = None
print(type(x))   # <class 'NoneType'>



'''
Q2. How does None behave in conditions?
Ans:
None behaves like False in Boolean contexts, but it is NOT the same as
False, 0, or an empty string. It simply means “absence of a value”.
'''
# Example
if not None:
    print("None behaves like False")



'''
Q3. What is the correct way to check for None?
Ans:
Always use “is” or “is not” because None is a singleton.
Never use == to check for None.
'''
# Example
x = None
if x is None:
    print("Correct check!")   # recommended
  
# Why not use == to check for None?

# • None is a singleton → only one instance exists.
#   → Use `is` / `is not` to compare identity.

# • `==` can be overridden by classes → may give wrong results.
#   Example:
#       class Weird:
#           def __eq__(self, other): return True
#       obj = Weird()
#       obj == None   # True (wrong)
#       obj is None   # False (correct)

# • `is` is faster and explicit → directly checks object identity.

# Recommended:
#     if x is None:
#         ...

# Not recommended:
#     if x == None:
#         ...



'''
Q4. When do functions return None automatically?
Ans:
If a function has no return statement, Python returns None by default.
'''
# Example
def hello():
    print("Hi!")

print(hello())   # prints "Hi!" then None



'''
Q5. When is None used in programs?
Ans:
Often used as a placeholder for “no value yet”, to mark missing data,
default parameters, or failed searches.
'''
# Example
result = None
if result is None:
    print("No result yet")



'''
Q6. Why use None instead of 0 or "" to represent “nothing”?
Ans:
0 and "" have meaning (zero, empty string). None clearly communicates:
“No value assigned” or “not applicable”, making code cleaner and safer.
'''
# Example
def find_user(id):
    return None   # means “user not found”



'''
Q7. Is None equal to False or zero?
Ans:
No. None is distinct from 0, False, "", [], and other falsy values.
It only evaluates to False in Boolean contexts.
'''
# Examples:
# Comparisons
print(None == 0)        # False
print(None == False)    # False
print(None == "")       # False
print(None == [])       # False
print(None is None)     # True (same object)
print(None is False)    # False



'''
Q8. Can you assign None to indicate optional function parameters?
Ans:
Yes. Using None as a default value is common for optional parameters,
especially when you need to detect “no value passed”.
'''
# Example
def load_data(path=None):
    if path is None:
        print("Using default path")



'''
Q9. Why is “is” used instead of “==” for checking None?
Ans:
Because None is a single unique object. “is” checks identity,
while “==” checks value — value comparison is unnecessary and unsafe.
'''
# Example
x = None
print(x is None)  # True  (correct)


