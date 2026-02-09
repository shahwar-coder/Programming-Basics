'''
Q1. What is __next__ in Python?
A.
__next__ is a special method used by iterators to return the next item
in a sequence.
It is called automatically by Python during iteration.
'''
# Example:
# iterator.__next__() → returns next value
# If no value remains → raises StopIteration


'''
Q2. When does Python call __next__?
A.
Python calls __next__ automatically inside a for-loop
after obtaining an iterator using __iter__.
You rarely call __next__ directly.
'''
# Example:
# for x in obj:
#     print(x)
# Internally:
# it = obj.__iter__()
# it.__next__()


'''
Q3. What is the relationship between __iter__ and __next__?
A.
__iter__ returns an iterator.
__next__ is defined on that iterator and produces values one by one.
Both are required for a custom iterable.
'''
# Example:
# class MyIter:
#     def __iter__(self):
#         return self
#     def __next__(self):
#         ...


'''
Q4. What must __next__ do when no items are left?
A.
It MUST raise StopIteration.
This is how Python knows to stop the loop.
'''
# Example:
# if no_more_items:
#     raise StopIteration


'''
Q5. Why is StopIteration important?
A.
StopIteration is the signal that safely ends iteration.
Without it, loops would never terminate.
'''
# Example:
# for-loop catches StopIteration internally
# and exits cleanly


'''
Q6. How does __next__ enable lazy iteration?
A.
__next__ computes and returns values only when requested,
instead of producing everything upfront.
This enables memory-efficient iteration.
'''
# Example:
# Generator-like behavior:
# next(it) → compute one value
# next(it) → compute next value


'''
Q7. How is __next__ related to generators?
A.
Generators automatically implement __iter__ and __next__ for you.
yield handles value production and StopIteration internally.
'''
# Example:
# def gen():
#     yield 1
#     yield 2
# Generator already has __next__


'''
Q8. What is the simplest mental model for __next__?
A.
__next__ answers one question repeatedly:
“What is the NEXT value?”
'''
# Example:
# return next_value
# or
# raise StopIteration
