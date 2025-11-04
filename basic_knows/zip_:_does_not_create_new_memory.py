'''
Q. Does zip() create a new list in memory?
Ans:
No — it returns a *lazy iterator*.  
Data isn’t stored in memory until you explicitly convert it (e.g., with list()).
'''
# Example
z = zip(range(1000000), range(1000000))
# Memory efficient — doesn't build a huge list
