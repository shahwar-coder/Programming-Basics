'''
Q1. What is __len__ in Python?
A.
__len__ is a special method that tells Python
how many items an object contains.
It is called automatically when you use len(object).
'''
# Example:
# class Basket:
#     def __init__(self, apples):
#         self.apples = apples
#     def __len__(self):
#         return len(self.apples)
#
# b = Basket(["🍎", "🍎", "🍎"])
# len(b) → 3


'''
Q2. What happens if __len__ is not defined?
A.
Python raises a TypeError because it does not know
how to measure the size of the object.
'''
# Example:
# class Box:
#     pass
#
# box = Box()
# len(box)
# TypeError: object of type 'Box' has no len()


'''
Q3. What should __len__ always return?
A.
__len__ must return a non-negative integer.
Returning anything else breaks Python expectations.
'''
# Example:
# def __len__(self):
#     return 5        # ✅ valid
#     return 0        # ✅ valid
#     return -1       # ❌ invalid
#     return "five"  # ❌ invalid


'''
Q4. Why is __len__ important for Python objects?
A.
Because many Python features rely on it:
- len(obj)
- truthiness checks
- loops and collections
'''
# Example:
# if my_object:
#     ...
# Python internally checks:
# len(my_object) > 0


'''
Q5. How is __len__ related to truthiness?
A.
If __len__ is defined:
- len(obj) == 0 → object is False
- len(obj) > 0  → object is True
'''
# Example:
# class Cart:
#     def __init__(self, items):
#         self.items = items
#     def __len__(self):
#         return len(self.items)
#
# bool(Cart([]))        → False
# bool(Cart(["item"])) → True


'''
Q6. What is a real backend-style use of __len__?
A.
__len__ is used to represent size-like concepts:
- number of users
- number of records
- number of items in a queue
'''
# Example:
# class UserList:
#     def __init__(self, users):
#         self.users = users
#     def __len__(self):
#         return len(self.users)
#
# users = UserList(["A", "B", "C"])
# len(users) → 3
