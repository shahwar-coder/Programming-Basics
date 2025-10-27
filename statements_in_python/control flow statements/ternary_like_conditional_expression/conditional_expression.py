'''
Q1. What is a conditional (ternary) expression in Python?
Ans:
- It’s a one-line form of `if-else` used to return a value based on a condition.  
- Syntax: `<expr1> if <condition> else <expr2>`
'''
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  
# Step-by-step:
# 1️⃣ Evaluate condition → age >= 18 → True.
# 2️⃣ Return "Adult" (expr1).
# 3️⃣ "Minor" (expr2) is skipped.



'''
Q2. How does it differ from a normal if-else statement?
Ans:
- Normal if-else controls *flow* (executes blocks).  
- Ternary expression *returns a value* (used inside assignments or functions).
'''
# Standard if-else:
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# Ternary equivalent:
status = "Adult" if age >= 18 else "Minor"



'''
Q3. When should you use a ternary expression?
Ans:
✅ When the logic is simple and fits in one line.  
🚫 Avoid when the condition or expressions are complex — reduces readability.
'''
# Good use:
status = "Even" if n % 2 == 0 else "Odd"

# Bad use (too complex):
result = x*y if (a+b > c and not flag) else z*(a-b)
# → Hard to read, better as normal if-else.



'''
Q4. Can you nest ternary expressions?
Ans:
✅ Yes, but readability suffers.  
Better to use `if-elif-else` for multi-branch logic.
'''
age = 16
group = "Child" if age < 13 else "Teen" if age < 18 else "Adult"
print(group)  # Teen
# Step-by-step:
# 1️⃣ age < 13 → False.
# 2️⃣ Next ternary → age < 18 → True → "Teen".



'''
Q5. Why is it called “ternary”?
Ans:
- Because it uses **three operands**:  
  (1) condition, (2) value if True, (3) value if False.
'''
a, b = 10, 20
min_val = a if a < b else b
# Operands → a (expr1), condition (a < b), b (expr2)



'''
Q6. Quick shorthand
✔ Syntax → expr1 if cond else expr2  
✔ Returns a value, not a statement  
✔ Use for short, simple decisions  
✔ Avoid nesting or long conditions  
✔ Improves clarity in inline assignments
'''
