'''
Q1. What is a `frozenset`?
Ans. A `frozenset` is an immutable and unordered collection of unique elements.
'''
# Example
fs = frozenset([1, 2, 3])
# Like a set, but cannot be changed


'''
Q2. How is `frozenset` different from `set`?
Ans. A set is mutable, but a frozenset is immutable.
'''
# Example
s = {1, 2}
fs = frozenset({1, 2})

s.add(3)     # ✅ allowed
# fs.add(3)  ❌ error (frozenset is immutable)


'''
Q3. Why is `frozenset` hashable?
Ans. Because it is immutable, its contents cannot change.
'''
# Example
# Hashable → can be used as a dictionary key
# yes hashable simply means it can  be used as a key


'''
Q4. Why can `frozenset` be used as a dictionary key?
Ans. Because dictionary keys must be hashable, and frozenset is hashable.
'''
# Example
groups = {
    frozenset({"a", "b"}): "Group 1",
    frozenset({"c", "d"}): "Group 2"
}


'''
Q5. Why can `frozenset` be stored inside another set?
Ans. Because frozenset is hashable, unlike normal sets.
'''
# Example
nested = {
    frozenset({1, 2}),
    frozenset({3, 4})
}


'''
Q6. Why does Python not allow normal sets inside sets?
Ans. Because normal sets are mutable and not hashable.
'''
# Example
# s = {{1, 2}}  ❌ TypeError
# frozenset works ✔️


'''
Q7. When should you use `frozenset`?
Ans. When you need a set that must never change and be used as a key or element.
'''
# Example
# Permission sets, fixed groups, cache keys


'''
Q8. What is the one-line rule to remember?
Ans. `frozenset` is an immutable, hashable version of a set.
'''
# Example (lock it 🔒)
# Immutable set → frozenset
