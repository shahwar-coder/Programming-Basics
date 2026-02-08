'''
__bool__ : a special method, that ansers the question "is this object true or false?"
Whenever Python needs to check something like:
if obj:
    ...
It internally calls:
obj.__bool__()
'''

# Class (check __bool__)
class Box:
    def __init__(self, items):
        self.items = items

    def __bool__(self):
        return len(self.items) > 0


# Objects
b1 = Box([1, 2, 3])
b2 = Box([])


# Conditions will check __bool__ internally
if b1:
    print("Box 1 is not empty")

if b2:
    print("Box 2 is not empty")
else:
    print("Box 2 is empty")


# Output
# Box 1 is not empty
# Box 2 is empty

