'''
Q1. What does “truth value testing” mean in Python?
Ans:
It means checking if an object should be treated as True or False 
in conditions like if, while, etc.
Every object in Python has a truth value.
'''
# Example
if "Hello":
    print("Truthy")   # runs because non-empty string → True
if []:
    print("Falsy")    # won’t run → empty list → False



'''
Q2. What are the common falsy values in Python?
Ans:
Falsy values include:
False, None, 0, 0.0, 0j, "", [], {}, set(), range(0).
Also, any object whose `__bool__()` or `__len__()` returns False or 0.
'''
# Example
for val in [False, None, 0, "", [], {}]:
    if val:
        print("Truthy:", val)
    else:
        print("Falsy:", type(val))
# Falsy: <class 'bool'>
# Falsy: <class 'NoneType'>
# Falsy: <class 'int'>
# Falsy: <class 'str'>
# Falsy: <class 'list'>
# Falsy: <class 'dict'>



'''
Q3. What counts as truthy values?
Ans:
Anything that is not falsy — 
for example, non-empty strings, non-zero numbers, and most objects.
'''
# Example
if [1, 2, 3]:
    print("Truthy list!")   # Runs → list not empty



'''
Q4. How does Python decide whether something is truthy or falsy?
Ans:
1. Tries calling `obj.__bool__()`.  
2. If not defined, tries `obj.__len__()`.  
3. If neither exists, it defaults to True.
'''
# Example
class Box:
    def __len__(self): return 0
print(bool(Box()))   # False → because __len__ returns 0



'''
Q5. Can we make custom objects behave as falsy?
Ans:
Yes! Define the `__bool__()` method to return False.
That makes instances of your class evaluate as False in conditions.
'''
# Example
class MyBox:
    def __bool__(self):
        return False

if MyBox():
    print("Truthy")
else:
    print("Falsy")    # prints Falsy



'''
Q6. Why is truth value testing useful?
Ans:
It makes conditions simple and natural — 
you can just write `if items:` instead of `if len(items) > 0:`.
It keeps code clean and “Pythonic”.
'''
# Example
items = [1, 2, 3]
if items:
    print("List has items!")   # Clear and Pythonic
