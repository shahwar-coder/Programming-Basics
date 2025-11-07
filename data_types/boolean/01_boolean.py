'''
Q1. What is the Boolean type in Python?
Ans:
It’s a data type with only **two values** — `True` and `False`.  
`bool` is actually a **subclass of int**, where `True == 1` and `False == 0`.
'''
# Example
print(True, False)
print(True == 1, False == 0)  # True True
print(isinstance(True, int))  # True



'''
Q2. How can you create Boolean values?
Ans:
You can directly assign `True` or `False`,  
or use the `bool()` function to convert other types.
'''
# Example
print(bool(1))       # True
print(bool(0))       # False
print(bool([]))      # False
print(bool("Hi"))    # True



'''
Q3. What values are considered falsy in Python?
Ans:
Falsy values evaluate to `False` in Boolean contexts:
`0, 0.0, 0j, None, '', [], {}, set(), range(0)`
Everything else is truthy.
'''
# Example
falsy = [0, 0.0, 0j, None, '', [], {}, set()]
print([bool(x) for x in falsy])  # [False, False, False, False, False, False, False, False]



'''
Q4. What are the main Boolean operators?
Ans:
- `and` → True if **both** values are True  
- `or` → True if **at least one** is True  
- `not` → negates a Boolean value  
They also support **short-circuit evaluation**.
'''
# Example
print(True and False)   # False
print(True or False)    # True
print(not True)         # False
print(0 and 5)          # 0 (short-circuited)



'''
Q5. What built-in functions work with Booleans?
Ans:
- `bool(x)` → convert to Boolean  
- `all(iterable)` → True if all items truthy  
- `any(iterable)` → True if any item truthy
'''
# Example
print(all([True, 1, "ok"]))     # True
print(any([0, "", 5]))          # True
print(any([0, "", []]))         # False



'''
Q6. What does “short-circuit evaluation” mean?
Ans:
Python stops evaluating as soon as the result is known.  
E.g., in `a and b`, if `a` is False, `b` is never checked.
'''
# Example
def demo():
    print("Checked!")
    return True

print(False and demo())  # Short-circuits, no print
print(True or demo())    # Short-circuits, no print



'''
Q7. Why should you avoid using Booleans in arithmetic?
Ans:
Since `bool` is a subclass of `int`,  
you can add them — but it’s poor style and confusing.
'''
# Example
print(True + True)    # 2
print(False + 5)      # 5
# Avoid doing this in real code



'''
Q8. What’s the recommended way to test truth in conditions?
Ans:
Use **direct truth checks**, not `== True` or `is True`.
'''
# Example
items = [1, 2, 3]
if items:          # ✅ Preferred
    print("List not empty")
if len(items) > 0: # 👎 Verbose
    print("Still works")



'''
Q9. Can you override Boolean behavior in custom classes?
Ans:
Yes — by defining the special method `__bool__()` or `__len__()`  
to control how objects evaluate in Boolean contexts.
'''
# Example
class MyBox:
    def __bool__(self):
        return False

box = MyBox()
print(bool(box))   # False



'''
Q10. What’s the difference between `is` and `==` with Booleans?
Ans:
- `is` → checks **identity** (same object in memory)  
- `==` → checks **value equality**  
Since True/False are singletons, both usually behave the same — but `is` is preferred.
'''
# Example
x = True
print(x is True)   # True
print(x == True)   # True
