'''
Q1. What are Boolean operators in Python and their purpose?
Ans:
- Boolean operators combine multiple conditions into a single logical test.
- The three are: `and`, `or`, and `not`.
'''
x, y = 5, 10
if x > 0 and y > 0:
    print("Both positive")

# Step-by-step:
# 1️⃣ x > 0 → True
# 2️⃣ y > 0 → True
# 3️⃣ True and True → overall True → executes print



'''
Q2. How do and, or, and not differ logically?
Ans:
- and → True only if both conditions True.  
- or  → True if at least one condition True.  
- not → Inverts the Boolean value.
'''
x, y = 5, -1
print(x > 0 and y > 0)  # False
print(x > 0 or y > 0)   # True
print(not(x > 0))       # False



'''
Q3. What is the precedence order of Boolean operators?
Ans:
1️⃣ not  
2️⃣ and  
3️⃣ or  
Use parentheses to override this order for clarity.
'''
x = True
y = False
z = True
print(x or y and not z)       # x or (y and (not z)) → True or (False and False) → True
print((x or y) and not z)     # (True or False) and False → False



'''
Q5. What’s a common pitfall with or/and evaluation?
Ans:
- Short-circuiting: Python stops evaluating once the result is known.
  → and stops at first False, or stops at first True.
'''
def test(msg):
    print(msg)
    return True

# Short-circuit demo
print(False and test("Won’t print"))  # Stops before calling test()
print(True or test("Won’t print"))    # Stops before calling test()



'''
Q6. Quick shorthand
✔ and → both True  
✔ or → at least one True  
✔ not → invert  
✔ Precedence: not > and > or  
✔ Use parentheses for clarity  
✔ Remember short-circuit behavior
'''
