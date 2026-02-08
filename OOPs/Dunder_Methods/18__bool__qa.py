'''
Q1. What is __bool__ in Python?
A.
__bool__ is a special method that tells Python
whether an object should be treated as True or False.

Whenever Python sees:
if obj:

It internally calls:
obj.__bool__()
'''
# Example:
# class Box:
#     def __init__(self, items):
#         self.items = items
#     def __bool__(self):
#         return len(self.items) > 0
#
# b1 = Box([1, 2])
# b2 = Box([])
#
# bool(b1) → True
# bool(b2) → False


'''
Q2. When does Python automatically call __bool__?
A.
Python calls __bool__ in all truth-value checks:
- if obj:
- while obj:
- not obj
- bool(obj)
'''
# Example:
# if b1:          # calls b1.__bool__()
#     print("True")
#
# print(bool(b2)) # calls b2.__bool__()


'''
Q3. What happens if __bool__ is NOT defined?
A.
Python falls back to __len__.
If __len__ returns 0 → False
If __len__ > 0 → True
'''
# Example:
# class Cart:
#     def __init__(self, items):
#         self.items = items
#     def __len__(self):
#         return len(self.items)
#
# cart = Cart([])
# if cart:        # False because len(cart) == 0
#     print("Has items")


'''
Q4. What if neither __bool__ nor __len__ is defined?
A.
Python treats the object as True by default.
'''
# Example:
# class AlwaysTrue:
#     pass
#
# obj = AlwaysTrue()
# if obj:
#     print("Always true")


'''
Q5. Why is __bool__ useful in real backend code?
A.
It allows objects to express business meaning naturally.
Instead of writing explicit checks everywhere,
logic becomes readable and expressive.
'''
# Example:
# if user:              # instead of if user.is_active
# if cart:              # instead of if len(cart.items) > 0
# if token:             # instead of if token.is_valid()


'''
Q6. What are common backend patterns using __bool__?
A.
- Empty vs non-empty containers
- Valid vs invalid tokens
- Loaded vs unloaded resources
- Active vs inactive objects
'''
# Example:
# class Token:
#     def __init__(self, expired):
#         self.expired = expired
#     def __bool__(self):
#         return not self.expired
#
# token = Token(expired=False)
# if token:
#     print("Token is valid")


'''
Q7. What should __bool__ ALWAYS return?
A.
A boolean value: True or False.
Anything else is a bug.
'''
# Example:
# ❌ BAD
# def __bool__(self):
#     return 1
#
# ✅ GOOD
# def __bool__(self):
#     return True


'''
Q8. Golden rule to remember
A.
- __bool__ answers: "Does this object logically exist?"
- __len__ answers: "How many things are inside?"
- if obj: should read like English
'''
# Example:
# if cart:
# if user:
# if response:
# Clean, expressive, Pythonic
