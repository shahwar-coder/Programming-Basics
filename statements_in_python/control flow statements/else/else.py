'''
Q1. What does the `else` after an `if` do?
Ans:
- `else` is the fallback branch: it runs only when the `if` condition is False.
Example:
'''
x = 7
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# Step-by-step:
# 1. Evaluate x % 2 == 0 -> False
# 2. `if` block skipped
# 3. `else` block runs -> prints "Odd"



'''
Q2. How do `if` / `elif` / `else` chains behave?
Ans:
- Python evaluates conditions top-down; the first True branch runs and the chain ends.
- `else` runs only if none of the preceding `if`/`elif` conditions were True.
Example (grading):
'''
score = 82
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C"
print(grade)

# Step-by-step:
# 1. Check score >= 90 -> False
# 2. Check score >= 75 -> True -> set grade "B"
# 3. Skip remaining branches (including else)



'''
Q3. Loop `else` — what is that? (very useful pattern)
Ans:
- `else` after a `for` or `while` runs **only if the loop completed normally** (no `break`).
- Useful for “search” patterns to avoid flags.
'''
# Problem (flag approach):
found = False
for x in items:
    if is_target(x):
        print("Found")
        found = True
        break
if not found:
    print("Not found")

# Better: loop-else
for x in items:
    if is_target(x):
        print("Found")
        break
else:
    print("Not found")

# Step-by-step (loop-else version):
# 1. Iterate items; on target -> print and break (else skipped).
# 2. If loop finishes without break -> else runs -> print "Not found".



'''
Q4. `try` / `except` / `else` — how `else` helps
Ans:
- `else` after `try/except` runs only if the `try` block did NOT raise an exception.
- Use `else` to keep the `try` block minimal (only the code that may raise).
Example:
'''
s = "123"
try:
    value = int(s)       # only this in try
except ValueError:
    print("Bad number")
else:
    print("Parsed:", value)

# Step-by-step:
# 1. int(s) succeeds -> no exception.
# 2. except skipped.
# 3. else runs -> prints "Parsed: 123".
# Benefit: code in else is not inside the try, so unrelated exceptions won't be swallowed.



'''
Q5. Common pitfalls & best-practice hints
Ans:
'''
# - **Unnecessary `else` after `return`**: avoid redundant nesting.
  # Problem:
  def f(x):
      if x > 0:
          return "pos"
      else:
          return "non-pos"
  # Better:
  def f(x):
      if x > 0:
          return "pos"
      return "non-pos"
  # Step-by-step:
  # 1. Both behave the same, but second is clearer and avoids extra indentation.

# - **Misreading loop-else**: many expect `else` to run when loop had a truthy last item — it only runs when loop was NOT terminated by `break`.
# - **Overusing else**: sometimes an explicit `if` + early `return` or well-named helper makes code clearer than complex branching.
'''



'''
Q6. Quick reference: when `else` runs
Ans:
- `if/else` -> runs when condition False.
- `for/while/else` -> runs if loop completed without `break`.
- `try/except/else` -> runs if `try` raised no exception.
# Keep these three in your pocket for quick decisions.
'''
