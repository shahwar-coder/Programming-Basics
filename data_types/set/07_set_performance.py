'''
Q1. What does O(1) membership testing mean for sets?
Ans. It means checking if an element exists in a set takes constant time.
'''
# Example
s = {1, 2, 3, 4, 5}
# 3 in s  → very fast (O(1))


'''
Q2. Why are sets so fast at membership checking?
Ans. Because sets use hashing internally to locate elements instantly.
'''
# Example
# Hash → direct lookup
# No need to scan every element


'''
Q3. How does membership testing work in lists?
Ans. Lists check elements one by one until a match is found.
'''
# Example
lst = [1, 2, 3, 4, 5]
# 5 in lst → may check many elements (O(n))


'''
Q4. Which is faster for lookup: list or set?
Ans. Sets are much faster than lists for lookup operations.
'''
# Example
# list → O(n)
# set  → O(1)


'''
Q5. When does this performance difference really matter?
Ans. When working with large data or frequent membership checks.
'''
# Example
# Checking usernames, IDs, visited pages, permissions


'''
Q6. Why are sets preferred for “exists?” checks?
Ans. Because they scale well even when the data size grows very large.
'''
# Example
# 1 million items:
# list lookup → slow
# set lookup  → still fast


'''
Q7. Does O(1) mean always exactly the same time?
Ans. Practically yes, but internally it means average constant time.
'''
# Example
# Minor variations exist, but performance is stable


'''
Q8. What is the one-line rule to remember?
Ans. Use sets for fast membership testing; they are much faster than lists.
'''
# Example (lock it 🔒)
# Lookup-heavy task → use set
