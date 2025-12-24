'''
Q1. What does `add()` do in a set?
Ans. `add()` inserts ONE new element into the set.
'''
# Example
s = {1, 2}
s.add(3)
# s = {1, 2, 3}


'''
Q2. What does `update()` do in a set?
Ans. `update()` adds MULTIPLE elements from another iterable into the set.
'''
# Example
s = {1, 2}
s.update([2, 3, 4])
# s = {1, 2, 3, 4}


'''
Q3. What is the difference between `add()` and `update()`?
Ans. `add()` adds a single element, while `update()` adds many elements.
'''
# Example
# add(5)        → one element
# update([5,6]) → multiple elements


'''
Q4. What does `remove(x)` do?
Ans. It removes element `x` from the set, but raises an error if `x` is not present.
'''
# Example
s = {1, 2, 3}
s.remove(2)
# s = {1, 3}

# s.remove(5) ❌ KeyError


'''
Q5. What does `discard(x)` do?
Ans. It removes element `x` if present, and does NOTHING if it is not.
'''
# Example
s = {1, 2, 3}
s.discard(2)
# s = {1, 3}

s.discard(5)
# No error 👍


'''
Q6. What does `pop()` do in a set?
Ans. It removes and returns a RANDOM element from the set.
'''
# Example
s = {10, 20, 30}
x = s.pop()
# x → some element
# s → remaining elements


'''
Q7. What does `clear()` do?
Ans. It removes ALL elements from the set, making it empty.
'''
# Example
s = {1, 2, 3}
s.clear()
# s = set()


'''
Q8. What is the one-line rule to remember?
Ans. Use `add/update` to insert, and `remove/discard/pop/clear` to delete set elements.
'''
# Example (lock it 🔒)
# remove → error if missing
# discard → safe removal
# pop → random removal
# clear → empty set
