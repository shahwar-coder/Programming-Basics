'''
Q1. Why can `frozenset` be used as dictionary keys?
Ans. Because `frozenset` is immutable and hashable, which is required for dict keys.
'''
# Example
permissions = {
    frozenset({"read", "write"}): "editor",
    frozenset({"read"}): "viewer"
}


'''
Q2. How is `frozenset` useful for graph edges?
Ans. It represents an unordered edge between two nodes safely.
'''
# Example
# Edge between A and B (same as B and A)
edge = frozenset(("A", "B"))
# frozenset(("B", "A")) → same edge


'''
Q3. Why are `frozenset`s good for unique combinations?
Ans. Because order doesn’t matter and duplicates are removed automatically.
'''
# Example
combo1 = frozenset((1, 2))
combo2 = frozenset((2, 1))
# combo1 == combo2 → True


'''
Q4. How do `frozenset`s help in storing sets inside sets?
Ans. Because frozensets are hashable, unlike normal sets.
'''
# Example
set_of_sets = {
    frozenset({1, 2}),
    frozenset({3, 4})
}


'''
Q5. Why are `frozenset`s called safe collections?
Ans. Because their contents cannot be modified after creation.
'''
# Example
roles = frozenset({"admin", "user"})
# roles.add("guest") ❌ not allowed


'''
Q6. When should you use `frozenset` instead of `set`?
Ans. When the collection must stay fixed and be safely shared or reused.
'''
# Example
# Configuration flags
# Permission sets
# Cache keys


'''
Q7. How do `frozenset`s reduce bugs in programs?
Ans. Immutability prevents accidental changes and side effects.
'''
# Example
# Passing frozenset to functions → no mutation risk


'''
Q8. What is the one-line rule to remember?
Ans. Use `frozenset` for fixed, unordered, hashable collections.
'''
# Example (lock it 🔒)
# Fixed + hashable + unordered → frozenset
