'''
====    __iter__   ====:

What is __iter__?
- __iter__ is a special method that tells Python how to loop over an object.
- It is automatically used when you write: for x in obj:

What happens internally?
- Python calls: iterator = obj.__iter__()
- Then it repeatedly asks the iterator for the next value.

Important rule:
- __iter__ must return an iterator.
- Most common pattern: return iter(self.some_collection)

How iter() is involved:
- iter() converts a collection (like list, tuple, string) into an iterator.
- Inside __iter__, we usually call: iter(self.items)
- That iterator then gives elements one by one during the loop.

One simple example:

class Bag:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return iter(self.items)   # iter() creates the iterator

b = Bag(["apple", "banana", "mango"])

for item in b:
    print(item)

Internal flow:
1. Python calls: b.__iter__()
2. __iter__ returns: iter(self.items)
3. Python keeps asking the iterator for the next item
4. Items are printed one by one

Core idea:
- __iter__ = defines how an object is traversed
- iter() = creates the actual iterator used in the loop
'''
