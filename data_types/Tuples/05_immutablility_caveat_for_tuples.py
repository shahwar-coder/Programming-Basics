'''
Q1. What does immutability mean for a tuple?
Ans. It means the tuple itself cannot be changed after creation.
'''
# Example
t = (1, 2, 3)
# t[0] = 99 ❌ not allowed


'''
Q2. What exactly is not allowed in a tuple?
Ans. You cannot add, remove, or replace elements of the tuple.
'''
# Example
t = (10, 20)
# t.append(30) ❌
# t[1] = 50    ❌


'''
Q3. What is the immutability caveat with tuples?
Ans. While the tuple structure is fixed, mutable objects inside it can still change.
'''
# Example
t = (1, [2, 3], 4)


'''
Q4. Can the list inside a tuple be modified?
Ans. Yes. The list itself is mutable, even though the tuple is not.
'''
# Example
t = (1, [2, 3], 4)
t[1].append(99)
# t is now (1, [2, 3, 99], 4)


'''
Q5. Why is this not considered “changing the tuple”?
Ans. Because the tuple still points to the same objects; only the internal state of a mutable object changes.
'''
# Example
# The list reference stays the same
# Only its contents change


'''
Q6. What is still NOT allowed even with mutable elements?
Ans. You cannot replace the mutable object itself with another object.
'''
# Example
t = (1, [2, 3], 4)
# t[1] = [9, 9] ❌ not allowed


'''
Q7. Why is this caveat important in real programs?
Ans. Because it can cause unexpected side effects if you assume tuples are “deeply immutable.”
'''
# Example
# Tuple used as config but contains a list → config can still change!


'''
Q8. What is the one-line rule to remember?
Ans. Tuples are immutable, but mutable elements inside them can still change.
'''
# Example (lock it 🔒)
# Tuple structure → fixed
# Mutable contents → changeable
