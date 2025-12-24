'''
Q1. What operations are supported by `frozenset`?
Ans. `frozenset` supports all read-only set operations like union, intersection, difference, and symmetric difference.
'''
# Example
a = frozenset({1, 2, 3})
b = frozenset({3, 4})

a | b   # union → frozenset({1, 2, 3, 4})
a & b   # intersection → frozenset({3})
a - b   # difference → frozenset({1, 2})
a ^ b   # symmetric difference → frozenset({1, 2, 4})


'''
Q2. Does `frozenset` support membership testing?
Ans. Yes. You can check if an element exists using `in`.
'''
# Example
fs = frozenset({10, 20, 30})
20 in fs    # True
40 in fs    # False


'''
Q3. Can you check subset and superset relations with `frozenset`?
Ans. Yes. Subset and superset checks work exactly like with sets.
'''
# Example
a = frozenset({1, 2})
b = frozenset({1, 2, 3})

a.issubset(b)     # True
b.issuperset(a)   # True


'''
Q4. Do set operations on frozensets return sets or frozensets?
Ans. They return a new `frozenset` when both operands are frozensets.
'''
# Example
type(a | b)   # frozenset


'''
Q5. Why are these operations allowed on an immutable structure?
Ans. Because they do not modify the original frozenset; they create new ones.
'''
# Example
# a remains unchanged after a | b


'''
Q6. What operations are NOT supported by `frozenset`?
Ans. Any operation that tries to modify the data is not allowed.
'''
# Example
# fs.add(1)      ❌
# fs.remove(1)   ❌
# fs.pop()       ❌
# fs.clear()     ❌
# fs.update(...) ❌


'''
Q7. Why are modification methods not supported?
Ans. Because `frozenset` is immutable and must never change after creation.
'''
# Example
# Immutability guarantees safety and hash stability


'''
Q8. What is the one-line rule to remember?
Ans. `frozenset` supports all non-mutating set operations but forbids all modifying ones.
'''
# Example (lock it 🔒)
# Read-only set math → allowed
# Any change → NOT allowed
