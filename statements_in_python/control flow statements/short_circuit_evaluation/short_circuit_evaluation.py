'''
Q1. What is short-circuit evaluation in Python?
Ans:
- It means `and` and `or` operators evaluate only as much as needed.
- The second expression is skipped if the first already determines the result.
'''
# Example 1:
print(False and print("Skipped"))
print(True or print("Skipped"))
# Step-by-step:
# 1️⃣ 'and' stops since False makes whole False → no right eval.
# 2️⃣ 'or' stops since True makes whole True → skips right side.



'''
Q2. How does short-circuiting work for 'and'?
Ans:
- In `a and b`, if `a` is falsy → stop immediately and return `a`.
- If `a` is truthy → evaluate and return `b`.
'''
x = 0
y = 10
print(x and y)   # 0 (left falsy → stop)
print(5 and y)   # 10 (left truthy → returns right)




'''
Q3. How does short-circuiting work for 'or'?
Ans:
- In `a or b`, if `a` is truthy → stop immediately and return `a`.
- If `a` is falsy → evaluate and return `b`.
'''
x = ""
y = "Hello"
print(x or y)    # "Hello" (left falsy → right returned)
print("Hi" or y) # "Hi" (left truthy → stop early)



'''
Q4. What is actually *returned* from short-circuit expressions?
Ans:
- Python returns the **value of the operand** that determined the result,
  not strictly True/False.
'''
print(5 and 10)   # 10 is returned
print(5 or 10)    # 5 is returned
# Check below comments for details

# Important to undestand that:
# 1. and/or does not retun any True/False directly. They return Truty/Falsy and those can be values.
# 2. When you do 5 and 10, 1st 5 is checked (Truty), since it's 'and' we go to right part as well, 10 is also Truthy, now the lastest (10) is returned.
# 3. When you do 5 or 10, 1st 5 is checked, it's Truthy,, since since Truthy is already found we stop ther and 5 is returned. 



'''
Q5. How can short-circuit logic be used in real code?
Ans:
✅ For defaults or conditional assignments.  
✅ To safely call functions only when needed.  
⚠ Avoid when right-hand side has side effects.
'''
# Example 1: Default username if none provided
user_input = ""
name = user_input or "Guest"
print("Hello,", name)

# Step-by-step:
# 1️⃣ user_input = "" → falsy
# 2️⃣ 'or' moves to right side → returns "Guest"
# ✅ Output → "Hello, Guest"


# Example 2: Only run a function if condition is True
is_admin = False
is_admin and print("Access granted!")

# Step-by-step:
# 1️⃣ 'and' stops if left side is falsy.
# 2️⃣ is_admin = False → short-circuits → print() never runs.
# ✅ No output (safe skip)


# Example 3: Function on right side may never run
def notify():
    print("Notification sent!")

flag = True
flag or notify()   # notify() never runs

# Step-by-step:
# 1️⃣ 'or' stops when left is truthy.
# 2️⃣ Right side (notify) skipped — side effect lost.
# ⚠ Be careful: sometimes you expect it to run but it won’t.
