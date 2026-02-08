'''
Q1. What does __iter__ do in Python, and how does it enable looping over objects?
A.
__iter__ defines how an object can be iterated over using a for-loop.
When Python sees:
    for x in obj:
it internally calls:
    iterator = obj.__iter__()
The returned iterator is then asked for values one by one.
__iter__ must return an iterator, most commonly created using iter() on an internal collection.
'''

# Example:
class Bag:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return iter(self.items)   # convert internal list to iterator

b = Bag(["apple", "banana", "mango"])

for item in b:
    print(item)

# Output:
# apple
# banana
# mango
