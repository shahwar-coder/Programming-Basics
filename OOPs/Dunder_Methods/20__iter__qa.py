'''
Q1. What is __iter__ in Python?
A.
__iter__ is a special method that tells Python
how an object should be LOOPED over.

Whenever you write:
for x in obj:

Python automatically calls:
obj.__iter__()
'''
# Example:
# class Bag:
#     def __init__(self, items):
#         self.items = items
#     def __iter__(self):
#         return iter(self.items)
#
# b = Bag(["apple", "banana"])
# for item in b:
#     print(item)


'''
Q2. What exactly happens internally during a for-loop?
A.
A for-loop works in two steps:
1️⃣ Call __iter__() to get an iterator
2️⃣ Repeatedly ask that iterator for next values
'''
# Example:
# iterator = b.__iter__()
# next(iterator) → "apple"
# next(iterator) → "banana"
# next(iterator) → StopIteration


'''
Q3. What must __iter__ return?
A.
__iter__ MUST return an iterator object.
Returning a list or value directly is WRONG.
'''
# Example:
# ✅ Correct
# def __iter__(self):
#     return iter(self.items)
#
# ❌ Wrong
# def __iter__(self):
#     return self.items


'''
Q4. Why do we usually write return iter(self.items)?
A.
Because iter():
- Converts a collection into an iterator
- Handles traversal logic safely
- Avoids reinventing iteration logic
'''
# Example:
# self.items = ["a", "b", "c"]
# iter(self.items) → <list_iterator>


'''
Q5. What is the difference between iterable and iterator?
A.
- Iterable → something you CAN loop over
- Iterator → something that PRODUCES values one-by-one
'''
# Example:
# list → iterable
# iter(list) → iterator
#
# __iter__ turns your object into an iterable


'''
Q6. Why is __iter__ important in backend / real code?
A.
It allows custom objects to behave like collections,
making code cleaner and more Pythonic.
'''
# Example:
# if cart:
#     for item in cart:
#         process(item)
#
# cart behaves like a list without exposing internals


'''
Q7. What is the core mental model?
A.
- __iter__ defines HOW traversal starts
- iter() creates the engine that moves step-by-step
- for-loop just drives the engine
'''
# Example:
# __iter__ → "Here is how to iterate me"
# iter()   → "Here is the iterator"
# for-loop → "Give me next, next, next..."
