'''
Q. How can short-circuit logic be used in real code?
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
