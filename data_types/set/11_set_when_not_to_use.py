'''
Q1. When should you NOT use a set?
Ans. When the order of elements matters.
'''
# Example
# Sequence of steps, rankings, history
# Use list or tuple instead


'''
Q2. Why are sets bad when duplicates matter?
Ans. Because sets remove duplicates automatically.
'''
# Example
scores = [10, 10, 20]
set(scores)   # {10, 20} ❌ duplicate lost


'''
Q3. Why can’t you use sets when indexing is required?
Ans. Because sets do not support indexing or slicing.
'''
# Example
s = {1, 2, 3}
# s[0] ❌ not allowed


'''
Q4. What is the one-line rule to remember?
Ans. Use sets for uniqueness and fast checks; avoid them when order, duplicates, or indexing matter.
'''
# Example (lock it 🔒)
# Unique + fast lookup → set
# Ordered / indexed / duplicate data → list or tuple
