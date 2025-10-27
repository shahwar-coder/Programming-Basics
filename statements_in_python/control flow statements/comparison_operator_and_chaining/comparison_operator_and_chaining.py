'''
Q1. What are comparison operators used for in Python?
Ans:
- They’re used to compare two values and return a Boolean result (`True` or `False`).
- Form the foundation of conditional statements (if, while).
'''
x = 10
print(x > 5)   # True
print(x == 5)  # False
# Step-by-step:
# 1️⃣ Compare x to 5.
# 2️⃣ Output a Boolean (True/False).



'''
Q2. How does Python handle equality and inequality?
Ans:
- `==` checks if two values are equal.  
- `!=` checks if they are not equal.
'''
a, b = 7, 7
print(a == b)  # True
print(a != b)  # False
# Step-by-step:
# a == b → same value → True.
# a != b → not different → False.



'''
Q3. What’s the use of relational operators (<, >, <=, >=)?
Ans:
- They compare the **magnitude** or **order** of two numbers.
'''
score = 85
if score >= 50:
    print("Pass")
else:
    print("Fail")
# Step-by-step:
# 1️⃣ score compared to 50.
# 2️⃣ True → executes the 'Pass' block.



'''
Q4. What is comparison chaining and how does it work?
Ans:
- It allows combining multiple comparisons compactly.
- Python evaluates them left to right and stops early if False.
'''
x = 5
if 0 < x < 10:
    print("x is between 0 and 10")
# Equivalent to: (0 < x) and (x < 10)
# Step-by-step:
# 1️⃣ 0 < x → True
# 2️⃣ x < 10 → True
# 3️⃣ Combined → True → executes print.



'''
Q5. What are the benefits of comparison chaining in Python?
Ans:
✅ More readable and Pythonic.  
✅ Avoids redundancy (`x > 0 and x < 10`).  
✅ Efficient — stops early if a comparison fails.
'''
x = -2
if 0 < x < 10:
    print("Inside range")
else:
    print("Outside range")
# First test (0 < x) fails → skips second test immediately.



'''
Q6. Quick shorthand
✔ ==, != → equality/inequality  
✔ <, >, <=, >= → magnitude comparison  
✔ 0 < x < 10 → clean chained syntax  
✔ Stops early if one part fails  
✔ Equivalent to 'and' between conditions
'''
