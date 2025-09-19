'''
Q1. What is the difference between chained assignment and parallel assignment?
Ans: 
- Chained assignment: a = b = c = 10 → all names bound to the same object.  
- Parallel assignment: x, y = 1, 2 → tuple packing/unpacking; different names 
can refer to different objects at once.

Q2. What rule must be followed when unpacking values into variables?
Ans: The number of variables on the left must match the number of values 
on the right, unless a starred target (*) is used.

Q3. How do starred targets work in assignment?
Ans: A starred target collects multiple values into a list.  
Example: a, *b, c = [1,2,3,4,5] → a=1, b=[2,3,4], c=5.

Q4. What is nested unpacking in Python?
Ans: It allows unpacking inside unpacking patterns.  
Example: (a, b), c = [(1,2), 3] → a=1, b=2, c=3.

Q5. (Coding)
# Try the following and explain outputs
'''

# Chained assignment
a = b = c = []
a.append(1)
print("b after mutation:", b)  
# ✅ Output: [1]
# Explanation: a, b, c all reference the same list object. 
# Mutating via 'a' is visible through 'b' and 'c'.

# Parallel assignment
x, y = 5, 10
print("x+y:", x+y)  
# ✅ Output: 15
# Explanation: RHS forms a tuple (5,10), unpacked into x=5, y=10.

# Starred assignment
a, *b, c = [1, 2, 3, 4, 5]
print("a:", a, "b:", b, "c:", c)  
# ✅ Output: a=1, b=[2,3,4], c=5
# Explanation: *b collects all middle values into a list.

# Nested unpacking
(p, q), r = [(7, 8), 9]
print("p:", p, "q:", q, "r:", r)  
# ✅ Output: p=7, q=8, r=9
# Explanation: (7,8) unpacks into p,q and 9 goes to r.
