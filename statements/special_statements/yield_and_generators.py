'''
Q1. What does yield do in a function?
Ans: Turns the function into a generator. 
It pauses execution and produces one value at a time.
Example:
'''

def g(): yield 1; yield 2
print(list(g()))   # [1, 2]




'''
Q2. What happens when a generator hits return?
Ans: It stops the generator. 
If return has a value, it's stored in StopIteration.value.
Example:
'''

def g(): return 99
try: next(g())
except StopIteration as e: print(e.value)   # 99




'''
Q3. What is the purpose of yield from?
Ans: It delegates iteration to a sub-generator, yields all its values, 
and captures its return value.

-> In Python, “delegation” in the context of yield from means that one generator hands off part of its work (yielding values, receiving sends, handling throws, etc.) to another generator or iterable. The delegating generator acts like a proxy / tunnel, allowing the sub-generator to manage iteration until it’s exhausted.
'''

'''
Example 1:
'''
def child(): yield 1; return "done"
def parent(): result = yield from child(); print("child returned:", result)
list(parent())   # [1], prints: child returned: done


'''
Example 2:
'''
def subgen():
    yield 1
    yield 2
    return "Done"

def delegator():
    print("Delegator: Before delegation")
    result = yield from subgen()
    print("Delegator: After delegation, got:", result)
    yield "Back in delegator"

# Using the generator
for value in delegator():
    print("Received:", value)




'''
Q4. Why don’t you usually see StopIteration with generators?
Ans: Because for-loops handle next() and StopIteration automatically.
Example:
'''

def g(): yield "a"; yield "b"
for val in g(): print(val)   # a, b (no StopIteration visible)
