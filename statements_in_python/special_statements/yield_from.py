'''
Q1. What does `yield from` do in Python?
Ans: It delegates iteration to another generator or iterable.
- It automatically yields all values from the sub-generator.
- When the sub-generator finishes, its return value is passed back.

Example:
'''

def child():
    yield 1; yield 2

def parent():
    yield from child()

print(list(parent()))  # [1, 2]



'''
Q2. How is `yield from` different from writing a manual for-loop?
Ans:
- Manual loop: for val in gen: yield val
- yield from: shorter, and it also captures the sub-generator’s return value.

Example:
'''

def child(): 
    yield 1; return 42

def parent_manual():
    for v in child():
        yield v   # return value lost

def parent_yf():
    result = yield from child()
    print("Child returned:", result)

list(parent_yf())  # [1], prints "Child returned: 42"


'''
Q3. How does `yield from` handle StopIteration from the sub-generator?
Ans: It catches the StopIteration, takes its .value (return value),
and makes it available to the delegating generator.

Example:
'''
def child(): 
    return "done"

def parent():
    result = yield from child()
    print("Result:", result)

list(parent())  # [], prints "Result: done"

