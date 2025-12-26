'''
Q1. How do you create a `frozenset` in Python?
Ans. Use the `frozenset()` constructor with an iterable.
'''
# Example
fs = frozenset([1, 2, 3])
# fs = frozenset({1, 2, 3})


'''
Q2. Can you create an empty `frozenset`?
Ans. Yes. Just call `frozenset()` with no arguments.
'''
# Example
empty_fs = frozenset()
# frozenset()


'''
Q3. Can elements be added or removed from a `frozenset`?
Ans. No. A `frozenset` cannot be modified after creation.
'''
# Example
fs = frozenset([1, 2])
# fs.add(3)     ❌ error
# fs.remove(1)  ❌ error


'''
Q4. Why does the hash value of a `frozenset` never change?
Ans. Because the elements inside it can never change.
'''
# Example
fs = frozenset([1, 2, 3])
# hash(fs) is always the same


'''
Q5. Why is a stable hash value important?
Ans. Because it allows `frozenset` to be safely used as dictionary keys or set elements.
'''
# Example
d = {frozenset([1, 2]): "group A"}


'''
Q6. Does element order matter in a `frozenset`?
Ans. No. Like sets, `frozenset` is unordered.
'''
# Example
frozenset([1, 2, 3]) == frozenset([3, 2, 1])  # True


'''
Q7. Are duplicate elements allowed in a `frozenset`?
Ans. No. Duplicates are automatically removed, just like in sets.
'''
# Example
frozenset([1, 2, 2, 3])
# Result → frozenset({1, 2, 3})


'''
Q8. What is the one-line rule to remember?
Ans. A `frozenset` is an immutable, unordered, hashable set created using `frozenset(iterable)`.
'''
# Example (lock it 🔒)
# No change + stable hash + no order
