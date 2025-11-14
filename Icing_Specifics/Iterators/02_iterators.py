'''
Q1. Is a for-loop an iterator or an iterable?
Ans:
Neither. A for-loop is just a control structure.  
It *uses* an iterable to get an iterator, then repeatedly calls next().
'''
# Example (internal steps)
# _it = iter([1,2,3])
# next(_it) → 1,2,3 … until StopIteration


'''
Q2. What does a for-loop do internally when looping over something?
Ans:
It calls iter() on the iterable to get an iterator, then repeatedly calls
next() inside a try/except StopIteration loop.
'''
# Example (Python’s hidden logic)
# it = iter(items)
# while True:
#     try:
#         x = next(it)
#     except StopIteration:
#         break
#     ...


'''
Q3. Why do beginners confuse for-loops with iterators?
Ans:
Because for-loops *use* next() implicitly. But the loop itself does not
produce values—the iterator does.
'''
# Example
# next() works only on an iterator, not on a for-loop.


'''
Q4. What part of iteration remembers the current position?
Ans:
Only the iterator remembers state.  
Iterables (list, tuple, string) do NOT store where you are in a loop.
'''
# Example
# it = iter([10,20]); next(it) → 10; next(it) → 20


'''
Q5. Can a for-loop be restarted?
Ans:
Yes. Because the iterable can create a NEW iterator each time.
'''
# Example
lst = [1, 2]
for x in lst: print(x)
for x in lst: print(x)   # works again (new iterator)


'''
Q6. What happens if you pass an iterator directly to a for-loop?
Ans:
The loop consumes it once. After exhaustion, further loops run 0 times.
'''
# Example
it = iter([1, 2])
for x in it: print(x)   # prints 1,2
for x in it: print(x)   # prints nothing (already exhausted)


'''
Q7. Why is iter() required even for simple for-loops?
Ans:
Because only an iterator knows how to produce the next item.
iter() converts an iterable into an iterator for the loop to use.
'''
# Example
# list → iterable; iter(list) → iterator


'''
Q8. Is every iterable automatically an iterator?
Ans:
No. Iterators implement both __iter__() and __next__().  
Iterables only implement __iter__().
'''
# Example
# next([1,2,3]) → TypeError (list is not an iterator)


'''
Q9. Why doesn’t next() work directly on a list?
Ans:
Because list has __iter__(), not __next__().
You must call next(iter(list)).
'''
# Example
lst = [3, 4]
it = iter(lst)
print(next(it))   # 3


'''
Q10. Final summary: What are the roles?
Ans:
• Iterable → holds the data  
• Iterator → delivers data step-by-step  
• for-loop → drives the iteration using next() behind the scenes  
The loop itself never stores items or remembers state.
'''
# Example
# for item in iterable: uses iterator protocol internally
