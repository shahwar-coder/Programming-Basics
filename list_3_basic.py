'''
Mutating a list: "Multiple proofs of list being mutable // Printing the same list but it gets updated every time."
'''

# Define List:
lst = [1,2,3]
print(f"List : {lst}")

# Simple Indexing
lst[0]
print(f"List : {lst}")

# Add at end
lst.append(4)
print(f"List : {lst}")

# Extend it
lst.extend([5,6])
print(f"List : {lst}")

# Pop last Index
lst.pop()
print(f"List : {lst}")

# Pop specific index:
lst.pop(1)
print(f"List : {lst}")

# Insert at specific index:
lst.insert(2, "shahwar")
print(f"List : {lst}")

# Insert at another index same thing:
lst.insert(3, "shahwar")
print(f"List : {lst}")

# Remove 1st Instance of an element:
lst.remove("shahwar")
print(f"List : {lst}")
