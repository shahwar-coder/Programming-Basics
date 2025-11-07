'''
Q1. What does any(iterable) do?
Ans:
It returns **True** if *at least one* element in the iterable is truthy.  
If *all elements* are falsy, it returns **False**.
'''
# Example
print(any([0, 0, 5]))      # True  → 5 is truthy
print(any([0, '', False])) # False → all falsy



'''
Q2. How does any() handle empty iterables?
Ans:
For an **empty iterable**, `any()` returns **False**,  
since there are no truthy elements.
'''
# Example
print(any([]))       # False
print(any(()))       # False



'''
Q3. What kinds of iterables can you use with any()?
Ans:
It works with **any iterable** — lists, tuples, sets, dictionaries, or generators.  
For dictionaries, it checks the **keys**.
'''
# Example
print(any((0, 0, 1)))        # True
print(any({0, 0, 0}))        # False
print(any({'a': 0, 'b': 0})) # True (non-empty dict → keys are truthy)



'''
Q4. How does any() determine truthiness?
Ans:
It converts each element using `bool(x)` —  
if it finds one truthy element, it immediately returns True (short-circuiting)
'''
# Example
print(any(["", 0, "Hello"]))   # True → "Hello" is truthy
print(any(["", 0, []]))        # False → all falsy



'''
Q5. How does short-circuiting work in any()?
Ans:
`any()` stops checking as soon as it finds the first truthy value,  
which makes it efficient for large iterables.
'''



'''
Q6. How is any() different from all()?
Ans:
- `all()` → True if **every** element is truthy  
- `any()` → True if **at least one** element is truthy
'''
# Example
print(all([1, 0, 3]))  # False
print(any([1, 0, 3]))  # True




'''
Q7. Can any() work with generator expressions?
Ans:
Yes — `any()` can take generators, evaluating elements lazily (one by one).
'''
# Example
nums = [0, 0, 2, 4]
print(any(n > 0 for n in nums))  # True
