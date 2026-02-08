'''
Q1. What does __bool__ do in Python, and when is it called?
A.
__bool__ defines how an object behaves in a true/false context.
Whenever Python evaluates an object in a condition like:
    if obj:
Python internally calls:
    obj.__bool__()
The method must return True or False, telling Python whether the object should be treated as truthy or falsy.
'''

# Example:
class Box:
    def __init__(self, items):
        self.items = items

    def __bool__(self):
        return len(self.items) > 0   # True if box has items

b1 = Box([1, 2, 3])
b2 = Box([])

if b1:
    print("Box 1 is not empty")

if b2:
    print("Box 2 is not empty")
else:
    print("Box 2 is empty")

# Output:
# Box 1 is not empty
# Box 2 is empty
