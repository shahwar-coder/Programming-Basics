'''
Q1. What is the difference between packing and unpacking in Python?
Ans: 
- Packing: combining multiple values into one object (usually a tuple).
  Example: t = 1, 2, 3 → t is a tuple (1,2,3).  
- Unpacking: extracting values from an iterable into individual names.  
  Example: a, b, c = t → a=1, b=2, c=3.

Q2. When does unpacking raise a ValueError?
Ans: If the number of variables on the left does not match the number 
of items on the right (unless a starred target is used).  
Example: a, b = [1,2,3] → ValueError.

Q3. How does starred unpacking help avoid errors?
Ans: It allows one variable to collect multiple values into a list.  
Example: a, *b, c = [1,2,3,4,5] → a=1, b=[2,3,4], c=5.

Q4. What is nested unpacking?
Ans: It allows unpacking inside other unpacking patterns.  
Example: (a,b), c = [(1,2), 3] → a=1, b=2, c=3.

Q5. (Coding)
# Predict the output
# Extended unpacking with * inside list
'''

nums = [*range(3), *[3,4], 5]
print(nums)

# ✅ Output: [0, 1, 2, 3, 4, 5]

# Reasoning:
# range(3) → 0,1,2
# *range(3) unpacks → 0,1,2
# *[3,4] unpacks → 3,4
# then literal 5
# Combined → [0, 1, 2, 3, 4, 5]
