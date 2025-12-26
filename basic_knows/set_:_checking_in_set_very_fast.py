'''
Q1. What does O(1) membership testing mean for sets?
Ans. It means checking if an element exists in a set takes constant time.
'''
# Example
s = {1, 2, 3, 4, 5}
# 3 in s  → very fast (O(1))

'''
Q. Why are sets so fast at membership checking?
Ans. Because sets use hashing internally to locate elements instantly.
'''
# Example
# Hash → direct lookup
# No need to scan every element

'''
Q. How does membership testing work in lists?
Ans. Lists check elements one by one until a match is found.
'''
# Example
lst = [1, 2, 3, 4, 5]
# 5 in lst → may check many elements (O(n))

'''
Q. Which is faster for lookup: list or set?
Ans. Sets are much faster than lists for lookup operations.
'''
# Example
# list → O(n)
# set  → O(1)

'''
Q. When does this performance difference really matter?
Ans. When working with large data or frequent membership checks.
'''
# Example
# Checking usernames, IDs, visited pages, permissions
