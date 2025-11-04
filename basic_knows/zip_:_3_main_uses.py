'''
Q. What are some common uses of zip()?
Ans:
- Pairing related data (like names and scores)  
- Looping through multiple lists together  
- Unzipping data using the * operator
'''

# Example 1 — Pairing related data
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

paired = list(zip(names, scores))
print(paired)
# [('Alice', 85), ('Bob', 90), ('Charlie', 78)]


# Example 2 — Looping together
subjects = ["Math", "Science", "English"]
marks = [95, 88, 76]

for subject, mark in zip(subjects, marks):
    print(f"{subject}: {mark}")
# Math: 95
# Science: 88
# English: 76

# ===================================================

# Example 2 — Looping together
subjects = ["Math", "Science", "English"]
marks = [95, 88, 76]

for subject, mark in zip(subjects, marks):
    print(f"{subject}: {mark}")

# ====================================================

# Example 3 — Unzipping
pairs = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]

names, scores = zip(*pairs)

print(names)
print(scores)
# ('Alice', 'Bob', 'Charlie')
# (85, 90, 78)

