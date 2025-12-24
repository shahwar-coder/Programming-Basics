'''
Q1. Why do set elements have to be unique?
Ans. Because a set is designed to store only one copy of each value.
'''
# Example
s = {1, 2, 2, 3}
# Result → {1, 2, 3}


'''
Q2. What does “hashable” mean in simple words?
Ans. Hashable means the value can be safely identified and does not change.
'''
# Example
# Hashable values have a fixed identity in memory.


'''
Q3. Why must elements in a set be hashable?
Ans. Because Python uses hashing to store and quickly find elements in a set.
'''
# Example
# Fast lookup → uses hash internally
# That’s why set membership is very fast


'''
Q4. Which common types are hashable and allowed in sets?
Ans. int, float, str, and tuple (if it contains only hashable items).
'''
# Examples
s1 = {1, 2, 3}
s2 = {"a", "b"}
s3 = {(1, 2), (3, 4)}


'''
Q5. Are tuples always hashable?
Ans. Only if all elements inside the tuple are hashable.
'''
# Example
(1, 2)           # ✅ hashable
(1, [2, 3])     # ❌ not hashable (contains list)


'''
Q6. Why are lists NOT allowed inside sets?
Ans. Because lists are mutable and their values can change.
'''
# Example
# s = {[1, 2]}  ❌ TypeError: unhashable type: 'list'


'''
Q7. Why are dict and set not allowed as set elements?
Ans. Because they are mutable and not hashable.
'''
# Example
# s = {{1: 2}}  ❌ error
# s = {{1, 2}}  ❌ error


'''
Q8. What is the one-line rule to remember?
Ans. Set elements must be hashable: immutable types are allowed, mutable ones are not.
'''
# Example (lock it 🔒)
# int, str, tuple → allowed
# list, dict, set → NOT allowed
