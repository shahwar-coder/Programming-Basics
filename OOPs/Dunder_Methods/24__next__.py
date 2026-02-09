'''
__next__ — short, effective summary

What is __next__?
- A special method used by iterators.
- It returns the next item in a sequence.

Where it is used:
- Automatically called during a `for` loop.

Internal flow:
iterator = obj.__iter__()
item = iterator.__next__()

Key rule:
- Each call to __next__ returns the next value.
- When no items remain, it must raise StopIteration.

Simple example:

class Counter:
    def __init__(self, max):
        self.current = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

for x in Counter(3):
    print(x)

Output:
1
2
3

One-line idea:
__next__ = method that gives the next item, or stops the loop.
'''
