# frozenset : set :: tuple : list

'''
Q1. What does the mental model `frozenset : set :: tuple : list` mean?
Ans. It means frozenset is the immutable version of set, just like tuple is the immutable version of list.
'''
# Example
# list  → mutable sequence
# tuple → immutable sequence
# set   → mutable unique collection
# frozenset → immutable unique collection

'''
Q2. Why is this mental model helpful?
Ans. It helps you quickly remember when to use mutable vs immutable collections.
'''
# Example
# Need changes → list / set
# Need safety → tuple / frozenset

'''
Q3. How does this model help in API design?
Ans. It helps choose immutable types to prevent accidental modification.
'''
# Example
# Return frozenset instead of set → safer API
